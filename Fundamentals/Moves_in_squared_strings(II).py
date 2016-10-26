"""
You are given a string of n lines, each substring being n characters long: For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study some transformations of this square of strings.

Clock rotation 180 degrees: rot
rot(s) => "ponm\nlkji\nhgfe\ndcba"
selfie_and_rot(s) (or selfieAndRot or selfie-and-rot) It is initial string + string obtained by clock rotation 180 degrees with dots interspersed in order (hopefully) to better show the rotation when printed.
s = "abcd\nefgh\nijkl\nmnop" -->
"abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"

Task:

Write these two functions rotand selfie_and_rot
and

high-order function oper(fct, s) where

fct is the function of one variable f to apply to the string s (fct will be one of rot, selfie_and_rot)
Examples:

s = "abcd\nefgh\nijkl\nmnop"
oper(rot, s) => "ponm\nlkji\nhgfe\ndcba"
oper(selfie_and_rot, s) => "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"

"""
# def rot(strng):
#     a = list(strng)
#     a.reverse()
#     return ''.join(a)
#
#
# def selfie_and_rot(strng):
#     length = len(strng.split()[0])
#     n1 = '.' * length + '\n'
#     n2 = '\n' + '.' * length
#     n3 = '.' * length + '\n' + '.' * length
#     s1 = strng.replace('\n', n1)
#     s2 = rot(strng).replace('\n', n2)
#     return s1 + n3 + s2
#
#
# def oper(fct, s):
#     if fct is rot:
#         return rot(s)
#     elif fct is selfie_and_rot:
#         return selfie_and_rot(s)
#     else:
#         pass
#

def rot(string):
    return string[::-1]

def selfie_and_rot(string):
    s_dot = '\n'.join([ s+'.'*len(s) for s in string.split('\n') ])
    return s_dot+'\n'+rot(s_dot)

def oper(fct, s):
    return fct(s)

#print rot("abcd\nefgh\nijkl\nmnop")
#selfie_and_rot("abcd\nefgh\nijkl\nmnop")