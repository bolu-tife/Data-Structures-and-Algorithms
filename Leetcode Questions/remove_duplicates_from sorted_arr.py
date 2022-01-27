# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
def removeDuplicates( nums):
    if not nums:
        return 0

    left = 0
    right = 1
    
    while right < len(nums):
        if nums[left] == nums[right]:
            right += 1
        else:
            nums[left+1] = nums[right]
            left += 1
            right += 1
    return left + 1

# another approah go through the loop and update nums[index] with the diffrent on (i != 1+i)
print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,2, 3,4]))