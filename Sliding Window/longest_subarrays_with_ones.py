# https://leetcode.com/problems/max-consecutive-ones-iii/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


def longest_subarray_with_ones(arr, k):
    window_start = 0
    window_sum = 0
    longest = float('-inf')

    for window_end, num in enumerate(arr):
        window_sum += num


        if window_end-window_start+1 - window_sum > k:
            window_sum -= arr[window_start]
            window_start += 1
            

        longest = max(longest, window_end-window_start+1)

    return longest

assert longest_subarray_with_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6
assert longest_subarray_with_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9
assert longest_subarray_with_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 0) == 2

# Time Complexity: O(n)
# Space Complexity: O(1) 
# n is the total size of the array

