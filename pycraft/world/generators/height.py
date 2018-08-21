from noise.perlin import SimplexNoise

simplex_noise2 = SimplexNoise(256).noise2


class HeightMap:

    def __init__(self, water_level, map_size):
        self.water_level = water_level
        self.map_size = map_size

    def height_field(self, x, z):
        """
        Calculate height for a determinate filed
        :param x:
        :param z:
        :return:
        """
        height_low = simplex_noise2(x * 1.3, z * 1.3) / 6 - 4
        height_high = simplex_noise2(x * 1.3, z * 1.3) / 5 + 6

        if simplex_noise2(x, z) / 8 > 0:
            height = height_low
        else:
            height = max(height_low, height_high)

        height = int(height / 2)

        if height < 0:
            height = height * 0.8

        return int(height + self.water_level)

    def create_height_map(self):
        """
        This functions requires the water_level and map_size.
        To calculate the 2D array of depth using perlin noise.
        :param map_size: Height and Width
        :return: 2D array
        """
        initial_map = [[0 for x in range(self.map_size[0])] for y in
                       range(self.map_size[0])]

        for x, column in enumerate(initial_map):
            for z, val in enumerate(column):
                initial_map[x][z] = self.height_field(x, z)

        return initial_map
