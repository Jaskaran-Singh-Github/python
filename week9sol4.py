def hasOnlyOneChild(preorder):
    n = len(preorder)

    for i in range(n - 1):
        next_diff = preorder[i] - preorder[i + 1]
        last_diff = preorder[i] - preorder[-1]
        if next_diff * last_diff < 0:
            return "No"

    return "Yes"
# Test case 1
preorder = [20, 10, 11, 13, 12]
print("Output:", hasOnlyOneChild(preorder))  # Output: Yes
#Test case 2
preorder= [15, 30, 25, 18, 20]
print("Output:",hasOnlyOneChild(preorder)) # Output: yes
