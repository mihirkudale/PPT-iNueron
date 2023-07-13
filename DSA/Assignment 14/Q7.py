class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nextGreaterNodes(head):
    # Convert linked list to a list for easier traversal
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next

    n = len(values)
    stack = []
    answer = [0] * n

    for i in range(n):
        while stack and values[i] > values[stack[-1]]:
            idx = stack.pop()
            answer[idx] = values[i]
        stack.append(i)

    return answer


# Create the linked list
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)

# Find the next greater node for each node
answer = nextGreaterNodes(head)
