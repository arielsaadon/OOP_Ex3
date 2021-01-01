class EdgeData:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __str__(self):
        return f'{self.dest}'
