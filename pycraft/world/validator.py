from pycraft.objects import UNBREAKABLE_BLOCKS, unbreakable, air
from pycraft.objects.character import FACES
from pycraft.world.generators.coords import Coord


class Validator:
    def __init__(self, blocks):
        self.blocks = blocks

    def is_in_map(self, coords):
        try:
            block = self.blocks[coords.x][coords.y][coords.z]
        except KeyError:
            return False
        except IndexError:
            return False
        return True

    def _is_unbreakable(self, coords):
        """
        Private function which checks if the block in the coords is unbreakable
        :param coords:
        :return:
        """
        block = self.blocks[coords.x][coords.y][coords.z]
        if block.identifier in UNBREAKABLE_BLOCKS:
            return True
        return False

    def _is_limit(self, coords):
        """
        Private function which checks if the block in the coords is unbreakable
        :param coords:
        :return:
        """
        block = self.blocks[coords.x][coords.y][coords.z]
        if block.identifier == unbreakable.identifier:
            return True
        return False

    def _is_air(self, coords):
        """
        Private function which checks if the block in the coords is unbreakable
        :param coords:
        :return:
        """
        block = self.blocks[coords.x][coords.y][coords.z]
        if block.identifier == air.identifier:
            return True
        return False

    def is_air(self, coords):
        """
        Public is air interface
        :param coords:
        :return:
        """
        if not self.is_in_map(coords):
            return False
        return self._is_air(coords)

    def exposed(self, coords):
        if not self.is_in_map(coords):
            return False

        if self._is_air(coords):
            return False

        for dx, dy, dz in FACES:
            face = Coord(coords.x + dx, coords.y + dy, coords.z + dz)
            if self.is_air(face):
                return True
        return False

    def is_usable(self, coords):
        """
        Check if the coords are in the map and if the block is breakable
        :param coords:
        :return:
        """
        if not self.is_in_map(coords):
            return False
        return not self._is_limit(coords)

    def is_underground(self, coords):
        """
        Check if the coords are in the map and if the block is breakable
        :param coords:
        :return:
        """
        if not self.is_in_map(coords):
            return False
        return self._is_unbreakable(coords)

    def is_user_friendly(self, coords):
        """
        Check if the coords are in the map, the block is air, and the user has floor
        :param coords:
        :return:
        """
        if not self.is_in_map(coords):
            return False
        if self._is_limit(coords):
            return False

        floor = coords.get_floor()
        for coord in floor:
            if not self.is_in_map(coord):
                return False
            if self._is_air(coord):
                return False

        if not self._is_air(coords):
            return False

        coords.y += 1
        if not self._is_air(coords):
            return False

        return True
