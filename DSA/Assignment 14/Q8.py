class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeZeroSumSublists(head):
    # Create a dummy node to handle cases where the head itself is part of a zero sum sublist
    dummy = ListNode(0)
    dummy.next = head

    # Use a dictionary to store the running sum and the corresponding node
    sum_dict = {}
    curr = dummy
    running_sum = 0

    while curr:
        running_sum += curr.val

        if running_sum in sum_dict:
            # Remove the nodes between the sum_dict[running_sum] and curr
            prev = sum_dict[running_sum]
            prev.next = curr.next
            while prev != curr:
                running_sum += prev.val
                del sum_dict[running_sum]
                prev = prev.next
        else:
            # Add the running_sum to the dictionary if it doesn't exist
            sum_dict[running_sum] = curr

        curr = curr.next

    return dummy.next


# Create the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

# Remove zero sum sublists
new_head = removeZeroSumSublists(head)
print(new_head)
