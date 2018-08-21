import pyglet.app

from pycraft.configuration import ConfigurationLoader
from pycraft.windows.game import GameWindow
from pycraft.world.generator import Generator

WINDOW_CAPTION = 'PyCraft'


def main():
    # Load configuration file
    config_loader = ConfigurationLoader()
    config_data = config_loader.load_configuration_file()
    config_loader.check_configuration()

    GameWindow(config=config_data, caption=WINDOW_CAPTION)

    generator = Generator(config_data, (10, 10))
    pyglet.app.run()
