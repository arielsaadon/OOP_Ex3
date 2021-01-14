import math


class NodeData:

    def __init__(self, key: int, tag: bool = False, pos: tuple = None):
        self.key = key
        self.tag = tag
        self.weight = math.inf
        self.location = pos

    def __str__(self):
        return f'{self.key}'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.weight < other.weight
