from GraphInterface import GraphInterface
from NodeData import NodeData
from EdgeData import EdgeData


class DiGraph(GraphInterface):
    def __init__(self):
        self.__vertices = {}
        self.__neighbors_out = {}
        self.__neighbors_in = {}
        self.__node_size = 0
        self.__edges_size = 0
        self.__mc = 0

    def v_size(self) -> int:
        return self.__node_size

    def e_size(self) -> int:
        return self.__edges_size

    def get_mc(self) -> int:
        return self.__mc

    def get_all_v(self) -> dict:
        if self.__vertices is not None:
            return self.__vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.__neighbors_in.get(id1) is not None:
            return self.__neighbors_in[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.__neighbors_out.get(id1) is not None:
            return self.__neighbors_out[id1]

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.__vertices.get(id1) is not None:
            if self.__neighbors_out.get(id1) is not None:
                for edge in self.__neighbors_out.get(id1):
                    if edge.src is id1 and edge.dest is id2:
                        self.remove_edge(id1, id2)
                        self.__neighbors_out.setdefault(id1, []).append(EdgeData(id1, id2, weight))
                        self.__neighbors_in.setdefault(id2, []).append(EdgeData(id1, id2, weight))
                        self.__edges_size += 1
                        self.__mc += 1
                        return True

            self.__neighbors_out.setdefault(id1, []).append(EdgeData(id1, id2, weight))
            self.__neighbors_in.setdefault(id2, []).append(EdgeData(id1, id2, weight))
            self.__edges_size += 1
            self.__mc += 1
            return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.__vertices.get(node_id) is None:
            self.__vertices[node_id] = NodeData(node_id, pos)
            self.__node_size += 1
            self.__mc += 1
            return True

        return False

    def remove_node(self, node_id: int) -> bool:
        if self.__vertices.get(node_id) is not None:
            out_edges = self.all_out_edges_of_node(node_id)
            for edge in out_edges:
                self.remove_edge(edge.src, edge.dest)

            in_edges = self.all_in_edges_of_node(node_id)
            for edge in in_edges:
                self.remove_edge(edge.src, edge.dest)

            del self.__vertices[node_id]
            self.__node_size -= 1
            self.__mc += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.__vertices[node_id1] is not None:
            if self.__neighbors_out.get(node_id1) is not None:
                for edge in self.__neighbors_out.get(node_id1):
                    if edge.src is node_id1 and edge.dest is node_id2:
                        self.__neighbors_out[node_id1].remove(edge)
                for edge in self.__neighbors_in.get(node_id2):
                    if edge.src is node_id1 and edge.dest is node_id2:
                        self.__neighbors_in[node_id2].remove(edge)
                        self.__edges_size -= 1
                        self.__mc += 1
                        return True

        return False

    def __str__(self):
        s = f'|V|={self.__node_size} , |E|={self.__edges_size} , MC={self.__mc}\n'
        for key in self.__vertices.keys():
            s += f'{key}{"-->"}'
            if self.__neighbors_out.get(key) is not None:
                for neighbor in self.__neighbors_out.get(key):
                    s += f'{neighbor.dest}{[neighbor.weight] } '
            s += '\n'
        return s

    def __repr__(self):
        return self.__str__()
