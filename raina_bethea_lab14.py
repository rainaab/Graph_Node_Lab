class UndirectedGraph:
    def __init__(self):
        self.adj_list = {}
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if u in self.adj_list:
            self.adj_list[u].append(v)
        if v not in self.adj_list:
            self.adj_list[v] = []
        if v in self.adj_list:
            self.adj_list[v].append(u)

    def node_exists(self, u):
        if u in self.adj_list:
            return u in self.adj_list
        else:
            return False
    def edge_exists(self,u,v):
        if u in self.adj_list and v in self.adj_list[u]:
            return True
        else:
            return False
    def get_neighbors(self, u):
        return self.adj_list[u]

    def get_edge_density(self):
        n = len(self.adj_list)
        num = 0
        for neighbor in self.adj_list.values():
            num = num + len(neighbor)
        edges = num // 2
        total = (n * (n-1)) // 2
        density = edges/total
        return round(density, 2)

    def is_complete(self):
        if self.get_edge_density() == 1.0:
            return True
        else:
            return False


graph = UndirectedGraph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print(graph.node_exists(1))
print(graph.node_exists(10))
print(graph.edge_exists(1,2))
print(graph.edge_exists(1,3))
print(graph.get_neighbors(1))
print(graph.get_edge_density())
print(graph.is_complete())
# print(graph.adj_list)