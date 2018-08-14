from pycraft.gamestates.base import States
from pycraft.gamestates.states.mainscreen import MainScreenState
from pycraft.gamestates.states.running import RunningState


class GameStateFactory:

    def __init__(self, config):
        self.stack = list()
        self.config = config

    def getGameState(self, state):
        # if States(state) == States.MAIN_SCREEN:
        #     pass
        if States(state) == States.RUNNING:
            return RunningState(self.config)
        return MainScreenState(self.config)
