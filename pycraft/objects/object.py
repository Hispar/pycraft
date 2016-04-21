
class WorldObject:
    unique = False
    texture = None
    breakable = False
    texture_path = None
    durability = 1
    # How much overlap with a dimension of a surrounding block you need to
    # have to count as a collision. If 0, touching terrain at all counts as
    # a collision. If .49, you sink into the ground, as if walking through
    # tall grass. If >= .5, you'll fall through the ground.
    pad = 0.25
