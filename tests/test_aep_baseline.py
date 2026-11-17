import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('aep_baseline', ROOT / 'tools/aep_baseline.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class AepBaselineTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / 'plans/evidence/AEP-001/cases.json').read_text())

    def test_digest_is_order_independent(self):
        self.assertEqual(module.digest({'a': 1, 'b': 2}), module.digest({'b': 2, 'a': 1}))

    def test_all_claims_remain_unknown_without_execution(self):
        with patch.object(module, 'validate', return_value=self.manifest['cases']):
            result = module.report(self.manifest, '.')
        self.assertIsNone(result['autonomous_completion_rate'])
        self.assertFalse(result['production_certified'])
        self.assertEqual(0, result['new_autonomous_attempts'])
        self.assertEqual(len(self.manifest['cases']), result['labels_pending_independent_review'])

    def test_unsafe_path_and_unpinned_source_fail_before_git(self):
        for field, value in [('path', '../secret'), ('path', '/etc/passwd'), ('commit', 'HEAD')]:
            manifest = copy.deepcopy(self.manifest)
            manifest['cases'][0]['source'][field] = value
            with patch.object(module.subprocess, 'run') as run:
                with self.assertRaises(ValueError):
                    module.validate(manifest, '.')
                run.assert_not_called()

    def test_source_tampering_fails(self):
        with patch.object(module.subprocess, 'run') as run:
            run.return_value.stdout = b'wrong content'
            with self.assertRaisesRegex(ValueError, 'digest mismatch'):
                module.validate(self.manifest, '.')

    def test_schema_and_label_escalation_fail(self):
        for change in ('schema', 'label'):
            manifest = copy.deepcopy(self.manifest)
            if change == 'schema':
                manifest['schema_version'] = 'unknown'
            else:
                manifest['cases'][0]['label']['review_status'] = 'approved'
            with self.assertRaises(ValueError):
                module.validate(manifest, '.')

    def test_valid_content_duplicate_anchor_and_execution_claim_guards(self):
        manifest = copy.deepcopy(self.manifest)
        case = manifest['cases'][0]
        content = case['source']['anchor'].encode()
        case['source']['sha256'] = hashlib.sha256(content).hexdigest()
        manifest['cases'] = [case]
        with patch.object(module.subprocess, 'run') as run:
            run.return_value.stdout = content
            self.assertEqual([case], module.validate(manifest, '.'))
            for change, message in [('duplicate', 'duplicate case'),
                                    ('anchor', 'anchor missing'),
                                    ('claim', 'cannot infer execution')]:
                changed = copy.deepcopy(manifest)
                if change == 'duplicate':
                    changed['cases'].append(copy.deepcopy(case))
                elif change == 'anchor':
                    changed['cases'][0]['source']['anchor'] = 'absent'
                else:
                    changed['cases'][0]['baseline']['native_terminal_receipt'] = 'invented'
                with self.subTest(change=change), self.assertRaisesRegex(ValueError, message):
                    module.validate(changed, '.')


if __name__ == '__main__':
    unittest.main()
