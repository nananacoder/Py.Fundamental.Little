'''
You are given two arrays a1 and a2 of strings.
Each string is composed with letters from a to z.
Let x be any string in the first array and y be any string in the second array.
'''



'''
If a1 or a2 are empty return -1 in each language except in Haskell where you will return Nothing.

Example:

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(s1, s2) --> 13
'''

def mxdiflg(a1, a2):
    s1_list = [len(i) for i in a1]
    s2_list = [len(i) for i in a2]
    maximum = []
    for i in s1_list:
        m = 0
        while m < len(s2_list):
            maxi = abs(i - s2_list[m])
            maximum.append(maxi)
            m += 1
    maximum.sort()
    return maximum[-1]


s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

print mxdiflg(s1, s2)
