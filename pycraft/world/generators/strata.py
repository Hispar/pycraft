from noise.perlin import SimplexNoise

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
        block_map = self.height_map
        for x, column in enumerate(self.height_map):
            for z, val in enumerate(column):
                dirt_thickness = simplex_noise2(x, z) / 24 - 4
                dirt_transition = self.height_map[x][z]
                stone_transition = dirt_thickness + dirt_transition

                y_map = {i: '' for i in range(self.depth)}
                for y in range(self.depth):
                    block_type = 'Air'
                    if y <= 0:
                        block_type = 'Stone'
                    elif y <= stone_transition:
                        block_type = 'WeakStone'
                    elif y <= dirt_transition:
                        block_type = 'Dirt'

                    y_map[y] = block_type

                block_map[x][z] = y_map

        return block_map
