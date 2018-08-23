from pycraft.world.generators.cave import Cave
from pycraft.world.generators.height import HeightMap
from pycraft.world.generators.strata import StrataMap
from pycraft.world.generators.subterranean import SubterraneanArea


class Generator:
    def __init__(self, config, map_size):
        self.config = config['world']
        self.map_size = map_size

    def generate(self):
        # Create 2D height map
        height_map_generator = HeightMap(self.config['water_level'],
                                         self.map_size)
        height_map = height_map_generator.create_height_map()

        # Create 3D block map
        strata_generator = StrataMap(self.config['depth'], height_map)
        strata_map = strata_generator.create_strata()

        subterranean_generator = SubterraneanArea(strata_map)
        # Get random positions for caves
        limits = self.map_size + (self.config['depth'],)
        coords = subterranean_generator.get_random_underground_positions(
            2, limits)

        # Create caves
        for coord in coords:
            cave_generator = Cave(strata_map, subterranean_generator, 'air')
            cave_generator.create_cave(coord)

        return strata_map
        # self.depth = config['world']['depth']

        # self.carve_out_caves()
        # self.create_ore_veins()
        # self.flood_water()
        # self.flood_lava()
        # self.create_surface()
        # self.create_plants()
        # self.create_buildings()
