from pycraft.objects.block import Block
from pycraft.objects.textures import tex_coords

SAND = tex_coords((1, 1, 1), (1, 1), (1, 1))


class Sand(Block):
    texture_path = 'pycraft/textures/sand.png'
    identifier = 'Sand'
    texture = SAND
    breakable = True
    durability = 2
