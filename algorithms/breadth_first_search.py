# time: O(V+E). a function of the number of vertices and edges

# deques support pops and appends on either side with O(1)
from collections import deque
from xxlimited import new

from jmespath import search

# source: the grokking algorithms book
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']

# https://stackoverflow.com/a/8922151/4540866
graph2 = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}

# this version simply finds the node or returns -1
def bfs(graph, start_node="you", end_node="thom"):
    search_queue = deque()
    search_queue += graph[start_node]
    # must keep track of nodes already searched
    searched = set()
    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            searched.add(node)
            if node == end_node:
                return node
            else:
                if graph.get(node):
                    search_queue += graph[node]
    return -1

# this version finds the shortest path to the node
# instead of appending node to the queue, it appends the whole path
def bfs2(graph, start_node, end_node):
    search_queue = deque()
    searched = set()
    search_queue.append([start_node])
    while search_queue:
        path = search_queue.popleft()
        node = path[-1]
        if node == end_node:
            return path
        for adjacent in graph.get(node, []):
            if adjacent not in searched:
                new_path = path.copy()
                new_path.append(adjacent)
                search_queue.append(new_path)
        searched.add(node)

assert bfs(graph, "you", "thom") == "thom"
assert bfs2(graph, "you", "thom") == ["you", "claire", "thom"]
assert bfs2(graph2, "1", "11") == ["1", "4", "7", "11"]