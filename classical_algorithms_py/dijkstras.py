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

def dijkstras():
    pass