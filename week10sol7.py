class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def rotateLinkedList(head, k):
    if not head or not head.next or k == 0:
        return head
    
    length = 1  
    current = head
    while current.next:
        length += 1
        current = current.next
    
    k = k % length
    if k == 0:
        return head  
    current.next = head  
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head

def printList(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

# Create the linked list for TestCase 1
head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head1.next.next.next = Node(40)
head1.next.next.next.next = Node(50)
head1.next.next.next.next.next = Node(60)

print("Original List: ")
printList(head1)

# Rotate the list by 4
head1 = rotateLinkedList(head1, 4)

print("List after rotation by 4: ")
printList(head1)

# Create the linked list for TestCase 2
head2 = Node(30)
head2.next = Node(40)
head2.next.next = Node(50)
head2.next.next.next = Node(60)

print("\nOriginal List 2: ")
printList(head2)

# Rotate the list by 2
head2 = rotateLinkedList(head2, 2)

print("List after rotation by 2: ")
printList(head2)
