# Python imports
import random

# project imports
from pycraft.objects.mobs.mob import Mob
from ..textures import tex_coords

# texture coords
WATER = tex_coords((1, 0), (0, 1), (0, 0))


class Chicken(Mob):
    identifier = 'chicken'
    texture = WATER
    breakable = True
    texture_path = 'pycraft/objects/texture/water.jpg'

    def __init__(self, config, position):
        super(Chicken, self).__init__(config, position)
        self.name = '{}_{}'.format(self.identifier, random.randint(1, 100))
