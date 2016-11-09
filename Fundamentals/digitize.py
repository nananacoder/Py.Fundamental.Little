'''

Convert number to reversed array of digits

Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.
Example:

348597 => [7,9,5,8,4,3]

'''

def digitize(n):

    '''
    by myself
    '''

    x = list(str(n))
    x.reverse()
    a = []
    for i in range(len(x)):
        a.append(int(x[i]))
    return a


def digitize2(n):
    # use map function
    map(int, str(n)[::-1])

#or
def digitize22(n):
    return map(int, reversed(str(n)))


# digitize2 equals :
def digitize3(n):
    return [int(x) for x in str(n)[::-1]]


#or
def digitize4(n):
    return [int(x) for x in reversed(str(n))]


#another method
def digitize5(n):
    result = []
    while n >= 1:
        result.append(n%10)
        n //= 10 # n = n//10
    return result
