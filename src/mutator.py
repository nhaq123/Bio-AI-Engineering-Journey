"""
Simple mutation utilities for DNA sequences.

Functions:
- is_valid_dna(seq)
- random_mutate(seq, num_mutations=1, allowed_bases='ATGC', seed=None)
- mutate_with_probability(seq, prob=0.01, seed=None)

Lightweight starter you can expand (insertions, deletions, context-aware).
"""
from typing import List, Tuple, Optional
import random

VALID_BASES = "ATGC"

def is_valid_dna(seq: Optional[str]) -> bool:
    """Return True if seq contains only DNA bases (A, T, G, C) and is not None."""
    if seq is None:
        return False
    seq = seq.strip()
    if seq == "":
        return False
    return all(ch in VALID_BASES for ch in seq.upper())

def random_mutate(seq: str, num_mutations: int = 1, allowed_bases: str = VALID_BASES, seed: Optional[int] = None) -> Tuple[str, List[Tuple[int, str, str]]]:
    """
    Randomly perform `num_mutations` point substitutions on `seq`.
    Returns (mutated_sequence, mutations) where mutations is a list of (pos, from, to).
    Positions are 0-based. If num_mutations > len(seq), up to len(seq) distinct mutations are attempted.
    """
    if not is_valid_dna(seq):
        raise ValueError("Input sequence must contain only A/T/G/C characters and be non-empty.")
    if num_mutations <= 0:
        return seq.upper(), []

    rng = random.Random(seed)
    seq_list = list(seq.upper())
    length = len(seq_list)
    mutations: List[Tuple[int, str, str]] = []

    # choose distinct positions to avoid mutating the same position multiple times
    positions = list(range(length))
    rng.shuffle(positions)
    for pos in positions[:min(num_mutations, length)]:
        original = seq_list[pos]
        choices = [b for b in allowed_bases if b != original]
        new_base = rng.choice(choices)
        seq_list[pos] = new_base
        mutations.append((pos, original, new_base))

    return "".join(seq_list), mutations

def mutate_with_probability(seq: str, prob: float = 0.01, seed: Optional[int] = None) -> Tuple[str, List[Tuple[int, str, str]]]:
    """
    Mutate each base independently with probability `prob`.
    Returns (mutated_sequence, mutations) where mutations is a list of (pos, from, to).
    """
    if not (0 <= prob <= 1):
        raise ValueError("prob must be between 0 and 1.")
    if not is_valid_dna(seq):
        raise ValueError("Input sequence must contain only A/T/G/C characters and be non-empty.")

    rng = random.Random(seed)
    seq_list = list(seq.upper())
    mutations: List[Tuple[int, str, str]] = []
    for i, base in enumerate(seq_list):
        if rng.random() < prob:
            choices = [b for b in VALID_BASES if b != base]
            new_base = rng.choice(choices)
            seq_list[i] = new_base
            mutations.append((i, base, new_base))
    return "".join(seq_list), mutations


if __name__ == "__main__":
    # quick demo
    s = "ATGCTAGCTAGGCTA"
    mutated, muts = random_mutate(s, num_mutations=3, seed=1)
    print("original:", s)
    print("mutated :", mutated)
    print("mutations:", muts)