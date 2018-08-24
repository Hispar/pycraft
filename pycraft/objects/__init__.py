from .block import Brick, Grass, Sand, Stone, WeakStone, Unbreakable, Air

brick = Brick()
grass = Grass()
sand = Sand()
weak_stone = WeakStone()
stone = Stone()
unbreakable = Unbreakable()
air = Air()


UNBREAKABLE_BLOCKS = [air.identifier, unbreakable.identifier, stone.identifier]
