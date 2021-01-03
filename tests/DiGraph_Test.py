import unittest

from DiGraph import DiGraph


class DiGraphTest(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()
        for n in range(6):
            self.graph.add_node(n)

    def test_v_size(self):
        graph = DiGraph()
        graph.add_node(0)
        self.assertEqual(graph.v_size(), 1, 'add one node')
        graph.add_node(0)
        self.assertEqual(graph.v_size(), 1, 'add same node')
        graph.add_node(12)
        self.assertEqual(graph.v_size(), 2)
        graph.remove_node(0)
        self.assertEqual(graph.v_size(), 1)

    def test_e_size(self):
        self.graph.add_edge(0, 1, 4)
        self.assertEqual(self.graph.e_size(), 1, 'add one edge')
        self.graph.add_edge(0, 1, 1.3)
        self.assertEqual(self.graph.e_size(), 1, 'add same edge')
        self.graph.add_edge(1, 2, 2.8)
        self.assertEqual(self.graph.e_size(), 2)
        self.graph.add_edge(2, 3, 8)
        self.graph.remove_edge(1, 2)
        self.assertEqual(self.graph.e_size(), 2, 'add one and after remove one')

    def test_get_all_v(self):
        dict_vertices = self.graph.get_all_v()
        for n in dict_vertices:
            self.assertEqual(dict_vertices[n].key, n)
            self.assertIsNotNone(dict_vertices[n])
        self.graph.remove_node(3)
        for n in dict_vertices:
            self.assertEqual(dict_vertices[n].key, n)
            self.assertIsNotNone(dict_vertices[n])

    def test_all_in_edges_of_node(self):
        self.graph.add_edge(0, 2, 13)
        self.assertIsNotNone(self.graph.all_in_edges_of_node(2), 'add one edge')
        self.graph.remove_edge(0, 2)
        self.assertIsNone(self.graph.all_in_edges_of_node(2), 'after remove edge')

        self.assertIsNone(self.graph.all_in_edges_of_node(6), 'node is not in graph')

    def test_all_out_edges_of_node(self):
        self.graph.add_edge(2, 5, 13)
        self.graph.add_edge(2, 3, 1.3)
        self.graph.add_edge(4, 2, 1)
        self.assertIsNotNone(self.graph.all_out_edges_of_node(2))
        self.assertIsNotNone(self.graph.all_out_edges_of_node(4))
        self.graph.remove_edge(2, 5)
        self.assertIsNotNone(self.graph.all_out_edges_of_node(2), 'remove only one edge')
        self.assertIsNotNone(self.graph.all_out_edges_of_node(4))
        self.graph.remove_edge(2, 3)
        self.graph.remove_edge(4, 2)
        self.assertIsNone(self.graph.all_in_edges_of_node(2), 'after remove all edges')
        self.assertIsNone(self.graph.all_in_edges_of_node(4), 'after remove all edges')

        self.assertIsNone(self.graph.all_out_edges_of_node(-1), 'node is not in graph')

    def test_add_edge(self):
        self.assertFalse(self.graph.add_edge(7, 3, 11), 'node is not in graph')
        self.assertFalse(self.graph.add_edge(3, 7, 11), 'node is not in graph')
        self.assertTrue(self.graph.add_edge(3, 2, 11), 'add edge 3,2')
        self.assertTrue(self.graph.add_edge(3, 2, 12), 'change weight')
        self.assertFalse(self.graph.add_edge(2, 2, 12), 'impossible to create a edge from vertex to himself')

    def test_add_node(self):
        graph = DiGraph()
        self.assertTrue(graph.add_node(5))
        self.assertFalse(graph.add_node(5), 'node is exists')
        dict_vertices = graph.get_all_v()
        for n in dict_vertices:
            self.assertEqual(dict_vertices[n].key, 5)

    def test_remove_node(self):
        self.assertEqual(self.graph.v_size(), 6)
        self.assertFalse(self.graph.remove_node(7), 'node is not in graph')
        self.assertTrue(self.graph.remove_node(5))
        self.assertEqual(self.graph.v_size(), 5, 'remove one node')
        self.graph.add_edge(0, 1, 9)
        self.assertEqual(self.graph.e_size(), 1, 'add one edge')
        self.assertTrue(self.graph.remove_node(0), 'remove one node')
        self.assertEqual(self.graph.v_size(), 4)
        self.assertEqual(self.graph.e_size(), 0, 'after remove a node, the edge is also removed')
        self.graph.add_edge(1, 2, 4)
        self.graph.add_edge(2, 1, 9)
        self.graph.add_edge(3, 1, 25)
        self.assertEqual(self.graph.e_size(), 3, 'add three edges')
        self.assertTrue(self.graph.remove_node(1), 'remove one node')
        self.assertEqual(self.graph.v_size(), 3)
        self.assertEqual(self.graph.e_size(), 0, 'after remove a node, the edges is also removed')

    def test_remove_edge(self):
        self.assertFalse(self.graph.remove_edge(6, 4), '6 not in graph')
        self.assertFalse(self.graph.remove_edge(3, 7), '7 not in graph')
        self.assertFalse(self.graph.remove_edge(7, 8), '7 and 8 not in graph')
        self.assertFalse(self.graph.remove_edge(2, 3), 'not have a edge')
        self.graph.add_edge(0, 1, 7)
        self.assertEqual(self.graph.e_size(), 1)
        self.assertTrue(self.graph.remove_edge(0, 1))
        self.assertEqual(self.graph.e_size(), 0)


if __name__ == '__main__':
    unittest.main()
