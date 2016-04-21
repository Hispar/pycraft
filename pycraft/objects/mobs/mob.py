# project imports
from pycraft.objects.character import Character


class Mob(Character):
    breakable = True
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

    # def update(self, dt, objects):
    #     """Private implementation of the `update()` method. This is where most
    #     of the motion logic lives, along with gravity and collision detection.
    #
    #     Parameters
    #     ----------
    #     dt : float
    #         The change in time since the last call.
    #     """
    #     # walking
    #     speed = WALKING_SPEED
    #     d = dt * speed  # distance covered this tick.
    #     dx, dy, dz = self.get_motion_vector()
    #     # New position in space, before accounting for gravity.
    #     dx, dy, dz = dx * d, dy * d, dz * d
    #     # gravity
    #
    #     # Update your vertical speed: if you are falling, speed up until you
    #     # hit terminal velocity; if you are jumping, slow down until you
    #     # start falling.
    #     self.dy -= dt * GRAVITY
    #     self.dy = max(self.dy, -TERMINAL_VELOCITY)
    #     dy += self.dy * dt
    #     # collisions
    #     x, y, z = self.position
    #     x, y, z = self.collide((x + dx, y + dy, z + dz),
    #                            PLAYER_HEIGHT, objects)
    #     self.position = (x, y, z)
