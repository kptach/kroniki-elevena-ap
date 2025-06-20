import shutil
import os
import sys
from const import *


def make_apworld(dir, world_name):
    subdir = os.path.join(dir, "..")
    shutil.make_archive(world_name, 'zip', dir)
    zip = os.path.join(subdir, world_name + ".zip")
    apworld = os.path.join(subdir, world_name + ".apworld")
    os.replace(zip, apworld)

def make_and_add_apworld(dir, world_name, archipelago_custom_worlds_path=ARCHIPELAGO_PATH):
    subdir = os.path.join(dir, "..")
    shutil.make_archive(world_name, 'zip', dir)
    zip = os.path.join(subdir, world_name + ".zip")
    apworld = os.path.join(subdir, world_name + ".apworld")
    os.replace(zip, apworld)
    os.replace(apworld, os.path.join(archipelago_custom_worlds_path, f"{world_name}.apworld"))

def main():
    make_and_add_apworld(WORLDS_DIR,  GAME_NAME)
    
if __name__ == "__main__":
    main()
    sys.exit(0)