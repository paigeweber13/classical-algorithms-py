import unittest

from classical_algorithms_py import dijkstras


class DijkstrasTest(unittest.TestCase):
    def setUp(self) -> None:
        self.typical_graph = {"a": ["b", "c"],
                              "b": ["a", "d"],
                              "c": ["a", "d"],
                              "d": ["e"],
                              "e": ["d"],
                              }

        self.small_graph = {"a": []}

        self.complex_graph = {"a": ["b", "d", "e", "j"],
                              "b": ["a", "c", "h"],
                              "c": ["b", "e", "f"],
                              "d": ["a", "e", "g"],
                              "e": ["a", "c", "d", "i"],
                              "f": ["c"],
                              "g": ["d"],
                              "h": ["e", "b"],
                              "i": ["e", "j"],
                              "j": ["a", "i"],
                              }

    def test_typical_graph(self) -> None:
        result = {}
        expected = {
            "a": (0, ['a']),
            "b": (1, ['a', 'b']),
            "c": (1, ['a', 'c']),
            "d": (2, ['a', 'b', 'd']),
            "e": (3, ['a', 'b', 'd', 'e']),
        }
        result = dijkstras.dijkstras(self.typical_graph, 'a')
        self.assertEqual(result, expected)

    def test_graph_with_single_node(self):
        result = {}
        expected = {
            "a": (0, ['a']),
        }
        result = dijkstras.dijkstras(self.typical_graph, 'a')
        self.assertEqual(result, expected)

    def test_complex_graph(self):
        result = {}
        expected = {
            "a": (0, ['a']),
            "b": (1, ['a', 'b']),
            "c": (2, ['a', 'b', 'c']),
            "d": (1, ['a', 'd']),
            "e": (1, ['a', 'e']),
            "f": (3, ['a', 'b', 'c', 'f']),
            "g": (2, ['a', 'd', 'g']),
            "h": (2, ['a', 'b', 'h']),
            "i": (2, ['a', 'e', 'i']),
            "j": (1, ['a', 'j']),
        }
        result = dijkstras.dijkstras(self.typical_graph, 'a')
        self.assertEqual(result, expected)
