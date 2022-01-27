# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

# questions
# answer for k when it is greater than the length - 0


# Approach brute force:
def maximum_subarray_sum_brute(arr, k):
    max_sum = 0
    for i in range(len(arr)-k + 1):
        curr_sum = 0

        for j in range(i, i+k):
            curr_sum += arr[j]
        max_sum = max(max_sum, curr_sum)

    return max_sum


print(maximum_subarray_sum_brute([2, 1, 5, 1, 3, 2], k=3 ))

print(maximum_subarray_sum_brute([2, 3, 4, 1, 5], k=2 ))

# Approach:
# use sliding window pattern
# keep track of sum and update maximum sum as we go


def maximum_subarray_sum(arr, k):
    if k > len(arr):
        return 0
    max_sum = 0 #since it's all positive numbers
    curr_sum = 0
    start = 0
    for i in range(len(arr)):
        curr_sum += arr[i]

        if i >= k -1:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[start]
            start += 1
    return max_sum

print(maximum_subarray_sum([2, 1, 5, 1, 3, 2], k=3 ))

print(maximum_subarray_sum([2, 3, 4, 1, 5], k=2 ))

# follow up return the array witht the maximum
def maximum_subarray_sum_follow_up(arr, k):
    if k > len(arr):
        return 0
    max_sum = 0 #since it's all positive numbers
    curr_sum = 0
    start = 0
    max_start = 0
    for i in range(len(arr)):
        curr_sum += arr[i]

        if i >= k -1:
            if max_sum < curr_sum:
                max_sum = curr_sum
                max_start = start
            curr_sum -= arr[start]
            start += 1
    return arr[max_start: max_start+k]

print(maximum_subarray_sum_follow_up([2, 1, 5, 1, 3, 2], k=3 ))

print(maximum_subarray_sum_follow_up([2, 3, 4, 1, 5], k=2 ))