import heapq
import json
import math
import random

import matplotlib.pyplot as plt

from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        if graph is None:
            self.graph = DiGraph()
        else:
            self.graph = graph

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
                    if node.get('pos') is not None:
                        self.graph.add_node(node.get('id'), tuple(map(float, node.get('pos').split(','))))
                    else:
                        self.graph.add_node(node.get('id'))

                for edge in load_edges:
                    self.graph.add_edge(edge.get('src'), edge.get('dest'), edge.get('w'))

                # print(self.graph)
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
        fig, ax = plt.subplots()
        self.set_location()

        vertices = self.graph.get_all_v()
        for vertex in vertices.values():
            ax.scatter(vertex.location[0], vertex.location[1])
            # ax.annotate(vertex.key, (vertex.location[0] + 0.00005, vertex.location[1] + 0.00015))
            ax.annotate(vertex.key, xy=(vertex.location[0], vertex.location[1]), xycoords="data",
                        va="center", ha="center",
                        bbox=dict(boxstyle="circle", fc="w", pad=0.1))
            neighbours = self.graph.all_out_edges_of_node(vertex.key)
            for neighbour in neighbours:
                xy_a = (vertex.location[0], vertex.location[1])
                xy_b = (vertices.get(neighbour).location[0], vertices.get(neighbour).location[1])
                # plt.plot([xy_a[0], xy_b[0]], [xy_a[1], xy_b[1]], "->")
                ax.annotate("",
                            xy=(xy_a[0], xy_a[1]), xycoords='data',
                            xytext=(xy_b[0], xy_b[1]), textcoords='data',
                            arrowprops=dict(arrowstyle="<-",
                                            connectionstyle="arc3", shrinkA=6, shrinkB=6),
                            )

        plt.show()

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
            if len(neighbours) > 0 and node.tag is False:
                for neighbour in neighbours:
                    distance = node.weight + neighbours.get(neighbour)
                    neighbour_node = nodes_list.get(neighbour)
                    if distance < neighbour_node.weight:
                        neighbour_node.weight = distance
                        neighbour_node.father = node.key
                        heapq.heapify(priority_queue)

            node.tag = True

    def set_location(self) -> None:
        x_val = []
        y_val = []

        vertices = self.graph.get_all_v()
        for vertex in vertices.values():
            if vertex.location is not None:
                x_val.append(vertex.location[0])
                y_val.append(vertex.location[1])
        for vertex in vertices.values():
            if vertex.location is None and len(x_val) == 0 and len(y_val) == 0:
                rand_x = random.uniform(0, len(vertices))
                rand_y = random.uniform(0, len(vertices))
                vertex.location = (rand_x, rand_y, 0)
            elif vertex.location is None and len(x_val) > 0 and len(y_val) > 0:
                rand_x = random.uniform(min(x_val) - 0.0005, max(x_val) + 0.00005)
                rand_y = random.uniform(min(y_val) - 0.0005, max(y_val) + 0.00005)
                vertex.location = (rand_x, rand_y, 0)

    def __str__(self):
        return DiGraph.__str__(self.graph)
