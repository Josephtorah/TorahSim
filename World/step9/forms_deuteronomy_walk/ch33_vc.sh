for u in deu_33_ve_zot; do python3 logic/solo_tools/verify_claims.py logic/oral_audit/manifests/${u}_claims.json || exit 1; done
