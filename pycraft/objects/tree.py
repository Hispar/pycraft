from pyglet import image
from pyglet.graphics import TextureGroup, GL_QUADS

from pycraft.objects import Granite
from pycraft.objects.object import WorldObject
from pycraft.util import cube_vertices, cube_shade


class Tree(WorldObject):

    def __init__(self):
        self.texture_group = {}
        self.parts = {}

    def render(self, coords, batch):
        """

        Parameters
        ----------
        coords : tuple of len 3
            The (x, y, z) position of the block to show.
        """
        granite = Granite()
        x, y, z = coords
        shade_data = cube_shade(1, 1, 1, 1)
        texture_data = granite.texture

        if granite.identifier not in self.texture_group:
            self.texture_group[granite.identifier] = TextureGroup(image.load(granite.texture_path).get_texture())

        for i in range(y, y + 3):
            vertex_data = cube_vertices(x, i, z, 0.5)
            coords = (coords[0], i, coords[2])
            self.parts[coords] = batch.add(
                24, GL_QUADS, self.texture_group[granite.identifier],
                ('v3f/static', vertex_data),
                ('c3f/static', shade_data),
                ('t2f/static', texture_data))
