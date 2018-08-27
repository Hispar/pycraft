from pycraft.gamestates.base import States
from pycraft.gamestates.gamestate import GameState
from pycraft.objects.map import Map
from pycraft.objects.player import Player
from pycraft.windows.layouts.loading import LoadingLayout
from pycraft.world.generator import Generator
from pycraft.world.world import World


class LoadingState(GameState):
    def __init__(self, gui, config, world):
        super(LoadingState, self).__init__()
        self.state = States.LOADING
        self.active = True
        self._init_gui(gui)
        if world:
            self.world = world
        else:
            self.load_world(config)

    def load_world(self, config):
        generator = Generator(config, (100, 100))
        strata = generator.generate()
        map = Map(strata)
        world = World(map)
        self.world = world

    def _init_gui(self, gui):
        self.layout = LoadingLayout()
        self.gui = gui
        self.gui.add(self.layout.get_layout())

    def update(self, dt, ticks_per_second):
        if self.world:
            self.active = False
            self.gui.remove(self.layout.get_layout())