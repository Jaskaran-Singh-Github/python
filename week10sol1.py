class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def maxDepth(root):
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)

# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# root.left.left.left = Node(8)
# root.left.left.right = Node(9)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

# Find maximum depth
print("Maximum depth of tree is", maxDepth(root))
