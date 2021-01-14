import json
import math
import random
from queue import PriorityQueue

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
        """
        @return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
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
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.graph, default=lambda d: d.__dict__, indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        Example:
        # >>> from GraphAlgo import GraphAlgo
        # >>> g_algo = GraphAlgo()
        # >>> g_algo.addNode(0)
        # >>> g_algo.addNode(1)
        # >>> g_algo.addNode(2)
        # >>> g_algo.addEdge(0,1,1)
        # >>> g_algo.addEdge(1,2,4)
        # >>> g_algo.shortestPath(0,1)
        # (1, [0, 1])
        # >>> g_algo.shortestPath(0,2)
        # (5, [0, 1, 2])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        nodes_list = self.graph.get_all_v()
        distance_path = []

        if id1 is not id2 and nodes_list.get(id1) is not None and nodes_list.get(id2) is not None:
            distance_path = self.dijkstra(id1)
        if len(distance_path) == 0:
            return math.inf, []

        dest_node = nodes_list.get(id2)
        path = [dest_node.key]
        if dest_node is None:
            return math.inf, []

        while dest_node is not nodes_list.get(id1):
            next_node = distance_path.get(dest_node.key)
            if next_node is None:
                return math.inf, []
            path.append(next_node.key)
            dest_node = next_node

        path.reverse()
        distance = nodes_list.get(id2).weight
        return distance, path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        node_list = self.graph.get_all_v()
        neighbours = self.graph.all_out_edges_of_node(id1)

        if id1 not in node_list:
            return []
        if neighbours is {}:
            return [id1]

        ans = []
        list_out = self.bfs(id1, True)
        list_in = self.bfs(id1, False)

        for node in list_out:
            if node in list_in:
                ans.append(node)
        if len(ans) > 1:
            ans.sort()

        return ans

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        all_scc = []
        nodes_list = self.graph.get_all_v()
        nodes_temp = [x for x in nodes_list]

        while nodes_temp:
            scc = self.connected_component(nodes_temp[0])
            for node in scc:
                nodes_temp.remove(node)
            all_scc.append(scc)

        return all_scc

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner(with set_location() function).
        @return: Graph Visualization
        """
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

        title = "Graph Visualization(|V|=" + str(self.graph.v_size()) + " , |E|=" + str(self.graph.e_size()) + ")"
        plt.title(title, pad=10)
        plt.show()

    def dijkstra(self, src):
        node_list = self.graph.get_all_v()
        visited = {}
        vertex = {}
        queue = PriorityQueue()

        for node in node_list.values():
            node.weight = math.inf
            visited[node.key] = False
            vertex[node.key] = None

        node = node_list.get(src)
        queue.put(node)
        node.weight = 0

        while not queue.empty():
            node = queue.get()
            neighbours = self.graph.all_out_edges_of_node(node.key)
            for neighbour in neighbours:
                distance = node.weight + neighbours.get(neighbour)
                node_neighbour = node_list.get(neighbour)
                if not visited.get(neighbour) and node_neighbour.weight > distance:
                    vertex[node_neighbour.key] = node
                    node_neighbour.weight = distance
                    queue.put(node_neighbour)
            visited[node.key] = True
        return vertex

    def bfs(self, src: int, out: bool) -> list:
        nodes_list = self.graph.get_all_v()
        for node in nodes_list.values():
            node.tag = False

        queue = PriorityQueue()
        bfs_list = []
        queue.put(src)
        bfs_list.append(src)
        nodes_list.get(src).tag = True

        if out:
            while not queue.empty():
                node = queue.get()
                neighbours = self.graph.all_out_edges_of_node(node)
                for neighbour in neighbours:
                    node_neighbour = nodes_list.get(neighbour)
                    if node_neighbour.tag is False:
                        node_neighbour.tag = True
                        queue.put(node_neighbour.key)
                        bfs_list.append(node_neighbour.key)
        else:
            while not queue.empty():
                node = queue.get()
                neighbours = self.graph.all_in_edges_of_node(node)
                for neighbour in neighbours:
                    node_neighbour = nodes_list.get(neighbour)
                    if node_neighbour.tag is False:
                        node_neighbour.tag = True
                        queue.put(node_neighbour.key)
                        bfs_list.append(node_neighbour.key)

        return bfs_list

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
