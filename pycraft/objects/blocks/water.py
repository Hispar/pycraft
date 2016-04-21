# project imports
from ..textures import tex_coords
from ..block import Block

# texture coords
WATER = tex_coords((1, 0), (0, 1), (0, 0))


class Water(Block):
    identifier = 'water'
    texture = WATER
    breakable = True
    texture_path = 'pycraft/objects/texture/water.jpg'
