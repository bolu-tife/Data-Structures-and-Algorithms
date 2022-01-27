# Problem 1: Given a set of intervals, find out if any two intervals overlap.

# Example:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: true if theres overlapping
# false if there isn't any overlapping
# Explanation: Intervals [1,4] and [2,5] overlap


def if_overlapping(arr):
    if not arr:
        return True
  
    arr.sort(key = lambda x: x[0])
 
    end = arr[0][1]
    for i in range(1, len(arr)):
        curr = arr[i]
        if curr[0] <= end:
            return True
        end = curr[1]

    return False

print(if_overlapping([[1,4], [2,5], [7,9]]))
print(if_overlapping([[1,4], [4,9]]))
print(if_overlapping([[1,4], [7,9]]))
print(if_overlapping([[0,30], [5,10], [15,20]]))
print(if_overlapping([[7,10], [2,4]]))