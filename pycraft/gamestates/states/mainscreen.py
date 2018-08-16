from pycraft.gamestates.base import States
from pycraft.gamestates.gamestate import GameState
from pycraft.windows.layouts.mainscreen import MainScreenLayout


class MainScreenState(GameState):
    def __init__(self, gui, config):
        super(MainScreenState, self).__init__()
        self.state = States.MAIN_SCREEN
        self.active = True
        self._init_gui(gui)

    def _init_gui(self, gui):
        self.layout = MainScreenLayout()
        self.layout.get_start_btn().push_handlers(
            on_click=lambda w: self.start())
        self.layout.get_resume_btn().push_handlers(
            on_click=lambda w: self.resume())
        self.gui = gui
        self.gui.add(self.layout.get_layout())

    def update(self, dt, ticks_per_second):
        pass

    def start(self):
        self.active = False
        self.gui.remove(self.layout.get_layout())
        print('start')

    def resume(self):
        print('resume')
