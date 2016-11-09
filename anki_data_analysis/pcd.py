# def relatively_prime(n, l):
#     def gcd(a, b):
#         if a < b:
#             a, b = b, a
#         while b != 0:
#             temp = a % b
#             a = b
#             b = temp
#         return a
#
#     output = []
#     for i in l:
#         if gcd(n,i) == 1:
#             output.append(i)
#     return output


# def relatively_prime (n, l):
#     from fractions import gcd
#     output = []
#     for i in l:
#         if gcd(n,i) == 1:
#             output.append(i)
#     return output


from fractions import gcd

def relatively_prime(n,l):
    return [x for x in l if gcd(n, x) == 1]

n=input("input num1:",)
l=input("input list1:",)
print relatively_prime(n,l)
