from typing import Dict
from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions
from dataclasses import dataclass


class Kontroler(Toggle): #TODO
    """
    Includes the Kontroler in the randomizer which is a Key item.
    """
    display_name = "Include Kontroler"
    


#class InteriorWalls(Toggle):
    """
    Includes Interior Walls in the randomizer.
    (Adds 30 locations.)
    """
#    display_name = "Include Interior Walls"


#class Levelsanity(Toggle):
    """
    Includes each level up as an item location.
    (Adds 80 locations.)
    """
#    display_name = "Include Levelsanity"


#class DeathLink(Toggle):
#    """
#    If your party dies, so do your friends! The opposite is also true, of course.
#    """
#    display_name = "Deathlink"

@dataclass
class KronikiElevenaOptionSet(PerGameCommonOptions):
    kontroler: Kontroler
#    death_link: DeathLink