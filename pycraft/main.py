import glooey
import pyglet.app

from pycraft.configuration import ConfigurationLoader
from pycraft.windows.game import GameWindow

WINDOW_CAPTION = 'PyCraft'


def main():
    # Load configuration file
    config_loader = ConfigurationLoader()
    config_data = config_loader.load_configuration_file()
    config_loader.check_configuration()

    game = GameWindow(config=config_data, caption=WINDOW_CAPTION)
    gui = glooey.Gui(game)
    vbox = game.get_vbox()
    gui.add(vbox)
    pyglet.app.run()
