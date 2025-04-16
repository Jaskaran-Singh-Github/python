#Problem 3
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

    def remove_duplicates(self):
        current = self.head

        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next  
            else:
                current = current.next 

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")

llist1 = LinkedList()
for i in [11, 11, 11, 13, 13, 20]:  
    llist1.append(i)
print("Original List:")
llist1.print_list()
llist1.remove_duplicates()
print("After Removing Duplicates:")
llist1.print_list() 

llist2 = LinkedList()
for i in [10, 15, 15, 15, 20, 20, 20, 23, 25, 25]:  
    llist2.append(i)
print("\nOriginal List:")
llist2.print_list()
llist2.remove_duplicates()
print("After Removing Duplicates:")
llist2.print_list()  
