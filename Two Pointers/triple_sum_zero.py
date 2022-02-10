# https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []


def triple_sum_zero(nums):
    if len(nums) < 3:
        return []

    nums.sort()
    answer = list()

    for index, num in enumerate(nums):
        left = index+1
        right = len(nums)-1

        if nums[index] == nums[index-1] and index > 0:
            continue
        
        else:
            while left < right:
                total = num + nums[left] + nums[right]

                if total == 0:
                    answer.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left-1] and left < right:
                        left+=1

                    while nums[right] == nums[right+1] and left < right:
                        right-=1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
    
    return answer

# print(triple_sum_zero([-3, 0, 1, 2, -1, 1, -2]))
# print(triple_sum_zero([-5, 2, -1, -2, 3]))
# print(triple_sum_zero([-1,0,1,2,-1,-4]))
print(triple_sum_zero([0,0,0]))