#Problem 5
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

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev  

    def add_one(self):
        self.reverse()
        current = self.head
        carry = 1

        while current:
            current.data += carry
            if current.data < 10:
                carry = 0  
                break
            else:
                current.data = 0  
                carry = 1

            if not current.next and carry:
                current.next = Node(1)  
                carry = 0
            current = current.next
        self.reverse()

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")
llist1 = LinkedList()
for i in [1, 9, 9, 9]: 
    llist1.append(i)
print("Original List:")
llist1.print_list()
llist1.add_one()
print("After Adding 1:")
llist1.print_list()  

llist2 = LinkedList()
for i in [3, 4, 5, 3]:  
    llist2.append(i)
print("\nOriginal List:")
llist2.print_list()
llist2.add_one()
print("After Adding 1:")
llist2.print_list()  
