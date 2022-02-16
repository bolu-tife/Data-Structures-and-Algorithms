# https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false



class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def reverse_linked_list(head):
  prev = None
  next_node = None
  current = head

  while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
  return prev

def middle_linked_list(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow

def is_palindromic_linked_list(head):
  if not head:
    return True

  middle_node = middle_linked_list(head)
  reverse_half = reverse_linked_list(middle_node)
  current = head

  while reverse_half and current:
    if current.value != reverse_half.value:
      return False
    current = current.next
    reverse_half = reverse_half.next

  return True


#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of nodes in the linkedlist 

# Another approach would be to put all elements in an array and check if the array is a palindrome