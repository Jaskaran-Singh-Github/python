class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nodes_with_greater_right(head):
    def reverse(head):
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    head = reverse(head)
    max_val = head.val
    curr = head
    while curr and curr.next:
        if curr.next.val < max_val:
            curr.next = curr.next.next
        else:
            curr = curr.next
            max_val = curr.val
    return reverse(head)
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
head = list_to_linkedlist([5, 2, 13, 3, 8])
new_head = remove_nodes_with_greater_right(head)
print(linkedlist_to_list(new_head))  

head2 = list_to_linkedlist([1, 1, 1, 1])
new_head2 = remove_nodes_with_greater_right(head2)
print(linkedlist_to_list(new_head2))  
