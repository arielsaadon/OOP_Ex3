import heapq
import json
import math
from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, di_graph: DiGraph = DiGraph()):
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
        nodes_list = self.graph.get_all_v()
        if id1 is not id2 and nodes_list.get(id1) is not None:
            self.dijkstra(id1)

        path = []
        dest_node = nodes_list.get(id2)
        distance_path = dest_node.weight

        while dest_node is not nodes_list.get(id1):
            if dest_node is None:
                return math.inf, []
            path.append(dest_node.key)
            dest_node = nodes_list.get(dest_node.father)

        path.append(dest_node)
        path.reverse()

        return distance_path, path

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    def dijkstra(self, src: int):
        nodes_list = self.graph.get_all_v()
        for node in nodes_list.values():
            node.tag = False
            node.weight = math.inf
            node.father = None
        start_node = nodes_list.get(src)
        start_node.weight = 0

        priority_queue = [node for node in nodes_list.values()]
        heapq.heapify(priority_queue)

        while len(priority_queue):
            node = heapq.heappop(priority_queue)
            neighbours = self.graph.all_out_edges_of_node(node.key)
            if neighbours is not None and node.tag is False:
                for neighbour in neighbours:
                    distance = node.weight + neighbour.weight
                    neighbour_node = nodes_list.get(neighbour.dest)
                    if distance < neighbour_node.weight:
                        neighbour_node.weight = distance
                        neighbour_node.father = node.key
                        heapq.heapify(priority_queue)

            node.tag = True
