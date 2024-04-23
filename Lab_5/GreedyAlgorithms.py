import random
import time
import matplotlib.pyplot as plt
import heapq


class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if vertex != self.parent[vertex]:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(graph):
    start_time = time.time()

    # Initialize an empty list to store the edges of the minimum spanning tree
    mst = []

    # Get all the vertices in the graph
    vertices = list(graph.keys())

    # Initialize a UnionFind data structure with the vertices
    uf = UnionFind(vertices)

    # Create a list to store the edges
    edges = []

    # Iterate through the graph to extract edges
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((weight, u, v))

    # Sort the edges by weight
    edges.sort()

    # Iterate through the sorted edges
    for weight, u, v in edges:
        # If adding the edge (u, v) does not form a cycle in the MST, add it to the MST
        if uf.find(u) != uf.find(v):
            mst.append((u, v, weight))
            uf.union(u, v)

    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


class Prim:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = list(graph.keys())
        self.visited = set()
        self.min_heap = []

    def prim_algorithm(self):
        start_time = time.time()
        self.visited.add(self.vertices[0])  # Start from the first vertex
        self.update_heap(self.vertices[0])
        mst = []

        while self.min_heap:
            weight, u, v = heapq.heappop(self.min_heap)
            if v not in self.visited:
                self.visited.add(v)
                mst.append((u, v, weight))
                self.update_heap(v)

        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time

    def update_heap(self, vertex):
        for neighbor, weight in self.graph[vertex].items():
            if neighbor not in self.visited:
                heapq.heappush(self.min_heap, (weight, vertex, neighbor))


def generate_random_graph(n):
    graph = {}
    for i in range(n):
        graph[i] = {}
        for j in range(i + 1, n):
            if random.random() < 0.5:
                weight = random.randint(1, 10)  # Adjust weight range as needed
                graph[i][j] = weight
                if j not in graph:
                    graph[j] = {}
                graph[j][i] = weight
    return graph


# Array containing the numbers of nodes
node_numbers = [250, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000]

kruskal_times = []
prim_times = []

for num_nodes in node_numbers:
    # Generate a random graph with the specified number of nodes
    random_graph = generate_random_graph(num_nodes)

    # Measure the time taken for Kruskal's algorithm
    kruskal_times.append(kruskal(random_graph))
    print("Time taken to find MST using Kruskal's algorithm for", num_nodes, "nodes:", kruskal_times[-1], "seconds")

    # Measure the time taken for Prim's algorithm
    prim = Prim(random_graph)
    prim_times.append(prim.prim_algorithm())
    print("Time taken to find MST using Prim's algorithm for", num_nodes, "nodes:", prim_times[-1], "seconds")

# Plotting the times
plt.plot(node_numbers, kruskal_times, marker='o', label="Kruskal's Algorithm", color='turquoise')
plt.plot(node_numbers, prim_times, marker='o', label="Prim's Algorithm", color='orange')
plt.title('Time taken to find MST for different numbers of nodes')
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()
