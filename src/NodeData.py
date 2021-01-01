class NodeData:
    def __init__(self, key: int, pos: tuple = None, weight: int = -1, tag: int = -1, info: str = ""):
        self.key = key
        self.tag = tag
        self.info = info
        self.weight = weight
        self.location = pos

    def __str__(self):
        return f'key:{self.key}'

