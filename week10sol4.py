class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def isLeaf(node):
    return node is not None and node.left is None and node.right is None

def isSumTree(node):
    if node is None:
        return True
    if isLeaf(node):
        return True
    if isSumTree(node.left) and isSumTree(node.right):
        if node.left is None:
            left_sum = 0
        elif isLeaf(node.left):
            left_sum = node.left.data
        else:
            left_sum = 2 * node.left.data
        if node.right is None:
            right_sum = 0
        elif isLeaf(node.right):
            right_sum = node.right.data
        else:
            right_sum = 2 * node.right.data
        return (node.data == left_sum + right_sum)

    return False
root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)
if isSumTree(root):
    print("The given tree is a SumTree")
else:
    print("The given tree is NOT a SumTree")
