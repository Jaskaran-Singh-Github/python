class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head  # Start from the head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # Remove duplicate
        else:
            current = current.next  # Move to next node

    return head  # Return modified list

# Example Usage:
# Creating linked list: [1,1,2]
head = ListNode(1, ListNode(1, ListNode(2)))
head=ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3)))))

# Removing duplicates
result = deleteDuplicates(head)

# Printing the output list
while result:
    print(result.val, end=" -> ")
    result = result.next
# Expected Output: 1 -> 2
