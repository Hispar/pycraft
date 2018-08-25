import time
from collections import OrderedDict

from pyglet import image
from pyglet.gl import GL_QUADS
from pyglet.graphics import Batch, TextureGroup

from pycraft.util import cube_vertices, cube_shade
from pycraft.world.area import Area
from pycraft.world.opengl import PycraftOpenGL
from pycraft.world.sector import Sector
from pycraft.world.visibility import Visibility


class World:
    def __init__(self, map):
        # A Batch is a collection of vertex lists for batched rendering.
        self.batch = Batch()
        # A TextureGroup manages an OpenGL texture.
        self.texture_group = {}
        # Mapping from position to a pyglet `VertextList` for all shown blocks.
        self._shown = {}
        self.show_hide_queue = OrderedDict()
        # Which sector the player is currently in.
        self.sector = None

        # Mapping from sector to a list of positions inside that sector.
        self.sectors = {}
        # Same mapping as `world` but only contains blocks that are shown.
        # self.shown = {}
        self.visibility = Visibility()

        PycraftOpenGL()

        # A mapping from position to the texture of the block at that position.
        # This defines all the blocks that are currently in the world.
        # self.area = Area()
        self.map = map

    def show_area(self, coords):
        area = self.map.get_surface_blocks(10, coords)
        if not area:
            return False
        print(area)
        for coord in area:
            self._show_block(coord)

    # def get_blocks(self):
    #     return self.map.get_blocks()
    #
    # def add_block(self, coords, block, immediate=True):
    #     """Add a block with the given `texture` and `position` to the world.
    #
    #     Parameters
    #     ----------
    #     coords : tuple of len 3
    #         The (x, y, z) position of the block to add.
    #     block : list of len 3
    #         The coordinates of the texture squares. Use `tex_coords()` to
    #         generate.
    #     immediate : bool
    #         Whether or not to draw the block immediately.
    #     """
    #     self.area.add_block(coords, block)
    #     if immediate:
    #         if self.area.exposed(coords):
    #             self.show_block(coords, block, immediate)
    #             neighbors = self.area.get_neighbors(coords)
    #             for element in neighbors['hide']:
    #                 self.hide_block(element['coords'])
    #             for element in neighbors['show']:
    #                 self.show_block(element['coords'], element['block'])
    #
    # def remove_block(self, coords):
    #     """
    #     Remove a block from the world. And shows the neighbors
    #     :param coords:
    #     :return:
    #     """
    #     self.area.remove_block(coords)
    #     self.hide_block(coords)
    #     neighbors = self.area.get_neighbors(coords)
    #     for element in neighbors['hide']:
    #         self.hide_block(element['coords'])
    #     for element in neighbors['show']:
    #         self.show_block(element['coords'], element['block'])
    #
    # def show_block(self, coords, block, immediate=False):
    #     """Ensure all blocks that should be shown are drawn
    #     to the canvas.
    #
    #     Parameters
    #     ----------
    #     coords : tuple of len 3
    #         The (x, y, z) position of the block to show.
    #     block : list of len 3
    #         The coordinates of the texture squares. Use `tex_coords()` to
    #         generate.
    #     immediate : bool
    #         Whether or not to immediately remove the block from the canvas.
    #     """
    #
    #     if coords in self.shown:
    #         return
    #     self.shown[coords] = block
    #     if not immediate:
    #         self.show_hide_queue[coords] = True
    #         return
    #     self._show_block(coords, block)
    #
    def _show_block(self, coords):
        """Private implementation of the `show_block()` method.

        Parameters
        ----------
        coords : tuple of len 3
            The (x, y, z) position of the block to show.
        """
        x, y, z = coords
        block = self.map.get_block(coords)
        vertex_data = cube_vertices(x, y, z, 0.5)
        shade_data = cube_shade(1, 1, 1, 1)
        texture_data = block.texture
        if block.identifier not in self.texture_group:
            self.texture_group[block.identifier] = TextureGroup(
                image.load(block.texture_path).get_texture())

        self._shown[coords] = self.batch.add(
            24, GL_QUADS, self.texture_group[block.identifier],
            ('v3f/static', vertex_data),
            ('c3f/static', shade_data),
            ('t2f/static', texture_data))
        self.visibility.show_coord(coords)

    def _hide_block(self, coords):
        """Private implementation of the 'hide_block()` method."""
        self.visibility.hide_coord(coords)
        self._shown.pop(coords).delete()

    def hide_block(self, coords, immediate=True):
        """Ensure all blocks that should be hidden are hide
        from the canvas."""
        if not self.visibility.is_visible(coords):
            return

        self.visibility.hide_coord(coords)
        if not immediate:
            self.show_hide_queue[coords] = False
        self._hide_block(coords)

    def _dequeue(self):
        """Pop the top function from the internal queue and call it."""
        coords, show = self.show_hide_queue.popitem(last=False)
        shown = self.visibility.is_visible(coords)
        if show and not shown:
            self._show_block(coords)
        elif shown and not show:
            self._hide_block(coords)

    def process_queue(self, ticks_per_sec):
        """Process the entire queue while taking periodic breaks. This allows
        the game loop to run smoothly. The queue contains calls to
        _show_block() and _hide_block() so this method should be called if
        add_block() or remove_block() was called with immediate=False
        """
        start = time.clock()
        while self.show_hide_queue and time.clock() - start < 1.0 / ticks_per_sec:
            self._dequeue()

    def process_entire_queue(self):
        """Process the entire queue with no breaks."""
        while self.show_hide_queue:
            self._dequeue()

    # def add_sector(self, sector, coords):
    #     #     self.sector = coords
    #     #     self.sectors[coords] = sector
    #     #     # self.sectors.setdefault(coords, []).append(sector)
    #     #
    #     # def show_sector(self, coords, immediate=True):
    #     #     """Ensure all blocks in the given sector that should be shown are drawn
    #     #     to the canvas.
    #     #     """
    #     #     sector = self.sectors.get(coords)
    #     #     if sector:
    #     #         for position in sector.blocks:
    #     #             if position not in self.shown and self.area.exposed(position):
    #     #                 self.show_block(position, immediate)
    #     #     else:
    #     #         sector = Sector(coords, self.area)
    #     #         self.add_sector(sector, coords)
    #     #         self.show_sector(coords)
    #     #
    #     # def hide_sector(self, coords):
    #     #     """Ensure all blocks in the given sector that should be hidden are
    #     #     removed from the canvas.
    #     #     """
    #     #     sector = self.sectors.get(coords)
    #     #     if not sector:
    #     #         return
    #     #     for position in sector.blocks:
    #     #         if position in self.shown:
    #     #             self.hide_block(position, False)

    # def change_sectors(self, before, after):
    #     """Move from sector `before` to sector `after`. A sector is a
    #     contiguous x, y sub-region of world. Sectors are used to speed up
    #     world rendering.
    #     """
    #     before_set = set()
    #     after_set = set()
    #     pad = 4
    #     for dx in range(-pad, pad + 1):
    #         for dy in [0]:  # range(-pad, pad + 1):
    #             for dz in range(-pad, pad + 1):
    #                 if dx ** 2 + dy ** 2 + dz ** 2 > (pad + 1) ** 2:
    #                     continue
    #                 if before:
    #                     x, y, z = before
    #                     before_set.add((x + dx, y + dy, z + dz))
    #                 if after:
    #                     x, y, z = after
    #                     after_set.add((x + dx, y + dy, z + dz))
    #     show = after_set - before_set
    #     hide = before_set - after_set
    #     for coords in hide:
    #         self.hide_sector(coords)
    #     for coords in show:
    #         self.show_sector(coords)
