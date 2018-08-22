import random
from math import sin, cos
from operator import add, sub

from pycraft.world.generators.coords import Coord
from pycraft.world.generators.validator import Validator


class SubterraneanArea:
    def __init__(self, strata):
        self.validator = Validator(strata)
        # Cave direction
        self.theta = random.uniform(0, 1)
        self.delta_t = 0
        self.phi = random.uniform(0, 1)
        self.delta_p = 0

        # variable initialization
        self.coords = None
        self.size = None

    def get_area(self, coords, min_size, max_size):
        self.coords = coords
        self.size = random.uniform(min_size, max_size)
        blocks = self.create_area_skeleton()
        return self.fill_area(blocks)

    def get_random_underground_positions(self, count, limits):
        """
        Return :count: random underground positions
        :param count: Number of positions
        :param limits: map dimensions
        :return:
        """
        positions = []
        while len(positions) < count:
            x, y, z = limits
            pos = Coord(random.randint(0, x), random.randint(0, y), random.randint(0, z))
            if self.validator.is_underground(pos):
                positions.append(pos)
        return positions

    def create_area_skeleton(self):
        pos = self.coords
        blocks = [pos.get_as_tuple()]
        for i in range(int(self.size)):
            pos.x = pos.x + sin(self.theta) * cos(self.phi)
            pos.y = pos.y + cos(self.theta) * cos(self.phi)
            pos.z = pos.z + sin(self.phi)

            self.theta = self.theta + self.delta_t * 0.2
            self.delta_t = self.delta_t * 0.9 + random.uniform(0, 0.5)
            self.phi = self.phi * 0.5 + self.delta_p * 0.25
            self.delta_p = self.delta_p * 0.75 + random.uniform(0, 0.5)
            int_pos = Coord(*pos.get_as_tuple())
            if self.validator.is_usable(int_pos):
                blocks.append(pos.get_as_tuple())

        return blocks

    def fill_area(self, blocks):
        for coord in blocks.copy():
            radius = self.get_random_radius()
            add_coord = tuple(map(add, coord, radius))
            sub_coord = tuple(map(sub, coord, radius))
            for x in range(sub_coord[0], add_coord[0] + 1):
                pos = Coord(x, coord[1], coord[2])
                if self.validator.is_usable(pos):
                    blocks.append(pos.get_as_tuple())

            for y in range(sub_coord[1], add_coord[1] + 1):
                pos = Coord(coord[0], y, coord[2])
                if self.validator.is_usable(pos):
                    blocks.append(pos.get_as_tuple())

            for z in range(sub_coord[2], add_coord[2] + 1):
                pos = Coord(coord[0], coord[1], z)
                if self.validator.is_usable(pos):
                    blocks.append(pos.get_as_tuple())

        return blocks

    @staticmethod
    def get_probabilities():
        """
        Generate an array with dimensions by probability
        1 - 55%, 2- 25%, 3 - 10%, 4 - 3%, 5 - 2%, 6 - 2%, 7 - 1%, 10 - 1%
        :return:
        """
        return [1] * 55 + [2] * 25 + [3] * 10 + [4] * 3 + [5] * 2 + [6] * 2 + \
               [7] * 2 + [10] * 1

    def get_random_radius(self):
        """
        Generate the random radius based in the probabilities array
        :return: Tuple with the radius to apply
        """
        probabilities = self.get_probabilities()
        return (
            probabilities[random.randint(0, 99)],
            probabilities[random.randint(0, 99)],
            probabilities[random.randint(0, 99)],
        )
