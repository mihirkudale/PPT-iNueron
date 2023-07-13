class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def addOne(head):
    if head is None:
        return head

    current = head
    lastNonNine = None

    while current:
        if current.data != 9:
            lastNonNine = current

        current = current.next

    if lastNonNine is None:
        newHead = Node(1)
        newHead.next = head
        head = newHead
    else:
        lastNonNine.data += 1
        current = lastNonNine.next

        while current:
            current.data = 0
            current = current.next

    return head


# Create the linked list: 4->5->6
head = Node(4)
head.next = Node(5)
head.next.next = Node(6)

result = addOne(head)
