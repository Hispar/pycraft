from pycraft.objects.block import Block
from pycraft.objects.textures import tex_coords

GRASS = tex_coords((0, 1, 2), (1, 0), (0, 0))


class Grass(Block):
    texture_path = 'pycraft/textures/grass.png'
    identifier = 'Grass'
    texture = GRASS
    breakable = True
    durability = 5
