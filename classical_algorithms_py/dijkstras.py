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

    for key in graph:
        unvisited_nodes.add(key)
        if key == start_node:
            result[key] = (0, [])
        else:
            result[key] = (sys.maxsize, [])

    while len(unvisited_nodes) is not 0:
        current_node
        pass
