from pycraft.gamestates.base import States
from pycraft.gamestates.states.loading import LoadingState
from pycraft.gamestates.states.mainscreen import MainScreenState
from pycraft.gamestates.states.running import RunningState


class GameStateFactory:

    def __init__(self, gui, config):
        self.stack = list()
        self.gui = gui
        self.config = config

    def get_game_state(self, state, world=None):
        try:
            if States(state) == States.RUNNING:
                return RunningState(self.gui, self.config, world)
            if States(state) == States.LOADING:
                return LoadingState(self.gui, self.config, world)
        except ValueError:
            pass
        return MainScreenState(self.gui, self.config)
