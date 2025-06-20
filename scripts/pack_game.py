#WIP
from py7zr import pack_7zarchive
import sys
import os
import shutil
from const import *

shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive')


def pack_game(dir, output_path, game_name="kroniki-elevena"):
    shutil.make_archive(game_name, '7zip', dir)
    # archive = os.path.join(dir, game_name + ".7z")
    # apworld = os.path.join(subdir, game_name + ".7z")
    # os.replace(archive, apworld)
    
def main():
    pack_game(GAME_DIR, OUTPUT_PATH, GAME_NAME)
    
if __name__ == "__main__":
    main()
    sys.exit(0)
    
