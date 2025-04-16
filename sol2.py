#Solution 2
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def maxTwinSum(head):
    slow,fast=head,head
    prev=None
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    while slow:
        temp=slow.next
        slow.next=prev
        prev=slow
        slow=temp    
    max_sum=0
    while prev:
        max_sum=max(max_sum,head.val+prev.val)
        head,prev=head.next,prev.next
    return max_sum
head1=ListNode(5,ListNode(4,ListNode(2,ListNode(1))))
print(maxTwinSum(head1))   
head1=ListNode(4,ListNode(2,ListNode(2,ListNode(3))))
print(maxTwinSum(head1))           