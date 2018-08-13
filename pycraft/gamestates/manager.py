class GameStateManager:
    """
        Desirable option for game states switch - don't let this function for the
        main method

        It's implemented as a stack in order to let game states return to previous
        one without  the need it to know for which state it is returning to (e.g.
        maps and option menus)
    """

    def __init__(self):
        self.stack = list()

    # TODO define a good way to map each possible game state
    def switch_game_state(self):
        pass

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        return self.stack.pop()

    def push(self, game_state):
        self.stack.append(game_state)
