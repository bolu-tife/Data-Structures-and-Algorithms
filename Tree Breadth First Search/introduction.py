# Return a list of all elements in a tree following the bfs tree traversal


from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_breadth_first_search(root):
    if root is None:
        return []
    
    result = list()
    queue = deque()

    queue.append(root)

    while queue:
        current_node = queue.popleft()
        result.append(current_node.val)

        if current_node.left:
            queue.append(current_node.left)
        
        if current_node.right:
            queue.append(current_node.right)
        
    return result


# Time complexity: O(n), where n is the total number of nodes
# Space Complexity: O(n), where n is the total number of nodes