class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def leftShift(head, k):
    if not head or not head.next or k <= 0:
        return head

    # Find the (k+1)-th node
    curr = head
    for _ in range(k):
        if not curr.next:
            return head
        curr = curr.next

    # Save the new head
    new_head = curr.next

    # Traverse until the last node
    while curr.next:
        curr = curr.next

    # Connect the last node to the original head
    curr.next = head

    # Set the next pointer of the (k+1)-th node to None
    curr = new_head
    new_tail = head
    while curr.next:
        curr = curr.next
        new_tail = new_tail.next
    new_tail.next = None

    return new_head


# Create the linked list
head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(7)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(9)

# Left-shift the list by k=3 nodes
k = 3
new_head = leftShift(head, k)
