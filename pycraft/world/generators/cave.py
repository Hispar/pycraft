class Cave:
    def __init__(self, strata, subterraean_generator, fill):
        self.strata = strata
        self.subterraean_generator = subterraean_generator
        self.fill = fill

    def create_cave(self, coords):
        blocks = self.subterraean_generator.get_area(coords, 1, 3)
        for block in blocks:
            self.strata[block[0]][block[1]][block[2]] = self.fill
