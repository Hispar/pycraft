from pycraft.objects.block import Block
from pycraft.objects.textures import tex_coords

STONE = tex_coords((2, 1, 1), (2, 1), (2, 1))


class WeakStone(Block):
    texture_path = 'pycraft/textures/stone.png'
    identifier = 'WeakStone'
    texture = STONE
    breakable = True
    durability = 15
