# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
# Example 2:

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
# or [1, 1, 6].


def smallest_subarray_with_given_sum(target, arr):
# You don't need to go throught this check if you can the read the data only once since the float(inf) takes care of it
  # if k == 0: 
  #   if min(arr) != 0:
  #     return 0
  #   else:
  #     return 1
  
  window_start = 0
  sum_so_far = 0
  minimum_size = float('inf')

  for window_end in range(len(arr)):
    sum_so_far += arr[window_end]

    while sum_so_far >= target and window_start <= window_end:
      minimum_size = min(window_end - window_start + 1, minimum_size)
      sum_so_far -= arr[window_start]
      window_start += 1

  return minimum_size if minimum_size != float('inf') else 0

# Note: This solution would not work when negative numbers are introduced

# Time Complexity: O(n) because the for loop runs atmost O(n + n) times
# Space Complexity: O(1) 
# n is the total size of the array