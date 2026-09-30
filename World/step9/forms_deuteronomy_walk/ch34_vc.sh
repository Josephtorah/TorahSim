for u in deu_34_moses_death; do python3 logic/solo_tools/verify_claims.py logic/oral_audit/manifests/${u}_claims.json || exit 1; done
