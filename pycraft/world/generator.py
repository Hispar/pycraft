from pycraft.world.generators.cave import Cave
from pycraft.world.generators.coords import Coord
from pycraft.world.generators.height import HeightMap
from pycraft.world.generators.strata import StrataMap
from pycraft.world.generators.subterranean import SubterraneanArea


class Generator:
    def __init__(self, config, map_size):
        print(config['world'], map_size)
        height_map_generator = HeightMap(config['world']['water_level'],
                                         map_size)
        height_map = height_map_generator.create_height_map()

        strata_generator = StrataMap(config['world']['depth'], height_map)
        strata_map = strata_generator.create_strata()

        subterraean_generator = SubterraneanArea(strata_map)

        coords = Coord(5, 7, 5)
        cave_generator = Cave(strata_map, subterraean_generator, 'air')
        cave_generator.create_cave(coords)

        # self.depth = config['world']['depth']

        # self.carve_out_caves()
        # self.create_ore_veins()
        # self.flood_water()
        # self.flood_lava()
        # self.create_surface()
        # self.create_plants()
        # self.create_buildings()
