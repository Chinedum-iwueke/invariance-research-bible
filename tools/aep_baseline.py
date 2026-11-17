#!/usr/bin/env python3
"""Read-only replay of pinned AEP evidence, never an autonomy certificate."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

DISPOSITIONS = {'repair', 'await_data', 'scientifically_infeasible',
                'requirements_conflict', 'requires_new_question', 'await_authority_or_capacity'}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def validate(manifest, repository):
    if manifest.get('schema_version') != 'aep-failure-corpus-v1':
        raise ValueError('unsupported schema')
    cases = manifest.get('cases', [])
    if not cases or len(cases) > 100:
        raise ValueError('require 1..100 cases')
    ids, cache = set(), {}
    for case in cases:
        if case['id'] in ids:
            raise ValueError('duplicate case')
        ids.add(case['id'])
        if case['split'] not in {'development', 'held_out'}:
            raise ValueError('invalid split')
        if case['evidence_kind'] not in {'historical_report', 'synthetic_fault'}:
            raise ValueError('invalid evidence kind')
        label = case['label']
        if label['proposed_disposition'] not in DISPOSITIONS or not label['rationale']:
            raise ValueError('invalid label')
        if label['review_status'] != 'pending_independent_review':
            raise ValueError('baseline v1 cannot confer independent label approval')
        source = case['source']
        if source['repository'] != 'swarm-control-plane':
            raise ValueError('unmapped repository')
        path = PurePosixPath(source['path'])
        if path.is_absolute() or '..' in path.parts or not source['path'].startswith(('docs/', 'worker/tests/')):
            raise ValueError('unsafe evidence path')
        if not re.fullmatch(r'[0-9a-f]{40}', source['commit']):
            raise ValueError('require exact source commit')
        key = (source['commit'], source['path'])
        if key not in cache:
            result = subprocess.run(['git', '-C', str(repository), 'show', ':'.join(key)],
                                    check=True, capture_output=True, timeout=30)
            cache[key] = result.stdout
        content = cache[key]
        if hashlib.sha256(content).hexdigest() != source['sha256']:
            raise ValueError('source digest mismatch: ' + case['id'])
        if not source['anchor'] or source['anchor'].encode() not in content:
            raise ValueError('source anchor missing: ' + case['id'])
        baseline = case['baseline']
        if baseline['human_intervention'] not in (True, False, None):
            raise ValueError('invalid intervention observation')
        for field in ('autonomous_episode_completed', 'native_terminal_receipt', 'model_tokens', 'billed_cost'):
            if baseline[field] is not None:
                raise ValueError('historical replay cannot infer execution metrics')
    return cases


def report(manifest, repository):
    cases = validate(manifest, repository)
    result = {
        'schema_version': 'aep-baseline-report-v1', 'manifest_digest': digest(manifest),
        'source_verification': 'passed', 'case_count': len(cases),
        'splits': dict(sorted(Counter(c['split'] for c in cases).items())),
        'evidence_kinds': dict(sorted(Counter(c['evidence_kind'] for c in cases).items())),
        'research_mechanisms': sorted({c['mechanism'] for c in cases if c['evidence_kind']=='historical_report'}),
        'observed_outcomes': dict(sorted(Counter(c['baseline']['observed_outcome'] for c in cases).items())),
        'labels_pending_independent_review': len(cases),
        'known_human_assisted_cases': sum(c['baseline']['human_intervention'] is True for c in cases),
        'new_model_calls': 0, 'new_backtests': 0, 'new_autonomous_attempts': 0,
        'autonomous_completion_rate': None, 'verified_task_completion_rate': None,
        'recovery_success_rate': None, 'billed_cost': None,
        'production_certified': False,
        'claim_boundary': 'Pinned historical-report replay, not raw artifact replay, live verification or independent label adjudication.'
    }
    return {**result, 'report_digest': digest(result)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, default=Path(__file__).resolve().parents[1] / 'plans/evidence/AEP-001/cases.json')
    args = parser.parse_args()
    try:
        result = report(json.loads(args.manifest.read_text()), args.repository)
    except (ValueError, KeyError, subprocess.SubprocessError) as error:
        parser.exit(1, f'AEP baseline failed: {error}\n')
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
