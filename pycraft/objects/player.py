# python imports
import math

# project imports
from pycraft.objects.character import Character

FACES = [
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]


class Player(Character):
    def __init__(self, config):
        super(Player, self).__init__(config, position=(0, 5, 0))
        # A list of blocks the player begins with. Hit num keys to cycle.
        self.inventory = ["brick", "grass", "sand", "weakstone"]
        # A dict of player blocks with their respective quantities
        self.items = {
            "brick": {
                "qty": 10
            },
            "grass": {
                "qty": 20
            },
            "sand": {
                "qty": 5
            },
            "weakstone": {
                "qty": 15
            }
        }
        # The current block the user can place. Hit num keys to cycle.
        self.block = self.inventory[0]

        # General Configuration
        # speed
        self.flying_speed = config["flying_speed"]
        # player height
        self.height = config["player_height"]

    def switch_inventory(self, index):
        """
        Change selected element in the inventory
        :param index:integer
        :return:None
        """
        if len(self.inventory):
            self.block = self.inventory[index % len(self.inventory)]

    def adjust_inventory(self, item, qty=1):
        """
        Adjusts player inventory when a block is placed; updates current
        block if item is no longer available
        :param item:string
        :param qty:integer
        :return:None
        """
        self.items[item]["qty"] -= qty
        if self.items[item]["qty"] == 0:
            self.inventory.remove(item)
            del self.items[item]
            if self.block == item:
                self.block = self.inventory[0] if len(self.inventory) else None

    def get_sight_vector(self):
        """Returns the current line of sight vector indicating the direction the
        player is looking.
        """
        x, y = self.rotation
        # y ranges from -90 to 90, or -pi/2 to pi/2, so m ranges from 0 to 1 and
        # is 1 when looking ahead parallel to the ground and 0 when looking
        # straight up or down.
        m = math.cos(math.radians(y))
        # dy ranges from -1 to 1 and is -1 when looking straight down and 1 when
        # looking straight up.
        dy = math.sin(math.radians(y))
        dx = math.cos(math.radians(x - 90)) * m
        dz = math.sin(math.radians(x - 90)) * m
        return dx, dy, dz

    def update(self, dt, objects):
        """Private implementation of the `update()` method. This is where most
        of the motion logic lives, along with gravity and collision detection.

        Parameters
        ----------
        dt : float
            The change in time since the last call.
        """
        # walking
        self.speed = self.flying_speed if self.flying else self.walking_speed
        return super(Player, self).update(dt, objects)
