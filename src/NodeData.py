import math


class NodeData:
    def __init__(self, key: int, pos: tuple = None, tag: bool = False, father: int = None):
        self.key = key
        self.tag = tag
        self.father = father
        self.weight = math.inf
        self.location = pos

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f'{self.key}'

    def __repr__(self):
        return self.__str__()
