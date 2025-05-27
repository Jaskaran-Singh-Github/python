from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    # Step 1: Build graph and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Step 2: Collect nodes with 0 in-degree
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    count = 0

    # Step 3: BFS (Topological Sort)
    while queue:
        curr = queue.popleft()
        count += 1
        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: If we visited all courses, it's possible
    return count == numCourses
print(canFinish(2, [[1, 0]]))       # Output: True
print(canFinish(2, [[1, 0], [0, 1]]))  # Output: False
