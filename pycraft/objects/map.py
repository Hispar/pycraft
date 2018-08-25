from operator import add, sub

from pycraft.world.generators.coords import Coord
from pycraft.world.validator import Validator


class Map:
    def __init__(self, strata_map):
        self.strata = strata_map
        self.validator = None

    def get_block(self, coords):
        if isinstance(coords, tuple):
            coords = Coord(*coords)
        return self.strata[coords.x][coords.z][coords.y]

    def get_strata(self):
        return self.strata

    def get_surface_blocks(self, limit, coords):
        """
        Get elements in surface of the map, in a limited area
        :param limit:
        :param coords:
        :return:
        """
        low_limit = coords[0] - limit if (coords[0] - limit) > 0 else 0
        upper_limit = coords[0] + limit
        # Validator receives a limited area of the strata map
        self.validator = Validator(self.strata[low_limit:upper_limit])

        pos = Coord(*coords)
        if not self.validator.is_air(pos):
            print('not air')
            return False

        blocks = []

        limit_tuple = (limit, limit, limit)

        add_coord = tuple(map(add, coords, limit_tuple))
        sub_coord = list(map(sub, coords, limit_tuple))
        if sub_coord[0] < 0:
            sub_coord[0] = 0
        if sub_coord[1] < 0:
            sub_coord[1] = 0
        if sub_coord[2] < 0:
            sub_coord[2] = 0
        sub_coord = tuple(sub_coord)

        for x in range(sub_coord[0], add_coord[0]):
            for y in range(sub_coord[1], add_coord[1]):
                for z in range(sub_coord[2], add_coord[2]):
                    pos = Coord(x, y, z)
                    if self.validator.exposed(pos):
                        blocks.append(pos.get_as_tuple())

        return set(blocks)

    def get_block_number(self):
        total = 0
        for x in self.strata:
            for y in x:
                total += len(y)
        return total
