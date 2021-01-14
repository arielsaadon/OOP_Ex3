from GraphInterface import GraphInterface
from NodeData import NodeData

"""This abstract class represents an implement of a graph."""


class DiGraph(GraphInterface):
    def __init__(self):
        self.__vertices = {}
        self.__neighbors_out = {}
        self.__neighbors_in = {}
        self.__edges_size = 0
        self.__mc = 0

    def v_size(self) -> int:
        """
        @return: The number of vertices in this graph
        """
        return len(self.__vertices)

    def e_size(self) -> int:
        """
        @return: The number of edges in this graph
        """
        return self.__edges_size

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__mc

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)
        """
        if self.__vertices is not None:
            return self.__vertices
        return {}

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        if self.__neighbors_in.get(id1) is not None:
            return self.__neighbors_in[id1]
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if self.__neighbors_out.get(id1) is not None:
            return self.__neighbors_out[id1]
        return {}

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 is not id2:
            if id1 in self.__vertices and id2 in self.__vertices:
                if id2 not in self.__neighbors_out[id1]:
                    self.__neighbors_in[id2][id1] = weight
                    self.__neighbors_out[id1][id2] = weight
                    self.__mc += 1
                    self.__edges_size += 1
                    return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if self.__vertices.get(node_id) is None:
            self.__vertices[node_id] = NodeData(node_id, pos)
            self.__neighbors_in[node_id] = {}
            self.__neighbors_out[node_id] = {}
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
        if node_id in self.__vertices:
            out_edge = self.all_out_edges_of_node(node_id).copy()
            if len(out_edge) > 0:
                for dest in out_edge:
                    del self.__neighbors_out[node_id][dest]
                    del self.__neighbors_in[dest][node_id]
                    self.__edges_size -= 1

            in_edge = self.all_in_edges_of_node(node_id).copy()
            if len(in_edge) > 0:
                for dest in in_edge:
                    del self.__neighbors_in[node_id][dest]
                    del self.__neighbors_out[dest][node_id]
                    self.__edges_size -= 1

            del self.__vertices[node_id]
            del self.__neighbors_in[node_id]
            del self.__neighbors_out[node_id]
            self.__mc += 1
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
            if node_id1 in self.__vertices and node_id2 in self.__vertices:
                if node_id2 in self.__neighbors_out[node_id1]:
                    del self.__neighbors_out[node_id1][node_id2]
                    del self.__neighbors_in[node_id2][node_id1]
                    self.__edges_size -= 1
                    self.__mc += 1
                    return True

        return False

    def __str__(self):
        s = f'|V|={self.v_size()} , |E|={self.__edges_size} , MC={self.__mc}\n'
        for key in self.__vertices.keys():
            s += f'{key}{"-->"}'
            if self.__neighbors_out.get(key) is not None:
                for neighbor, weight in self.__neighbors_out.get(key).items():
                    s += f'{neighbor}{[weight]} '
            s += '\n'
        return s

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.v_size() != other.v_size():
            return False
        if self.__edges_size != other.__edges_size:
            return False
        other_vertices = other.get_all_v()
        for key, value in self.__vertices.items():
            if key not in other_vertices:
                return False
            elif value.key is not other_vertices.get(key).key:
                return False
            else:
                for dest, weight in self.__neighbors_out.get(key).items():
                    if dest not in other.__neighbors_out.get(key):
                        return False
                    elif weight != other.__neighbors_out.get(key).get(dest):
                        return False
        return True
