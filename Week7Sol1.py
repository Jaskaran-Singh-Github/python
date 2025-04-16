class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, le: int, right: int) -> ListNode:
    if not head or le == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node before the 'le' position
    for _ in range(le - 1):
        prev = prev.next

    # Start reversing the sublist
    curr = prev.next
    next_node = None
    for _ in range(right - le):
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example Usage
# head = create_linked_list([1, 2, 3, 4, 5])
head=create_linked_list([5])
le, right = 1, 1
new_head = reverseBetween(head, le, right)
print(linked_list_to_list(new_head))  # Output: [1, 4, 3, 2, 5] , [5]
