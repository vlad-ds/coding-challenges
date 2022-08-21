# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/
# Works on undirected, connected, weighted graphs

# PriorityQueue: a queue where elements are sorted
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        # originally self.v
        self.num_of_vertices = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = set()
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
        
def dijkstra(graph: Graph, start_vertex: int):
    paths = {v: float("inf") for v in range(graph.num_of_vertices)}
    paths[start_vertex] = 0
    pq = PriorityQueue()
    # First value is shortest path, second value is vertex
    pq.put((0, start_vertex))
    while not pq.empty():
        _, current_vertex = pq.get()
        graph.visited.add(current_vertex)
        for neighbor in range(graph.num_of_vertices):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = paths[neighbor]
                    new_cost = paths[current_vertex] + distance
                    if new_cost < old_cost:
                        # add the lower cost node to the priority queue
                        pq.put((new_cost, neighbor))
                        paths[neighbor] = new_cost
    return paths
        
g = Graph(9)

edges = [
    (0, 1, 4),
    (0, 6, 7),
    (1, 6, 11),
    (1, 7, 20),
    (1, 2, 9),
    (2, 3, 6),
    (2, 4, 2),
    (3, 4, 10),
    (3, 5, 5),
    (4, 5, 15),
    (4, 7, 1),
    (4, 8, 5),
    (5, 8, 12),
    (6, 7, 1),
    (7, 8, 3),
]

for edge in edges:
    g.add_edge(*edge)
    
print(dijkstra(g, 0))