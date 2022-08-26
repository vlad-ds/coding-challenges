# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/
# Works on undirected, connected, weighted graphs

# PriorityQueue: a queue where elements are sorted
# When adding tuples to a PQ, the first element determines the sorting 
# In this case we add tuples (distance, node) to the PQ
# So when we get from PQ, we know we're always getting the closest node
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        # originally self.v
        self.num_of_vertices = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
        
def dijkstra(graph: Graph, start_vertex):
    paths = {v: float("inf") for v in range(graph.num_of_vertices)}
    paths[start_vertex] = 0
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start_vertex))
    while not pq.empty():
        current_cost, current_node = pq.get()
        visited.add(current_node)
        for neighbor in range(graph.num_of_vertices):
            distance = graph.edges[current_node][neighbor]
            if distance != -1 and neighbor not in visited:
                old_cost = paths[neighbor]
                new_cost = current_cost + distance 
                if new_cost < old_cost:
                    paths[neighbor] = new_cost
                    pq.put((new_cost, neighbor))
    return paths
        
g = Graph(9)

# (source, target, weight)
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

assert dijkstra(g, 0) == {0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11}