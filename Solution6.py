#Problem 6
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

    @staticmethod
    def add_two_lists(l1, l2):
        l1.reverse()
        l2.reverse()

        result = LinkedList()
        carry = 0
        p1, p2 = l1.head, l2.head

        while p1 or p2 or carry:
            sum_value = carry
            if p1:
                sum_value += p1.data
                p1 = p1.next
            if p2:
                sum_value += p2.data
                p2 = p2.next

            carry, digit = divmod(sum_value, 10)
            result.append(digit)

        result.reverse()  
        return result

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")
l1 = LinkedList()
for i in [5, 6, 3]:  
    l1.append(i)

l2 = LinkedList()
for i in [8, 4, 2]:  
    l2.append(i)

print("List1:")
l1.print_list()
print("List2:")
l2.print_list()

result = LinkedList.add_two_lists(l1, l2)
print("Resultant List:")
result.print_list()  


l3 = LinkedList()
for i in [7, 5, 9, 4, 6]:  
    l3.append(i)

l4 = LinkedList()
for i in [8, 4]: 
    l4.append(i)

print("\nList1:")
l3.print_list()
print("List2:")
l4.print_list()

result2 = LinkedList.add_two_lists(l3, l4)
print("Resultant List:")
result2.print_list()  
