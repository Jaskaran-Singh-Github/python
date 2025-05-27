def pacificAtlantic(heights):
    if not heights:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited, prev_height):
        if (
            r < 0 or c < 0 or r >= rows or c >= cols
            or (r, c) in visited
            or heights[r][c] < prev_height
        ):
            return
        visited.add((r, c))
        # Explore 4 directions
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    # Start DFS from Pacific Ocean (top and left edges)
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])            # Left edge
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right edge
    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])            # Top edge
        dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom edge

    # Cells that can reach both oceans
    result = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacific and (r, c) in atlantic:
                result.append([r, c])
    return result
# heights = [
#   [1,2,2,3,5],
#   [3,2,3,4,4],
#   [2,4,5,3,1],
#   [6,7,1,4,5],
#   [5,1,1,2,4]
# ]
# heights=[[1]]
print(pacificAtlantic(heights))
# Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
