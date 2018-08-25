FACES = [
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]


class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_as_tuple(self):
        return round(self.x), round(self.z), round(self.y)

    def get_neighbours(self):
        """
        Retrieve adjacent coordinates
        :return:
        """
        neighbours = []
        x, y, z = self.get_as_tuple()
        for dx, dy, dz in FACES:
            neighbours.append((x + dx, z + dz, y + dy))
        return neighbours

    def get_floor(self):
        neighbours = []
        x, y, z = self.get_as_tuple()
        for dx, dy, dz in FACES:
            neighbours.append((x + dx, z, y + dy))
        return neighbours

    def __str__(self):
        return '(x:{}, y:{}, z:{})'.format(self.x, self.y, self.z)
