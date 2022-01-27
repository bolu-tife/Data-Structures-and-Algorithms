# https://leetcode.com/problems/merge-intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        merged = []
        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] <= end:
                end = max(end, current[1])
            else:
                merged.append([start, end])
                start = current[0]
                end = current[1]

        merged.append([start, end])

        return merged