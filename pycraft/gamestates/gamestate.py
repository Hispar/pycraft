class GameState:
    """
        Just an interface. All Game States implementation defined in the States
        enum should extend this class and implement those methods
    """

    def __init__(self):
        pass

    """
        Think about those resposabilities from the GameState.
        Some game states may only need to be updated, while another only need
        to be drawn
    """

    def on_update(self):
        pass

    def on_draw(self, size):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_key_press(self, symbol, modifiers, controls):
        pass

    def on_key_release(self, symbol, modifiers, controls):
        pass

    # --- ** ---
    # Methods related to the GameStateManager
    """
        To be called AFTER the game state has been placed in the
        GameStateManager stack
    """

    def on_entered(self):
        pass

    """
        To be called BEFORE the game state is removed from the game
        state manager
    """

    def on_leaving(self):
        pass

    """
        To be called BEFORE another game state is stacked on top of the actual
    """

    def on_obscuring(self):
        pass

    """
        To be called AFTER this actual game state to be on the top of the
        GameStateManager stacked
    """

    def on_revealed(self):
        pass
