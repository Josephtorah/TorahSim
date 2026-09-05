#!/usr/bin/env python3
# =============================================================================
# lev_01_call_and_korban_opening — 1:1-3
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_01_call_and_korban_opening.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Opening of Leviticus: call-to-Moses, then first offering scope (1:1–3)"""
from machine import Machine

m = Machine("lev_01_call_and_korban_opening")

# -------------------------- Lev.1.1 · ETNACHTA_SPLIT -----------------------
# ‹ויקרא אל משה› (“and-call to Moses”)
# ‹… וידבר יהוה אליו› (“and-speak YHWH to-him/its”)
# ‹מאהל מועד לאמר› (“from-tent seasons to-say”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 1:1."
m.step("Lev.1.1")
# witness-tier presupposed read: kriyah_precedes_dibbur on call_protocol —
# read, not installed
m.witness_read("call_protocol", "kriyah_precedes_dibbur",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 1 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 1 6", "Sifra, Vayikra Dibbura DeNedavah, Chapter 1 7", "Sifra, Vayikra Dibbura DeNedavah, Chapter 1 10", "Sifra, Vayikra Dibbura DeNedavah, Chapter 1 11"])
# witness-grounded state (its own tier): bounded_single_receiver on voice
m.witness_state("voice", "bounded_single_receiver",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 2 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 2 9", "Sifra, Vayikra Dibbura DeNedavah, Chapter 2 10", "Sifra, Vayikra Dibbura DeNedavah, Chapter 2 12"])
# witness-tier presupposed read: reflection_pauses_chartered on
# paragraph_channel — read, not installed
m.witness_read("paragraph_channel", "reflection_pauses_chartered",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 1 8", "Sifra, Vayikra Dibbura DeNedavah, Chapter 1 9"])

# -------------------------- Lev.1.2 · ETNACHTA_SPLIT -----------------------
# ‹דבר אל בני› (“speak to son”)
# ‹ישראל ואמרת אלהם› (“Israel and-say to-them/their”)
# ‹אדם כי יקריב› (“human that bring-near”)
# ‹מכם קרבן ליהוה› (“from-you/your(pl) offering to-YHWH”)
# ‹… מן הבהמה מן› (“from the-livestock from”)
# ‹הבקר ומן הצאן› (“the-herd and-from the-flock”)
# ‹תקריבו את קרבנכם› (“bring-near obj-marker offering-you/your(pl)”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 1:2."
m.step("Lev.1.2")
# witness-tier presupposed read: covenant_keyed_optional on caller_domain —
# read, not installed
m.witness_read("caller_domain", "covenant_keyed_optional",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 2 3", "Sifra, Vayikra Dibbura DeNedavah, Section 2 4", "Sifra, Vayikra Dibbura DeNedavah, Section 2 5"])
# witness-tier presupposed read: domesticated_with_exclusions on
# input_filter — read, not installed
m.witness_read("input_filter", "domesticated_with_exclusions",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 2 6", "Sifra, Vayikra Dibbura DeNedavah, Section 2 7", "Sifra, Vayikra Dibbura DeNedavah, Section 2 9", "Sifra, Vayikra Dibbura DeNedavah, Section 2 10", "Sifra, Vayikra Dibbura DeNedavah, Section 2 11", "Sifra, Vayikra Dibbura DeNedavah, Chapter 3 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 3 4"])

# -------------------------- Lev.1.3 · COND_אם (“if”) -----------------------
# ‹אם עלה קרבנו› (“if burnt-offering offering-him/its”)
# ‹מן הבקר זכר› (“from the-herd male”)
# ‹תמים יקריבנו … אל› (“entire bring-near-him/its … to”)
# ‹פתח אהל מועד› (“opening tent seasons”)
# ‹יקריב אתו לרצנו› (“bring-near obj-marker-him/its to-delight-him/its”)
# ‹לפני יהוה› (“to-face YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 1:3."
m.step("Lev.1.3")
# witness-tier presupposed read: tamim_owner_coercion on acceptance_gate —
# read, not installed
m.witness_read("acceptance_gate", "tamim_owner_coercion",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 3 12", "Sifra, Vayikra Dibbura DeNedavah, Section 3 13", "Sifra, Vayikra Dibbura DeNedavah, Section 3 15", "Sifra, Vayikra Dibbura DeNedavah, Chapter 5 5", "Onkelos Lev 1:3"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted([])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 0
    assert sorted(m.WORLD["witnessed"]) == ['voice']
    assert m.WORLD["witnessed"]['voice']["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 2 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 2 9', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 2 10', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 2 12']
    assert all('bounded_single_receiver' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('call_protocol', 'kriyah_precedes_dibbur'), ('paragraph_channel', 'reflection_pauses_chartered'), ('caller_domain', 'covenant_keyed_optional'), ('input_filter', 'domesticated_with_exclusions'), ('acceptance_gate', 'tamim_owner_coercion')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 1 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 1 6', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 1 7', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 1 10', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 1 11']
    assert all('kriyah_precedes_dibbur' not in f for f in m.WORLD["facts"])
    assert 'call_protocol' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 1 8', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 1 9']
    assert all('reflection_pauses_chartered' not in f for f in m.WORLD["facts"])
    assert 'paragraph_channel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 2 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 2 4', 'Sifra, Vayikra Dibbura DeNedavah, Section 2 5']
    assert all('covenant_keyed_optional' not in f for f in m.WORLD["facts"])
    assert 'caller_domain' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 2 6', 'Sifra, Vayikra Dibbura DeNedavah, Section 2 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 2 9', 'Sifra, Vayikra Dibbura DeNedavah, Section 2 10', 'Sifra, Vayikra Dibbura DeNedavah, Section 2 11', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 3 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 3 4']
    assert all('domesticated_with_exclusions' not in f for f in m.WORLD["facts"])
    assert 'input_filter' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 3 12', 'Sifra, Vayikra Dibbura DeNedavah, Section 3 13', 'Sifra, Vayikra Dibbura DeNedavah, Section 3 15', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 5 5', 'Onkelos Lev 1:3']
    assert all('tamim_owner_coercion' not in f for f in m.WORLD["facts"])
    assert 'acceptance_gate' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
