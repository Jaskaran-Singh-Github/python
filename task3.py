class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()  # Dummy node to store result
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        
        carry = total // 10  # Compute carry
        current.next = ListNode(total % 10)  # Store unit digit
        current = current.next  # Move forward

        # Move to next nodes if available
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy_head.next  # Return the head of the result list

# Example usage:
# Creating the input lists: l1 = [2,4,3], l2 = [5,6,4]
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# Creating the input lists: l1=[0].l2=[0]
# l1=ListNode(0)
# l2=ListNode(0)
# Creating the input lists: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9]
print("Output is:")
l1=ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l2=ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
# Adding two numbers
result = addTwoNumbers(l1, l2)

# Printing the output list
while result:
    print(result.val, end=" -> ")
    result = result.next
# Expected Output: 7 -> 0 -> 8
