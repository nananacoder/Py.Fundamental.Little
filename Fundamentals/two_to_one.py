'''
Take 2 strings s1 and s2 including only letters from a to z.
Return a new sorted string, the longest possible,
containing distinct letters, - each taken only once - coming from s1 or s2.

Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

'''

def longest(s1, s2):
    from itertools import groupby
    a = [k for (k,_) in groupby(s1 + s2)]
    b = list(set(a))
    b.sort()
    return ''.join(b)


def longest_2(a1, a2):
    return "".join(sorted(set(a1 + a2)))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print longest_2(a,b)
