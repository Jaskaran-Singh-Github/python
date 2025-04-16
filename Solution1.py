#Problem 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("The middle element is", slow.data)

llist1 = LinkedList()
for i in [2, 3, 4, 5]:  
    llist1.append(i)
llist1.find_middle()  

llist2 = LinkedList()
for i in [1, 2, 3, 4, 5]:  
    llist2.append(i)
llist2.find_middle()  
