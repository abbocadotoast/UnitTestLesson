# swap/chunks.py
from itertools import batched

def pairs(names):
    """Split a class list into lab pairs; an odd student out works alone."""
    return [list(group) for group in batched(names, 2)]