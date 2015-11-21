from itertools import izip_longest
#
#
# def interleave(a, b):
#     """Return the interleaving of two sequences as a list."""
#     return [y for x in izip_longest(a, b) for y in x if y is not None]

def interleave(a, b):
    return [y for x in izip_longest(a, b) for y in x]
