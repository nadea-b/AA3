import time
import random
import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = weight

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.graph):
            current_vertex = min(
                (vertex for vertex in self.graph if vertex not in visited),
                key=lambda vertex: distances[vertex]
            )
            visited.add(current_vertex)

            for neighbor, weight in self.graph[current_vertex].items():
                distances[neighbor] = min(
                    distances[neighbor],
                    distances[current_vertex] + weight
                )

        return distances

    def floyd_warshall(self):
        vertices = list(self.graph.keys())
        n = len(vertices)
        dist = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
                elif vertices[j] in self.graph.get(vertices[i], {}):
                    dist[i][j] = self.graph[vertices[i]][vertices[j]]
                else:
                    dist[i][j] = float('inf')

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return {vertices[i]: {vertices[j]: dist[i][j] for j in range(n)} for i in range(n)}


def generate_random_weighted_graph(n):
    g = Graph()
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.5:
                weight = random.randint(1, 10)
                g.add_edge(i, j, weight)
                g.add_edge(j, i, weight)
    return g


def measure_execution_time(graph, algorithm, start=None):
    times = []
    for _ in range(100):
        start_time = time.time()
        if algorithm == 'dijkstra':
            graph.dijkstra(start)
        elif algorithm == 'floyd_warshall':
            graph.floyd_warshall()
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)


if __name__ == "__main__":
    graph_sizes = [1, 5, 10, 15, 20, 25, 30]
    dijkstra_times = []
    floyd_warshall_times = []

    for size in graph_sizes:
        random_graph = generate_random_weighted_graph(size)
        start_vertex = random.randint(0, size - 1)
        dijkstra_time = measure_execution_time(random_graph, 'dijkstra', start_vertex)
        floyd_warshall_time = measure_execution_time(random_graph, 'floyd_warshall')

        dijkstra_times.append(dijkstra_time)
        floyd_warshall_times.append(floyd_warshall_time)

    # Print the data in three rows
    print("Graph Sizes:", ', '.join([f"{size:8}" for size in graph_sizes]))
    print("Dijkstra times:", [format(time, '.5f') for time in dijkstra_times])
    print("Floyd-Warshall times:", [format(time, '.5f') for time in floyd_warshall_times])

    # Plot the comparison graph
    plt.plot(graph_sizes, dijkstra_times, label='Dijkstra', color='lightpink')
    plt.plot(graph_sizes, floyd_warshall_times, label='Floyd-Warshall', color='turquoise')
    plt.xlabel('Graph Size')
    plt.ylabel('Mean Execution Time (seconds)')
    plt.title('Mean Execution Time Comparison of Dijkstra and Floyd-Warshall')
    plt.legend()
    plt.show()
