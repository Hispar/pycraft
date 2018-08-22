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

    def is_usable(self, coords):
        if self.is_in_map(coords):
            block = self.blocks[coords.x][coords.y][coords.z]
            if block != 'Stone':
                return True
        return False

    def is_underground(self, coords):
        if self.is_in_map(coords):
            block = self.blocks[coords.x][coords.y][coords.z]
            if block not in ['Stone', 'Air']:
                return True
        return False
