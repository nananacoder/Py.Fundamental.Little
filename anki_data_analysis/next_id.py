# def next_id(arr):
#     if arr:
#         arr.sort()
#         if arr[0] != 0:
#             return 0
#         else:
#             for i in range(len(arr)-1):
#                 if (arr[i]-arr[i+1])<-1:
#                     return arr[i]+1
#             return arr[len(arr)-1]+1
#     else:
#         return 0

def next_id(arr):
    t = 0
    while t in arr:
        t +=1
    return t

list2 = input("please input a list:",)
print next_id(list2)