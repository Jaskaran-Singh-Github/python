class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def insertBeforeMiddle(head, value):
    if head is None:
        return Node(value)
    
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    new_node = Node(value)

    if prev is None:
        new_node.next = head
        head = new_node
    else:
        prev.next = new_node
        new_node.next = slow

    return head

def printList(head):
    while head:
        print(head.data, end="->" if head.next else "\n")
        head = head.next
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head = insertBeforeMiddle(head, 9)
printList(head)
