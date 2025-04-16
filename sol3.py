#Solution 3
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def mergeTwoLists(l1,l2):
    dummy=ListNode()
    tail=dummy
    while l1 and l2:
        if l1.val<l2.val:
            tail.next,l1=l1,l1.next
        else:
            tail.next,l2=l2,l2.next
        tail=tail.next
    tail.next=l1 or l2
    return dummy.next
def print_list(head):
    while head:
        print(head.val,end=" -> " if head.next else "\n")  
        head=head.next    
l1=ListNode(1,ListNode(2,ListNode(4)))   
l2=ListNode(1,ListNode(3,ListNode(4)))       
merged_head=mergeTwoLists(l1,l2)         
print_list(merged_head)      