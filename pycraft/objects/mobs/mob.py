from pycraft.objects.object import WorldObject


class Mob(WorldObject):
    unique = False
    texture = None
    breakable = False
    texture_path = 'pycraft/objects/textures.png'
    endurance = 1

    def __init__(self):
        self.live = self.endurance
        self.position = (10, 5, 0)

    def hit_and_destroy(self):
        if not self.breakable:
            return False
        self.live -= 1
        return self.live == 0
