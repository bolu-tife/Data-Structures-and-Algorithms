# https://leetcode.com/problems/remove-element/

def remove_duplicates_follow_up_2(arr, key):
    next_element = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element +=1
    return next_element

assert remove_duplicates_follow_up_2([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4
assert remove_duplicates_follow_up_2([2, 11, 2, 2, 1], 2) == 2

#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of element in the array 