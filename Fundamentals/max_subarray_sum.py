'''
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.


'''

# https://en.wikipedia.org/wiki/Maximum_subarray_problem
def maxSequence(arr):
    if arr:
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    else:
        return []


def maxSequence2(arr):
    maxx, curr = 0,0
    for i in arr:
        curr += i
        if curr < 0:
            curr = 0
        elif curr > maxx:
            maxx = curr
    return maxx

def maxSequence3(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
        return ans

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print maxSequence2(arr)