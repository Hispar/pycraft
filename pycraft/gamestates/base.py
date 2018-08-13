"""
    Requires python version 3.4 or greater
"""
from enum import Enum


class States(Enum):
    MAIN_SCREEN = 1
    MAIN_MENU = 2
    RUNNING = 3
    INVENTORY_MENU = 4
    CRAFTING_MENU = 5
    OPTIONS_MENU = 6
