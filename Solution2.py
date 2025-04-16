#Problem 2
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

    def delete_middle(self):
        if not self.head or not self.head.next:

            self.head = None
            return

        slow = fast = self.head
        prev = None 

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")
llist1 = LinkedList()
for i in [1, 2, 3, 4, 5]:  
    llist1.append(i)
print("Original List:")
llist1.print_list()
llist1.delete_middle()
print("After Deleting Middle:")
llist1.print_list() 

llist2 = LinkedList()
for i in [1, 2, 3, 4, 5, 6]:  
    llist2.append(i)
print("\nOriginal List:")
llist2.print_list()
llist2.delete_middle()
print("After Deleting Middle:")
llist2.print_list() 
