from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    
    # Define a counter to avoid tuple comparison issues in Python
    count = 0

    # Insert the head of each list into the heap
    for l in lists:
        if l:
            heappush(heap, (l.val, count, l))
            count += 1  # Ensure uniqueness in heap

    dummy_head = ListNode()
    current = dummy_head

    while heap:
        val, _, node = heappop(heap)  # Get the smallest element
        current.next = node  # Append to the merged list
        current = current.next

        if node.next:  # Insert the next element from the same list
            heappush(heap, (node.next.val, count, node.next))
            count += 1

    return dummy_head.next

# Example usage:
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
# lists=[]
# lists=[[]]
# Merging k sorted linked lists
result = mergeKLists(lists)

# Printing the output list
while result:
    print(result.val, end=" -> ")
    result = result.next
# Expected Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
