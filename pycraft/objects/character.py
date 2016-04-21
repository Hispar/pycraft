# project imports
from pycraft.objects.object import WorldObject
from pycraft.util import normalize

FACES = [
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]


class Character(WorldObject):
    def __init__(self, config, position=(0, 5, 0)):
        # Current (x, y, z) position in the world, specified with floats. Note
        # that, perhaps unlike in math class, the y-axis is the vertical axis.
        self.position = position

        # Velocity in the y (upward) direction.
        self.dy = 0

        # General Configuration

        # gravity
        self.gravity = config["gravity"]
        # speed
        self.walking_speed = config["walking_speed"]
        # terminal velocity
        self.terminal_velocity = config["terminal_velocity"]

    def collide(self, height, objects):
        """Checks to see if the character at the given `position` and `height`
        is colliding with any blocks or characters in the world.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position to check for collisions at.
        height : int or float
            The height of the player.

        Returns
        -------
        position : tuple of len 3
            The new position of the player taking into account collisions.
        """
        # How much overlap with a dimension of a surrounding block you need to
        # have to count as a collision. If 0, touching terrain at all counts as
        # a collision. If .49, you sink into the ground, as if walking through
        # tall grass. If >= .5, you'll fall through the ground.
        pad = 0.25
        p = list(self.position)
        np = normalize(self.position)
        for face in FACES:  # check all surrounding blocks
            for i in range(3):  # check each dimension independently
                if not face[i]:
                    continue
                # How much overlap you have with this dimension.
                d = (p[i] - np[i]) * face[i]
                if d < pad:
                    continue
                for dy in range(height):  # check each height
                    op = list(np)
                    op[1] -= dy
                    op[i] += face[i]
                    if tuple(op) not in objects:
                        continue
                    p[i] -= (d - pad) * face[i]
                    if face == (0, -1, 0) or face == (0, 1, 0):
                        # You are colliding with the ground or ceiling, so stop
                        # falling / rising.
                        self.dy = 0
                    break
        return tuple(p)
