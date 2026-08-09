<a id="b3-app-a"></a>
# Appendix A — Canonical Object Contracts

Every canonical object implements the common envelope below. Domain schemas extend it without redefining identity or provenance.

| Field | Requirement |
|---|---|
| `object_id` | Stable institutional identity |
| `object_type` | Controlled semantic type |
| `schema_version` | Contract version used for validation |
| `content_version` | Revision or edition identity where applicable |
| `content_digest` | Digest of identified content, distinct from version |
| `created_at` | ISO 8601 timestamp with explicit offset |
| `created_by` | Authenticated human, agent, or service identity |
| `provenance` | Source or input object identities and transformation |
| `authority` | Knowledge class, producer, and review state |
| `validity` | Effective interval, expiry, or review date where applicable |
| `access_policy` | Purpose, resource, action, environment, time, and identity constraints |
| `retention_policy` | Retention, legal hold, deletion, and tombstone behavior |
| `supersession` | Prior and later object relationships |

Scientific objects add their required scope: claims add proposition and evidence relations; sources add edition and rights; experiments add specification and environment; decisions add authority and conditions; beliefs add uncertainty semantics and revision lineage.

Book X owns concrete serialization, APIs, migrations, and storage.
