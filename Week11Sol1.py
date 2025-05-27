from typing import List

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val)
        self.visited[node] = clone_node

        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node

# Helper: Build graph from adjacency list
def build_graph(adj_list: List[List[int]]) -> Node:
    if not adj_list:
        return None

    nodes = [Node(i + 1) for i in range(len(adj_list))]

    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]

    return nodes[0]

# Helper: Convert graph to adjacency list for comparison
def graph_to_adj_list(node: 'Node') -> List[List[int]]:
    from collections import deque, defaultdict

    if not node:
        return []

    adj = defaultdict(list)
    visited = set()
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        if curr.val in visited:
            continue
        visited.add(curr.val)
        for neighbor in curr.neighbors:
            adj[curr.val].append(neighbor.val)
            if neighbor.val not in visited:
                queue.append(neighbor)

    return [sorted(adj[i]) for i in range(1, len(adj) + 1)]

# ---------- Test Case ----------

if __name__ == "__main__":
    adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original_node = build_graph(adj_list)

    solution = Solution()
    cloned_node = solution.cloneGraph(original_node)

    cloned_adj_list = graph_to_adj_list(cloned_node)
    print("Cloned Graph Adjacency List:", cloned_adj_list)
