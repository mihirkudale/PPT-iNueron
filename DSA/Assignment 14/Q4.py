class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None
        self.random = None


def copyRandomList(head):
    if not head:
        return None

    # Create a mapping between original nodes and new nodes
    mapping = {}

    # Create new nodes with corresponding values
    current = head
    while current:
        new_node = Node(current.val)
        mapping[current] = new_node
        current = current.next

    # Set next and random pointers of new nodes
    current = head
    while current:
        new_node = mapping[current]
        new_node.next = mapping.get(current.next)
        new_node.random = mapping.get(current.random)
        current = current.next

    return mapping[head]


# Create the original linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Set the random pointers
head.random = head.next
head.next.random = head.next.next.next

# Create a deep copy of the linked list
new_head = copyRandomList(head)
print(new_head)
