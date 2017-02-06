# python imports
import importlib
import sys

# project imports
from .object import WorldObject


class Block(WorldObject):
    texture_path = 'pycraft/textures/stone.png'
    durability = 1

    def __init__(self):
        self.block_duration = self.durability

    def hit_and_destroy(self):
        if not self.breakable:
            return False
        self.block_duration -= 1
        self.update_texture()
        return self.block_duration == 0

    def update_texture(self):
        pass


def get_block(identifier):
    try:
        classname = getattr(importlib.import_module("pycraft.objects.blocks"), identifier)
        return classname()
    except KeyError:
        sys.exit('Exiting! Class {} can\'t be instanciated'.format(identifier))
