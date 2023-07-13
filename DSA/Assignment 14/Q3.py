class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.bottom = None


def mergeLists(a, b):
    if a is None:
        return b
    if b is None:
        return a

    result = None

    if a.data <= b.data:
        result = a
        result.bottom = mergeLists(a.bottom, b)
    else:
        result = b
        result.bottom = mergeLists(a, b.bottom)

    result.next = None
    return result


def flatten(head):
    if head is None or head.next is None:
        return head

    head.next = flatten(head.next)

    head = mergeLists(head, head.next)

    return head


# Create the linked list with sub-linked lists
head = Node(5)
head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

head.bottom = Node(7)
head.next.bottom = Node(20)
head.next.next.bottom = Node(22)
head.next.next.next.bottom = Node(35)

head.bottom.bottom = Node(8)
head.next.next.bottom.bottom = Node(50)

head.bottom.bottom.bottom = Node(30)
head.next.next.bottom.bottom.bottom = Node(45)

result = flatten(head)
print(result)
