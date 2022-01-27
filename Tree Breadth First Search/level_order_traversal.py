# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root):
        result = []
        
        if root is None:
            return result

        # queue = [root]
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = list()
            for i in range(level_size):
                current_node = queue.popleft() # Same thing as poping the first element 
                current_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            result.append(current_level)

        return result


# Time complexity: O(n), where n is the total number of nodes
# Space Complexity: O(n), where n is the total number of nodes