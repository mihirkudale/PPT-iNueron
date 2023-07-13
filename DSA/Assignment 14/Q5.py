class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    if not head or not head.next:
        return head

    oddDummy = ListNode()
    evenDummy = ListNode()
    odd = oddDummy
    even = evenDummy
    isOdd = True

    while head:
        if isOdd:
            odd.next = head
            odd = odd.next
        else:
            even.next = head
            even = even.next

        isOdd = not isOdd
        head = head.next

    odd.next = evenDummy.next
    even.next = None

    return oddDummy.next


# Create the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Group the nodes into odd and even positions
new_head = oddEvenList(head)
print(new_head)
