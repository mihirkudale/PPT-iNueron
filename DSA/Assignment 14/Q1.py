class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def detectAndRemoveLoop(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if fast is None or fast.next is None:
        return head

    slow = head
    prev_slow = None

    while slow != fast:
        prev_slow = slow
        slow = slow.next
        fast = fast.next

    prev_slow.next = None

    return head


# Create the linked list: 1->3->4->3
head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = head.next

result = detectAndRemoveLoop(head)
