import time
import random
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited.add(v)

        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            v = queue.pop(0)

            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

def generate_random_graph(n):
    g = Graph()
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < 0.5:  # Adjust the probability for edge creation
                g.add_edge(i, j)
                g.add_edge(j, i)
    return g

def measure_execution_time(graph, algorithm):
    times = []
    for _ in range(5):  # Perform 5 executions and calculate mean time
        start_time = time.time()
        if algorithm == 'dfs':
            graph.dfs(0)  # Start DFS from vertex 0
        elif algorithm == 'bfs':
            graph.bfs(0)  # Start BFS from vertex 0
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)  # Mean execution time

if __name__ == "__main__":
    graph_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900]  # Sizes of the graphs to be generated
    dfs_times = []
    bfs_times = []

    for size in graph_sizes:
        random_graph = generate_random_graph(size)

        dfs_time = measure_execution_time(random_graph, 'dfs')
        bfs_time = measure_execution_time(random_graph, 'bfs')

        dfs_times.append(dfs_time)
        bfs_times.append(bfs_time)

    # Print the data in three rows
    print("Graph Sizes:", ', '.join([f"{size:8}" for size in graph_sizes]))
    print("DFS times:", [format(time, '.5f') for time in dfs_times])
    print("BFS times:", [format(time, '.5f') for time in bfs_times])

    # Plot the comparison graph
    plt.plot(graph_sizes, dfs_times, label='DFS')
    plt.plot(graph_sizes, bfs_times, label='BFS')
    plt.xlabel('Graph Size')
    plt.ylabel('Mean Execution Time (seconds)')
    plt.title('Mean Execution Time Comparison of DFS and BFS')
    plt.legend()
    plt.show()
