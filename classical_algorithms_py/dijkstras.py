import sys

"""
works on a "graph" that is implemented using python dicts, as shown below.
example_graph = { "a" : ["b","c"],
                  "b" : ["a", "d"],
                  "c" : ["a", "d"],
                  "d" : ["e"],
                  "e" : ["d"]
                }

diagram of example_graph:

    a --- b
    |     |
    |     |
    c --- d --- e
"""

"""
returns dict of node to a tuple containing the distance and the path
    node -> str: (distance -> int, path -> arr)
"""
def dijkstras(graph: dict, start_node: str) -> dict:
    unvisited_nodes = set()
    result = {}
    current_node = start_node
    first_iteration = True

    for key in graph:
        if key == start_node:
            result[key] = (0, [start_node])
        else:
            result[key] = (sys.maxsize, [start_node])
            unvisited_nodes.add(key)

    while len(unvisited_nodes) is not 0:
        if first_iteration:
            first_iteration = False
        else:
            current

        for neighbor in graph[current_node]:

        pass
