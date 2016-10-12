'''
Return the number (count) of vowels in the given string.

'''

def getCount(inputStr):
    num_vowels = sum([1 for i in inputStr if i in 'aeiou'])
    return num_vowels


def getCount2(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

def getCount3(s):
    return sum(c in 'aeiou' for c in s)

print getCount("o a kak ushakov lil vo kashu kakao") # return 13
print getCount("abracadabra") # return 5