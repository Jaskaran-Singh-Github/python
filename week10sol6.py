class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def deleteLastOccurrence(head, item):
    if head is None:
        return None
    
    last_occurrence = None
    current = head
    prev = None

    while current:
        if current.data == item:
            last_occurrence = prev
        prev = current
        current = current.next

    if last_occurrence is None:
        return head  
    
    if last_occurrence is None:
        head = head.next
        return head
    last_occurrence.next = last_occurrence.next.next
    
    return head

def printList(head):
    current = head
    while current:
        print(current.data, end=" --> " if current.next else "\n")
        current = current.next

# Create the linked list for TestCase 1
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(4)
head1.next.next.next.next.next.next = Node(4)

print("Created Linked List 1: ")
printList(head1)

# Delete the last occurrence of 4
head1 = deleteLastOccurrence(head1, 4)

print("List after deletion of 4: ")
printList(head1)

# Create the linked list for TestCase 2
head2 = Node(11)
head2.next = Node(32)
head2.next.next = Node(123)
head2.next.next.next = Node(344)
head2.next.next.next.next = Node(445)
head2.next.next.next.next.next = Node(484)
head2.next.next.next.next.next.next = Node(534)

print("\nCreated Linked List 2: ")
printList(head2)

# Delete the last occurrence of 445
head2 = deleteLastOccurrence(head2, 445)

print("List after deletion of 445: ")
printList(head2)
