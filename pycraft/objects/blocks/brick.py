from pycraft.objects.block import Block
from pycraft.objects.textures import tex_coords

BRICK = tex_coords((0, 0, 2), (0, 0), (0, 0))
BRICK2 = tex_coords((0, 1, 2), (0, 1), (0, 1))
BRICK3 = tex_coords((1, 0, 2), (1, 0), (1, 0))


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
