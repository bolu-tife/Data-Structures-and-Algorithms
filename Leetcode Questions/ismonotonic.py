# https://leetcode.com/problems/monotonic-array/submissions/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        increasing = True
        decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                decreasing = False
            if nums[i-1] > nums[i]:
                increasing = False
        return increasing or decreasing