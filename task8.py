def removeDuplicates(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove adjacent duplicate
        else:
            stack.append(char)  # Add character to stack

    return "".join(stack)  # Convert list to string

# Example usage:
print(removeDuplicates("abbaca"))  # Output: "ca"
print(removeDuplicates("azxxzy"))  # Output: "ay"
