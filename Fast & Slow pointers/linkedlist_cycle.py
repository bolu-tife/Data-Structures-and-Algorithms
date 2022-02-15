# https://leetcode.com/problems/linked-list-cycle/
# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def has_cycle(head):
  # TODO: Write your code here
  if not head:
    return False
  
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
      return True
  
  return False

#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of nodes in the linkedlist 

# Using sets

def has_cycle_using_sets(head):
  # TODO: Write your code here
  if not head:
    return False
  
  seen = set()
  pointer = head

  while pointer:
    if pointer in seen:
      return True
    else:
      seen.add(pointer)
      pointer = pointer.next
  
  return False

#   Time complexity = O(n)
#   Space complexity = O(n)
# where n is the number of nodes in the linkedlist