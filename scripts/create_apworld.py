import shutil
import os
import sys

ARCHIPELAGO_PATH = "C:\\ProgramData\\Archipelago\\custom_worlds"
GAME_NAME = "kroniki-elevena"
DIR = os.path.dirname(os.path.realpath(__file__))
WORLDS_DIR = os.path.join(DIR, "..", "worlds")


def make_apworld(dir, world_name, archipelago_custom_worlds_path=ARCHIPELAGO_PATH):
    subdir = os.path.join(dir, "..")
    shutil.make_archive(world_name, 'zip', dir)
    zip = os.path.join(subdir, world_name + ".zip")
    apworld = os.path.join(subdir, world_name + ".apworld")
    os.replace(zip, apworld)
    os.replace(apworld, os.path.join(archipelago_custom_worlds_path + f"\\{world_name}.apworld"))

def main():
    make_apworld(WORLDS_DIR,  GAME_NAME)
    
if __name__ == "__main__":
    main()
    sys.exit(0)