
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs_shortest_path(self, start, goal):
        visited = set()
        queue = deque([[start]])

        if start == goal:
            return [start]

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node not in visited:
                neighbors = self.graph.get(node, [])
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    if neighbor == goal:
                        return new_path
                visited.add(node)

        return None

# Test cases
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Shortest path from 2 to 3:", g.bfs_shortest_path(2, 3))  # Output: [2, 3]


 


