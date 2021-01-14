class GeoLocation:

    def __init__(self, pos: tuple = None):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

    def distance(self, other):
        dx = (self.x - other.x)**2
        dy = (self.y - other.y)**2
        dz = (self.z - other.z)**2
        return (dx + dy + dz)**0.5


