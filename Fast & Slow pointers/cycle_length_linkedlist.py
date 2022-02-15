# Given the head of a LinkedList with a cycle, find the length of the cycle.

def cycle_length(head):
  # TODO: Write your code here
  if not head:
    return 0
  
  slow, fast = head, head
  count = 0

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
      slow = slow.next
      count += 1
      break

  while fast != slow:
    slow = slow.next
    count += 1
  
  return count

#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of nodes in the linkedlist 