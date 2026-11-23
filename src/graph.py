# graph.py: builds the adjacency list from the CSV lines (R4)
# Allison

from loader import binary_search


def build_adjacency_list(edges, V):
    # adj = one empty list per vertex
    adj = []
    for i in range(len(V)):
        adj.append([])

    # for each edge (u, v): add (v, heading, dist, speed) to adj[u]
    for from_name, to_name, heading, distance, speed in edges:
        u = binary_search(V, from_name)
        v = binary_search(V, to_name)
        adj[u].append((v, heading, distance, speed))

    return adj