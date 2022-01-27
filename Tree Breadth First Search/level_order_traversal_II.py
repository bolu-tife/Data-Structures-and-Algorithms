# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]

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



# Approach one:
# insert the current level orders at the first position of the result 

# Time Complexity: O(n)^2 because of the way of insertion
# Space Complexity: O(n)
# where n is the number of nodes 

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if root is None:
            return result

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

            result.insert(0,current_level)

        return result


# Approach two:
# return reverse of the result when you follow the normal level order parttern
# check of the level_order_traversal.py in this directory

# Time Complexity: O(n) 
# Space Complexity: O(n)
# where n is the number of nodes 

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def reverser(arr):
            size = len(arr)
            for i in range(size//2):
                arr[i], arr[size - 1- i] = arr[size - 1- i], arr[i],
            
            return arr
        
        result = []
        
        if root is None:
            return result

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
        

        return reverser(result)