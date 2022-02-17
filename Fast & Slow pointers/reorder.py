# https://leetcode.com/problems/reorder-list/
# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def middle_linked_list(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  return slow

def reverse_linked_list(head):
  prev = None
  curr = head

  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

  return prev

def reorder(head):
  if not head or not head.next:
    return head

  current = head
  middle_node = middle_linked_list(current)
  reverse_half = reverse_linked_list(middle_node)

  current = head
  while reverse_half.next :
    current_next = current.next
    reverse_half_next = reverse_half.next
    reverse_half.next = current_next
    current.next = reverse_half

    current = current_next
    reverse_half = reverse_half_next
  
  return head


#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of nodes in the linkedlist 
