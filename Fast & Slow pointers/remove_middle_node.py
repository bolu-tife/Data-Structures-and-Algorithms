# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

def deleteMiddle( head):
    if not head or not head.next:
        return None
    
    slow, fast = head, head
    
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    prev.next = slow.next
    
    return head


#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of nodes in the linkedlist 