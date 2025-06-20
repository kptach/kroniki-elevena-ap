import os

ARCHIPELAGO_PATH = "C:\\ProgramData\\Archipelago\\custom_worlds"
GAME_NAME = "kroniki-elevena"
DIR = os.path.dirname(os.path.realpath(__file__))
WORLDS_DIR = os.path.join(DIR, "..", "worlds")
GAME_DIR = os.path.join(DIR, "..", "games", GAME_NAME)
OUTPUT_PATH = os.path.join(DIR, "..", "bin")