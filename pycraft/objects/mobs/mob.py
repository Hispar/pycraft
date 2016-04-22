# project imports
from pycraft.objects.character import Character


class Mob(Character):
    breakable = True
    texture_path = 'pycraft/objects/textures.png'
    endurance = 1

    def __init__(self, config, position):
        self.live = self.endurance
        super(Mob, self).__init__(config, position)

    def hit_and_destroy(self):
        if not self.breakable:
            return False
        self.live -= 1
        return self.live == 0

    def update(self, dt, objects, mobs):
        """Private implementation of the `update()` method. This is where most
        of the motion logic lives, along with gravity and collision detection.

        Parameters
        ----------
        dt : float
            The change in time since the last call.
        """
        super(Mob, self).update(dt, objects, mobs)
