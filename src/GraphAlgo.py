import json
from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, di_graph: DiGraph):
        self.graph = di_graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        load_nodes = {}
        load_edges = {}
        try:
            with open(file_name, "r") as file:
                load_json = json.load(file)
                for key, value in load_json.items():
                    if key == 'Nodes':
                        load_nodes = value
                    if key == 'Edges':
                        load_edges = value

                for node in load_nodes:
                    self.graph.add_node(node.get('id'), node.get('pos'))

                for edge in load_edges:
                    self.graph.add_edge(edge.get('src'), edge.get('dest'), edge.get('w'))

                #print(self.graph)
                return True

        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                json.dump(self.graph, default=lambda d: d.__dict__, indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
