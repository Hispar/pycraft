from noise.perlin import SimplexNoise

simplex_noise2 = SimplexNoise(256).noise2


class Generator:
    def __init__(self, config, map_size):
        height_map = self.create_height_map(config['world']['water_level'],
                                            map_size)
        self.create_strata(config['world']['depth'], height_map)
        # self.carve_out_caves()
        # self.create_ore_veins()
        # self.flood_water()
        # self.flood_lava()
        # self.create_surface()
        # self.create_plants()
        # self.create_buildings()

    @staticmethod
    def create_height_map(water_level, map_size):
        """
        This functions requires the water_level and map_size.
        To calculate the 2D array of depth using perlin noise.
        :param water_level: Water level
        :param map_size: Height and Width
        :return:
        """
        initial_map = [[0 for x in range(map_size[0])] for y in
                       range(map_size[0])]
        for column in initial_map:
            x, z = column
            height_low = simplex_noise2(x * 1.3, z * 1.3) / 6 - 4
            height_high = simplex_noise2(x * 1.3, z * 1.3) / 5 + 6

            if simplex_noise2(x, z) / 8 > 0:
                height = height_low
            else:
                height = max(height_low, height_high)

            height = int(height / 2)

            if height < 0:
                height = height * 0.8

            initial_map[x][z] = int(height + water_level)

        return initial_map

    @staticmethod
    def create_strata(depth, height_map):
        """
        Create the 3D array with blocks
        :param depth: Map depth
        :param height_map: previously calculate height map
        :return:
        """
        block_map = height_map
        for column in height_map:
            x, z = column
            dirt_thickness = simplex_noise2(x, z) / 24 - 4
            dirt_transition = height_map[x][z]
            stone_transition = dirt_thickness + dirt_transition

            y_map = {i: '' for i in range(depth)}
            for y in range(depth):
                block_type = 'air'
                if y <= stone_transition:
                    block_type = 'unbreakable'
                elif y <= dirt_transition:
                    block_type = 'dirt'

                y_map[y] = block_type

            block_map[x][z] = y_map

        return block_map
