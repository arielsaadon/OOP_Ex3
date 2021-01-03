class EdgeData:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __str__(self):
        return f'{self.src}{"-->"}{self.dest}'

    def __repr__(self):
        return self.__str__()
