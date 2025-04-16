class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = even  # Store the head of the even list

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head  # Attach even list to the end of odd list

    return head

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
head=create_linked_list([2,1,3,5,6,4,7])
new_head = oddEvenList(head)
print(linked_list_to_list(new_head))  # Output: [1, 3, 5, 2, 4]  [2,3,6,7,1,5,4]
