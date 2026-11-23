# loader.py: reads the CSV, sorts and dedupes the names, looks up a name's index (R1, R2, R3)

import csv


# R1: load the CSV file
def load_edges(filename):
    edges = []
    with open(filename, newline='', encoding='utf-8') as file:
        for start_from, to, heading, distance, speed in csv.reader(file):
            edges.append((start_from, to, heading, float(distance), float(speed)))
    return edges


# R2: get the vertex list (sorted, no duplicates)
def build_vertex_list(edges):
    names = []
    for start_from, to, _, _, _ in edges:
        names.append(start_from)
        names.append(to)
    n = len(names)
    for i in range(n):
        for j in range(n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
    vertices = []
    for name in names:
        if not vertices or name != vertices[-1]:
            vertices.append(name)
    return vertices


# R3: look up a building's index in the vertex list
def binary_search(vertices, target):
    low, high = 0, len(vertices) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if vertices[mid] == target:
            return mid
        if vertices[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1