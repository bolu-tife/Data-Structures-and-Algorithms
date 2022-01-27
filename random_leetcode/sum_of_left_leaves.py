# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        return self.recurse(root)
    
    def recurse(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.recurse(root.right)
        else:
            return self.recurse(root.left) + self.recurse(root.right)
        