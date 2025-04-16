def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols  # Histogram heights
    max_area = 0

    def largestRectangleArea(heights):
        stack = []
        max_area = 0
        heights.append(0)  # Add sentinel to pop all elements

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Remove the sentinel
        return max_area

    for row in matrix:
        for j in range(cols):
            if row[j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0
        
        max_area = max(max_area, largestRectangleArea(heights))

    return max_area

# Example usage
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
# matrix = [["0"]]
# matrix = [["1"]]
print(maximalRectangle(matrix))  # Output: 6, 0 ,1
