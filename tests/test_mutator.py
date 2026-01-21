import re
from src import mutator

def test_is_valid_dna_valid():
    assert mutator.is_valid_dna("ATGCATGC")
    assert mutator.is_valid_dna("atgc")

def test_is_valid_dna_invalid():
    assert not mutator.is_valid_dna("ATGB")
    assert not mutator.is_valid_dna("")
    assert not mutator.is_valid_dna(None)

def test_random_mutate_length_and_changes():
    seq = "AAAA"
    mutated, muts = mutator.random_mutate(seq, num_mutations=2, seed=42)
    assert len(mutated) == len(seq)
    assert len(muts) == 2
    for pos, orig, new in muts:
        assert orig == "A"
        assert new in mutator.VALID_BASES and new != orig

def test_mutate_with_probability_zero():
    seq = "ATGC"
    mutated, muts = mutator.mutate_with_probability(seq, prob=0.0, seed=1)
    assert mutated == seq.upper()
    assert muts == []

def test_mutate_with_probability_full():
    seq = "ATGC"
    mutated, muts = mutator.mutate_with_probability(seq, prob=1.0, seed=1)
    assert len(muts) == len(seq)
    assert re.fullmatch(f"[{mutator.VALID_BASES}]+", mutated)