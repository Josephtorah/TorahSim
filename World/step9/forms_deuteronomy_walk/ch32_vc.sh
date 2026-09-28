for u in deu_32_haazinu deu_32_song_aftermath; do python3 logic/solo_tools/verify_claims.py logic/oral_audit/manifests/${u}_claims.json || exit 1; done
