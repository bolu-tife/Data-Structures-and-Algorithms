# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

# Normal approach - brute force O(n * k)
# edge cases 
# if k > len(arr): empty list
# if empty arr? empty list


# bruteforce approach
from msvcrt import kbhit


def find_averages_of_subarrays(K, arr):
  if K > len(arr) or len(arr) == 0 or K == 0:
    return []
  
  result = []

  for i in range(len(arr)-K+1):
    sum_so_far = 0

    for j in range(i,i+K):
      sum_so_far+= arr[j]

    result.append(sum_so_far/K)
  return result

#   Time complexity = O(n*k)
#   Space complexity = O(n)
# where n is the number of element in the array and k is k

def find_averages_of_subarray_sliding_window(arr, k):
    if k > len(arr):
        return []
    if k == 0 or len(arr) == 0:
        return []
    
    window_start = 0
    result = list()
    sum_so_far = 0

    for window_end in range(len(arr)):
        sum_so_far += arr[window_end]

        if window_end >= k-1:
            result.append(sum_so_far/k)
            sum_so_far -= arr[window_start]
            window_start+=1

    return result

#   Time complexity = O(n)
#   Space complexity = O(n)
# where n is the number of element in the array 

# followup return the maximum average subarray of size k, https://leetcode.com/problems/maximum-average-subarray-i/

def find_averages_of_subarray_sliding_window(arr, k):
    if k > len(arr):
        return []
    if k == 0 or len(arr) == 0:
        return []
    
    window_start = 0
    maximum_so_far = float('-inf')
    sum_so_far = 0

    for window_end in range(len(arr)):
        sum_so_far += arr[window_end]

        if window_end >= k-1:
            average = sum_so_far/k
            maximum_so_far = max(maximum_so_far, average)
            sum_so_far -= arr[window_start]
            window_start+=1

    return  maximum_so_far


#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of element in the array 