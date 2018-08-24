class Visibility:

    def __init__(self):
        self.coords = set()

    def is_visible(self, coord):
        return coord in self.coords

    def show_coord(self, coord):
        self.coords.add(coord)

    def get_all(self):
        return self.coords

    def hide_coord(self, coord):
        self.coords.remove(coord)


