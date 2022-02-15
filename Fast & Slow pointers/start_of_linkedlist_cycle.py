# https://leetcode.com/problems/linked-list-cycle-ii/
# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
def start_of_ll_cycle(head):
    if head is None:
        return None

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            break

    if not fast or not fast.next:
     return None

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of nodes in the linkedlist 

# using sets
def find_start_cycle_using_sets(head):
    if not head:
        return head

    seen = set()
    pointer = head

    while pointer:
        if pointer in seen:
            return pointer
        seen.add(pointer)
        pointer = pointer.next
    
    return None


#   Time complexity = O(n)
#   Space complexity = O(n)
# where n is the number of nodes in the linkedlist 