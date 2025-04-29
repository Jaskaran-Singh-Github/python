class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def checkSubtreeSum(root, target_sum):
    found = [False]
    
    def subtreeSum(node):
        if node is None:
            return 0
        left_sum = subtreeSum(node.left)
        right_sum = subtreeSum(node.right)
        total = node.data + left_sum + right_sum
        if total == target_sum:
            found[0] = True
        
        return total
    
    subtreeSum(root)
    return found[0]
root = Node(1)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(5)
root.left.right = Node(9)
root.right.left = Node(8)
target_sum = 17
if checkSubtreeSum(root, target_sum):
    print("Yes")
else:
    print("No")
