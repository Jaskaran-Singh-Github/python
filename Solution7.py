#Problem 7
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

    def find_second_last(self):
        if not self.head or not self.head.next:
            print("List has less than two elements.")
            return None

        current = self.head
        while current.next.next:  
            current = current.next

        print("Second last element is:", current.data)
        return current.data

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")
llist1 = LinkedList()
for i in [2, 4, 6, 8, 33, 67]:  
    llist1.append(i)

print("Linked List:")
llist1.print_list()
llist1.find_second_last()  

llist2 = LinkedList()
for i in [1, 2, 3, 4, 5]:  
    llist2.append(i)

print("\nLinked List:")
llist2.print_list()
llist2.find_second_last() 
