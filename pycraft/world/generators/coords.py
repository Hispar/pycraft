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
        return round(self.x), round(self.y), round(self.z)

    def get_neighboring(self):
        """
        Retrieve adjacent coordinates
        :return:
        """
        neighboring = []
        x, y, z = self.get_as_tuple()
        for dx, dy, dz in FACES:
            neighboring.append((x + dx, y + dy, z + dz))
        return neighboring

    def __str__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)
