from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Step 1: Initialize queue with all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    # If no fresh oranges, return 0
    if fresh == 0:
        return 0

    minutes = 0
    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    # Step 2: BFS
    while queue and fresh > 0:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If neighbor is fresh, rot it
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx, ny))
        minutes += 1

    # Step 3: Check if all fresh oranges are rotted
    return minutes if fresh == 0 else -1
grid1 = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid1))  # Output: 4

grid2 = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid2))  # Output: -1

grid3=[[0,2]]
print(orangesRotting(grid3)) # Output: 0