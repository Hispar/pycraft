# 3rd party imports
import glooey
import pyglet.clock
import pyglet.window

from pycraft.gamestates.manager import GameStateManager
from pycraft.gamestates.states.mainscreen import MainScreenState


class GameWindow(pyglet.window.Window):
    def __init__(self, config, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        self.config_data = config
        self.ticks_per_second = config["window"]["ticks_per_second"]
        # self.width = config["window"]["width"]
        # self.height = config["window"]["height"]
        # self.resizable = config["window"]["resizeable"]

        # Whether or not the window exclusively captures the mouse.
        self.exclusive = config["window"]["exclusive_mouse"]
        # self.set_exclusive_mouse(config["window"]["exclusive_mouse"])
        # This call schedules the `update()` method to be called
        # ticks_per_second. This is the main game event loop.
        pyglet.clock.schedule_interval(self.update,
                                       1.0 / self.ticks_per_second)

        gui = glooey.Gui(self)
        self.manager = GameStateManager(gui, config)
        self.manager.create_state()

        # self.init_state()

    # def init_state(self):
    #     """Create the game state manager and set the first state"""
    #     state = MainScreenState(self.config_data)
    #     self.manager.push(state)
    #     # This should be changed when we implement the MAINMENU game state
    #     # gs_running = GameStateRunning(self.config_data, height=self.height,
    #     #                               width=self.width)

    # def get_vbox(self):
    #     return self.manager.peek().get_vbox()

    # def on_mouse_press(self, x, y, button, modifiers):
    #     """Called when a mouse button is pressed. See pyglet docs for button
    #     amd modifier mappings.
    #
    #     Parameters
    #     ----------
    #     x, y : int
    #         The coordinates of the mouse click. Always center of the screen if
    #         the mouse is captured.
    #     button : int
    #         Number representing mouse button that was clicked. 1 = left button,
    #         4 = right button.
    #     modifiers : int
    #         Number representing any modifying keys that were pressed when the
    #         mouse button was clicked.
    #     """
    #
    #     if self.exclusive:
    #         self.gamestatemanager.peek().on_mouse_press(x, y, button,
    #                                                     modifiers)
    #     else:
    #         self.set_exclusive_mouse(True)
    #
    # def on_mouse_motion(self, x, y, dx, dy):
    #     """Called when the player moves the mouse.
    #
    #     Parameters
    #     ----------
    #     x, y : int
    #         The coordinates of the mouse click. Always center of the screen if
    #         the mouse is captured.
    #     dx, dy : float
    #         The movement of the mouse.
    #     """
    #     if self.exclusive:
    #         self.gamestatemanager.peek().on_mouse_motion(x, y, dx, dy)
    #
    # def on_key_press(self, symbol, modifiers):
    #     """Called when the player presses a key. See pyglet docs for key
    #     mappings.
    #
    #     Parameters
    #     ----------
    #     symbol : int
    #         Number representing the key that was pressed.
    #     modifiers : int
    #         Number representing any modifying keys that were pressed.
    #     config_data["controls"] : dict
    #         control map read by the configuration file
    #     """
    #     if symbol == key.ESCAPE:
    #         self.set_exclusive_mouse(False)
    #     else:
    #         self.gamestatemanager.peek().on_key_press(symbol, modifiers,
    #                                                   self.config_data[
    #                                                       "controls"])
    #
    # def on_key_release(self, symbol, modifiers):
    #     """Called when the player releases a key. See pyglet docs for key
    #     mappings.
    #
    #     Parameters
    #     ----------
    #     symbol : int
    #         Number representing the key that was pressed.
    #     modifiers : int
    #         Number representing any modifying keys that were pressed.
    #     config_data["controls"] : dict
    #         control map read by the configuration file
    #     """
    #     self.gamestatemanager.peek().on_key_release(symbol, modifiers,
    #                                                 self.config_data[
    #                                                     "controls"])
    #
    # def on_resize(self, width, height):
    #     """Called when the window is resized to a new `width` and `height`."""
    #     self.gamestatemanager.peek().on_resize(width, height)

    def on_draw(self):
        """Called by pyglet to draw the canvas.

            Pass the current window size
        """
        # vbox = self.get_vbox()
        # self.gui.add(vbox)
        # # pass

        # self.clear()
        self.manager.peek().on_draw(self.get_size())

    def update(self, dt):
        """This method is scheduled to be called repeatedly by the pyglet
        clock.

        Parameters
        ----------
        dt : float
            The change in time since the last call.
        ticks_per_second:
        """
        self.manager.switch_game_state()
        self.manager.peek().update(dt, self.ticks_per_second)
        # pass
