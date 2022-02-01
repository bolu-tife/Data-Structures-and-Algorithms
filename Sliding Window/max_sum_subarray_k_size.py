# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

# questions
# answer for k when it is greater than the length - 0


# Approach: Brute Force:
def maximum_subarray_sum_brute(arr, k):
    max_so_far = 0
    for i in range(len(arr)-k + 1):
        sum_so_far = 0

        for j in range(i, i+k):
            sum_so_far += arr[j]
        max_so_far = max(max_so_far, sum_so_far)

    return max_so_far

# Time Complexity: O(n*k), where n is the length of the array and k is k
# space Complexity: O(1)



# Approach: Sliding Window Pattern
# keep track of sum and update maximum_sum and sum as we go

def find_maximum_sum_subarray_k_size(arr, k):
    if k == 0 or len(arr) == 0:
        return 0
    if k > len(arr):
        return 0
    
    window_start = 0
    sum_so_far = 0
    maximum_so_far = float('-inf')

    for window_end in range(len(arr)):
        sum_so_far += arr[window_end]

        if window_end >= k-1:
            maximum_so_far = max(maximum_so_far, sum_so_far)
            sum_so_far -= arr[window_start]
            window_start -=1

    return maximum_so_far

# Time Complexity: O(n), where n is the length of the array
# space Complexity: O(1)



# follow up return the array witht the maximum
def maximum_subarray_sum_follow_up(arr, k):
    if k == 0 or len(arr) == 0:
        return 0
    if k > len(arr):
        return 0

    max_so_far = float('inf') #since it's all positive numbers
    sum_so_far = 0
    window_start = 0
    max_start_index = 0

    for window_end in range(len(arr)):
        sum_so_far += arr[window_end]

        if window_end >= k -1:
            if max_so_far < sum_so_far:
                max_so_far = sum_so_far
                max_start_index = window_start

            sum_so_far -= arr[window_start]
            window_start += 1

    return arr[max_start_index: max_start_index+k]

# Time Complexity: O(n)
# space Complexity: O(n)
# where n is the length of the array