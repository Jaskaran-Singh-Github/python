#Solution 1
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def insert_at_beginning(head,val):
    new_node=ListNode(val)
    new_node.next=head
    return new_node
def print_list(head):
    while head:
        print(head.val,end=" -> " if head.next else "\n")  
        head=head.next
head=ListNode(2,ListNode(3,ListNode(4,ListNode(5))))
new_head=insert_at_beginning(head,1)
print_list(new_head)        

head=ListNode(3,ListNode(2,ListNode(5,ListNode(7,ListNode(1,ListNode(2))))))
new_head=insert_at_beginning(head,9)
print_list(new_head)