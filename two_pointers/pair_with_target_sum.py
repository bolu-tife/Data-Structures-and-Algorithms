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
        pair = arr[start] + arr[end]
        if pair < target:
            start +=1
        elif pair > target:
            end -= 1
        else:
            return [start, end]

    return [-1, -1]


print(find_pair([1, 2, 3, 4, 6], target=6))
print(find_pair([2, 5, 9, 11], target=11))
print(find_pair([1,2,3,4], 15))
print(find_pair([1,2,3], 6))

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

print(hash_find_pair([1, 2, 3, 4, 6], target=6))
print(hash_find_pair([2, 5, 9, 11], target=11))
print(hash_find_pair([1,2,3,4], 15))
print(hash_find_pair([1,2,3], 6))