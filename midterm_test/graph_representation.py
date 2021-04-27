from collections import defaultdict
from typing import Union


class Graph:
    """ Undirected graph data structure """

    def __init__(self, connections):
        self.graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self.graph[node1].add(node2)
        self.graph[node2].add(node1)

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self.graph and node2 in self.graph[node1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))


def transform_graph(source_graph_repr: Union[list, dict, 'Graph'],
                    representation: str) -> Union[dict, list, 'Graph']:
    if isinstance(source_graph_repr, list):
        vertices = []
        for n, i in enumerate(source_graph_repr):
            for m, j in enumerate(i):
                if j:
                    edge = sorted((n, m))
                    if edge not in vertices:
                        vertices.append(edge)
        class_graph = Graph(vertices)
    elif isinstance(source_graph_repr, dict):
        vertices = []
        for i in source_graph_repr:
            for j in source_graph_repr[i]:
                edge = sorted((i, j))
                if edge not in vertices:
                    vertices.append(edge)
        class_graph = Graph(vertices)
    elif isinstance(source_graph_repr, Graph):
        class_graph = source_graph_repr

    if representation == 'matrix':
        matrix_graph = []
        for v in class_graph.graph.values():
            adjacent = [0] * len(class_graph.graph)
            for i in v:
                adjacent[i] = 1
            matrix_graph.append(adjacent)

        return matrix_graph
    elif representation == 'adjacency':
        return dict(class_graph.graph)
    elif representation == 'class':
        return class_graph


# Пример для проверки - один и тот же граф в разных представлениях
matrix_graph = [[0, 1, 1, 0, 0, 0],
                [1, 0, 0, 1, 1, 0],
                [1, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 1, 0]]

adjacency_list_graph = {0: [1, 2],
                        1: [0, 3, 4],
                        2: [0, 5],
                        3: [1],
                        4: [1, 5],
                        5: [2, 4]}

vertices = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (4, 5)]
class_graph = Graph(vertices)

print(transform_graph(matrix_graph, 'class'))
