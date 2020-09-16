import unittest

from exercise8 import min_cost_to_connect_nodes


class TestMinCostToConnectNodes(unittest.TestCase):
    def test_it_works(self):
        """
        There are 3 connected components [1, 4, 5], [2, 3] and [6]
        We can connect these components into a single component by connecting node 1 to node 2
        and node 1 to node 6 at a minimum cost of 5 + 2 = 7.
        """
        nodes = 6
        edges = [[1, 4], [4, 5], [2, 3]]
        new_edges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]

        result = min_cost_to_connect_nodes(nodes, edges, new_edges)

        self.assertEqual(result, 7)
