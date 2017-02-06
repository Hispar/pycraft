from pycraft.objects.block import Block
from pycraft.objects.textures import tex_coords

BRICK = tex_coords((0, 0, 2), (0, 0, 2), (0, 0, 2))
BRICK2 = tex_coords((0, 1, 2), (0, 1, 2), (0, 1, 2))
BRICK3 = tex_coords((1, 0, 2), (1, 0, 2), (1, 0, 2))
GRASS = tex_coords((0, 1, 2), (1, 0, 2), (0, 0, 2))
SAND = tex_coords((1, 1, 1), (1, 1, 1), (1, 1, 1))
STONE = tex_coords((2, 1, 1), (2, 1, 1), (2, 1, 1))
GRANITE = tex_coords((0, 0, 1), (0, 0, 1), (0, 0, 1))


class Brick(Block):
    texture_path = 'pycraft/textures/brick2.png'
    identifier = 'Brick'
    texture = BRICK
    breakable = True
    durability = 10

    def update_texture(self):
        if self.block_duration < self.durability:
            self.texture = BRICK2
        if self.block_duration < self.durability / 2:
            self.texture = BRICK3


class Grass(Block):
    texture_path = 'pycraft/textures/grass.png'
    identifier = 'Grass'
    texture = GRASS
    breakable = True
    durability = 5


class Sand(Block):
    texture_path = 'pycraft/textures/sand.png'
    identifier = 'Sand'
    texture = SAND
    breakable = True
    durability = 2


class Stone(Block):
    texture_path = 'pycraft/textures/stone.png'
    identifier = 'Stone'
    texture = STONE


class WeakStone(Block):
    texture_path = 'pycraft/textures/stone.png'
    identifier = 'WeakStone'
    texture = STONE
    breakable = True
    durability = 15


class Granite(Block):
    texture_path = 'pycraft/textures/granite.png'
    identifier = 'Granite'
    texture = GRANITE
    breakable = True
    durability = 15
