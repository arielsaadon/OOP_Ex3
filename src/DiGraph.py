from GraphInterface import GraphInterface
from NodeData import NodeData


class DiGraph(GraphInterface):
    def __init__(self):
        self.__vertices = {}
        self.__neighbors_out = {}
        self.__neighbors_in = {}
        self.__edges_size = 0
        self.__mc = 0

    def v_size(self) -> int:
        return len(self.__vertices)

    def e_size(self) -> int:
        return self.__edges_size

    def get_mc(self) -> int:
        return self.__mc

    def get_all_v(self) -> dict:
        if self.__vertices is not None:
            return self.__vertices
        return {}

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.__neighbors_in.get(id1) is not None:
            return self.__neighbors_in[id1]
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.__neighbors_out.get(id1) is not None:
            return self.__neighbors_out[id1]
        return {}

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
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
        if self.__vertices.get(node_id) is None:
            self.__vertices[node_id] = NodeData(node_id, pos)
            self.__neighbors_in[node_id] = {}
            self.__neighbors_out[node_id] = {}
            self.__mc += 1
            return True

        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.__vertices:
            out_edge = self.all_out_edges_of_node(node_id).copy()
            if len(out_edge) > 0:
                for dest in out_edge:
                    # self.remove_edge(node_id, dest)
                    del self.__neighbors_out[node_id][dest]
                    del self.__neighbors_in[dest][node_id]
                    self.__edges_size -= 1
                    self.__mc += 1

            in_edge = self.all_in_edges_of_node(node_id).copy()
            if len(in_edge) > 0:
                for dest in in_edge:
                    # self.remove_edge(dest, node_id)
                    del self.__neighbors_in[node_id][dest]
                    del self.__neighbors_out[dest][node_id]
                    self.__edges_size -= 1
                    self.__mc += 1

            del self.__vertices[node_id]
            del self.__neighbors_in[node_id]
            del self.__neighbors_out[node_id]
            self.__mc += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
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
