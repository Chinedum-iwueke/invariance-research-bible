# RISK-004 completion evidence

Date: 2026-09-12

- Authoritative producer: `bt.institutional.candidate_admission.candidate_admission_receipt`
- Bulletproof source: `ecad17a36167845c7035b1302847b4455130e045`
- Bulletproof merge: PR #291, `24c25839bcc22178cee1c1bb06153bf1e12c06f8`
- Bulletproof tests: 28 focused; 1,458 full-suite passed; 28 declared skips; all CI gates passed
- Hermes source: `17ceffc`
- Hermes merge: PR #230, `9b1d68991dfec574769aa54b7ccbf43eddeb75b9`
- Hermes tests: 34 focused; 754 full backend; Ruff clean; all CI gates passed
- Migration: `d1a6b4e83c90`, single head and deployed on VM2
- VM2 image: `sha256:060e7cd322a923c168b5f30dca4ee446dd816a63aa84f8ea1447054844e445e6`, healthy
- Active schema: `2b4748c2-3052-4e3b-a706-e17698216324`
- Schema digest: `c3740311dcdd619a6b9e9fa2b1cebc3a4be3962beed52a9a9103997b1d424cc6`
- Automatic transition, allocation, capital, order and promotion authority: false

RISK-004 now makes admission, allocation, scaling, demotion and retirement separate,
digest-bound recommendations. Hermes requires one fresh exact RISK-004 receipt before
candidate promotion or capital qualification/allocation, then independently applies
GOV-003 authority and lifecycle rules. Deployment registered the boundary without
inventing a candidate decision; genuine candidate evidence will create the first
receipt.
