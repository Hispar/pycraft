from noise.perlin import SimplexNoise

from pycraft.objects.block import get_block

simplex_noise2 = SimplexNoise(256).noise2


class StrataMap:

    def __init__(self, depth, height_map):
        self.depth = depth
        self.height_map = height_map

    def create_strata(self):
        """
        Create the 3D array with blocks
        :param depth: Map depth
        :param height_map: previously calculate height map
        :return:
        """
        block_map = self.height_map.copy()
        for x, column in enumerate(self.height_map):
            for z, val in enumerate(column):
                dirt_thickness = simplex_noise2(x, z) / 24 - 4
                dirt_transition = val
                stone_transition = dirt_thickness + dirt_transition
                block_map[x][z] = []

                for y in range(self.depth):
                    block_type = 'Air'
                    if y <= 0:
                        block_type = 'Unbreakable'
                    elif y <= stone_transition:
                        block_type = 'WeakStone'
                    elif y <= dirt_transition:
                        block_type = 'Dirt'

                    block_map[x][z].append(get_block(block_type))

        return block_map
