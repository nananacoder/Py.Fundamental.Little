# def am_i_wilson(n):
#
#     import math
#     print math.factorial(n)
#     if n >0:
#         return (math.factorial(n-1)+1)%(n*n)==0
#     else:
#         return False
#
# num = input("please give a number:",)
# out = am_i_wilson(num)
# print out

#n!
def fac1(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)

def fac2(n):
    c = 1
    for i in range(1,n+1):
       c  *= i
    return c

def fac3(n):
    return reduce(lambda x,y: x*y, range(1,n+1)

num = input("please give a number:")
print fac2(num)