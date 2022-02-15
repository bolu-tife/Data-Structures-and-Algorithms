# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.

# Using fast and slow pointer
def find_middle_of_linked_list(head):
  if not head:
    return None

  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  return slow


#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of nodes in the linkedlist 



# Brute force - calculating list size, then returning the middle node
def calculate_linked_list_size(head):
  count = 0
  curr = head
  while curr:
    count += 1
    curr = curr.next
  return count

def find_middle_of_linked_list(head):
  if not head:
    return None

  current = head
  count = calculate_linked_list_size(current)
  
  for i in range(count//2 ):
    current = current.next
  return current



#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of nodes in the linkedlist 