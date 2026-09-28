for u in deu_29_moab_covenant deu_30_teshuvah_choice deu_31_charge_torah; do python3 logic/solo_tools/verify_claims.py logic/oral_audit/manifests/${u}_claims.json || exit 1; done
