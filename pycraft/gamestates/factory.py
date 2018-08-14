from pycraft.gamestates.base import States
from pycraft.gamestates.states.mainscreen import MainScreenState
from pycraft.gamestates.states.running import RunningState


class GameStateFactory:

    def __init__(self, config):
        self.stack = list()
        self.config = config

    def get_game_state(self, state):
        try:
            if States(state) == States.RUNNING:
                return RunningState(self.config)
        except ValueError:
            pass
        return MainScreenState(self.config)
