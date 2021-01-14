from GraphInterface import GraphInterface
from NodeData import NodeData

"""This abstract class represents an implement of a graph."""


class DiGraph(GraphInterface):

    def __init__(self):
        self.__nodes = dict()
        self.__in_edges = dict()
        self.__out_edges = dict()
        self.__mc = 0
        self.__edge_size = 0

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.__nodes:
            self.__nodes[node_id] = NodeData(node_id, pos)
            self.__in_edges[node_id] = {}
            self.__out_edges[node_id] = {}
            self.__mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self.__nodes:
            out_edge = self.all_out_edges_of_node(node_id).copy()
            if out_edge is not None:
                for dest in out_edge:
                    del self.__out_edges[node_id][dest]
                    self.__edge_size -= 1

            in_edge = self.all_in_edges_of_node(node_id).copy()
            if in_edge is not None:
                for dest in in_edge:
                    del self.__in_edges[node_id][dest]

            del self.__nodes[node_id]
            del self.__in_edges[node_id]
            del self.__out_edges[node_id]
            self.__mc += 1
            return True

        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        :param src:
        """
        if id1 is not id2:
            if id1 in self.__nodes and id2 in self.__nodes:
                if id2 not in self.__out_edges[id1]:
                    self.__out_edges[id1][id2] = weight
                    self.__in_edges[id2][id1] = weight
                    self.__mc += 1
                    self.__edge_size += 1
                    return True

            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 is not node_id2:
            if node_id1 in self.__nodes and node_id2 in self.__nodes:
                if node_id2 in self.__out_edges[node_id1]:
                    del self.__out_edges.get(node_id1)[node_id2]
                    del self.__in_edges.get(node_id2)[node_id1]
                    self.__edge_size -= 1
                    self.__mc += 1
                    return True

        return False

    def get_node(self, key: int) -> NodeData:
        return self.__nodes.get(key)

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)
        """
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        return self.__in_edges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.__out_edges.get(id1)

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.__nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__edge_size

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__mc

    def __str__(self):
        s = f'|V|={self.v_size()} , |E|={self.__edge_size} , MC={self.__mc}\n'
        for key in self.__nodes.keys():
            s += f'{key}{"-->"}'
            if self.__out_edges.get(key) is not None:
                for neighbor, weight in self.__out_edges.get(key).items():
                    s += f'{neighbor}{[weight]} '
            s += '\n'
        return s

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.v_size() != other.v_size():
            return False
        if self.__edge_size != other.__edge_size:
            return False
        other_vertices = other.get_all_v()
        for key, value in self.__nodes.items():
            if key not in other_vertices:
                return False
            elif value.key is not other_vertices.get(key).key:
                return False
            else:
                for dest, weight in self.__out_edges.get(key).items():
                    if dest not in other.__neighbors_out.get(key):
                        return False
                    elif weight != other.__neighbors_out.get(key).get(dest):
                        return False
        return True
