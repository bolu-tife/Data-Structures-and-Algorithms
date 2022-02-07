# Problem Statement#
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Example 1:

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11




def find_pair(arr, target):
    if not arr:
        return None
    start = 0
    end = len(arr)-1

    while start < end:
        pair_sum = arr[start] + arr[end]
        if pair_sum < target:
            start +=1
        elif pair_sum > target:
            end -= 1
        else:
            return [start, end]

    return [-1, -1]


assert find_pair([1, 2, 3, 4, 6], target=6 ) == [1,3]
assert find_pair([2, 5, 9, 11], target=11) == [0, 2]
assert find_pair([1,2,3,4], 15) == [-1,-1]
assert find_pair([1,2,3], 6) == [-1,-1]

#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of element in the array 



# Hash table approach
def hash_find_pair(arr, target):
    if not arr:
        return None
    seen = dict()

    for i in range(len(arr)):
        if target - arr[i] in seen:
            return [seen[target - arr[i]], i]
        else:
            seen[arr[i]] = i
    return [-1,-1]

assert hash_find_pair([1, 2, 3, 4, 6], target=6) == [1,3]
assert hash_find_pair([2, 5, 9, 11], target=11) == [0, 2]
assert hash_find_pair([1,2,3,4], 15) == [-1,-1]
assert hash_find_pair([1,2,3], 6) == [-1,-1]

#   Time complexity = O(n)
#   Space complexity = O(n)
# where n is the number of element in the array 


# using binary search
def binary_search(arr, num, start):
    # start = 0
    stop = len(arr)-1

    while start <= stop:
        mid = (start + stop)//2
        if num > arr[mid]:
            stop = mid-1
        elif num < arr[mid]:
            start = mid + 1
        else:
            return mid
    return None

def bin_search_find_pair(arr, target):
    for i in range(len(arr)):
        find_other_num = binary_search(arr, target-arr[i], i+1)
        
        if find_other_num:
            return [i, find_other_num]

    return [-1,-1]

assert bin_search_find_pair([1, 2, 3, 4, 6], target=6) == [1,3]
assert bin_search_find_pair([2, 5, 9, 11], target=11) == [0, 2]
assert bin_search_find_pair([1,2,3,4], 15) == [-1,-1]
assert bin_search_find_pair([1,2,3], 6) == [-1,-1]
assert bin_search_find_pair([1, 2, 3, 4, 6], target=10) == [3,4]

#   Time complexity = O(nlog(n)) because we perform a binary search(log(n)) on all elements
#   Space complexity = O(1)
# where n is the number of element in the array 


# using brute force
def brute_find_pair(arr, target):

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    
    return [-1,-1]
assert brute_find_pair([1, 2, 3, 4, 6], target=6) == [1,3]
assert brute_find_pair([2, 5, 9, 11], target=11) == [0, 2]
assert brute_find_pair([1,2,3,4], 15) == [-1,-1]
assert brute_find_pair([1,2,3], 6) == [-1,-1]
assert brute_find_pair([1, 2, 3, 4, 6], target=10) == [3,4]

#   Time complexity = O(n^2)
#   Space complexity = O(1)
# where n is the number of element in the array 