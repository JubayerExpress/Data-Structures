class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()

        def dfs_util(v):
            visited.add(v)
            print(v, end=' ')
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)

# Test cases
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS starting from vertex 2:")
g.dfs(2)  # Output: 2 0 1 3

