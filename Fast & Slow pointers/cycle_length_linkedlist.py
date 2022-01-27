
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_length(head):
  if not head:
    return 0
  fast, slow = head, head
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



def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
