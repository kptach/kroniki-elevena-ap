from typing import Dict
from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet


# class Kontroler(Toggle): #TODO
#     """
#     Includes the Kontroler in the randomizer which is a Key item.
#     """
#     display_name = "Include Kontroler"


#class InteriorWalls(Toggle):
    # """
    # Includes Interior Walls in the randomizer.
    # (Adds 30 locations.)
    # """
#    display_name = "Include Interior Walls"


class ElevenSanity(Toggle):
    """
    Includes each level up as an item location.
    (Adds 80 locations.)
    """
    display_name = "Include Levelsanity"
    
class ElevenLevels(Range):
    """
    The number of levels to include in the randomizer.
    (Default: 80)
    """
    range_start = 2
    range_end = 99
    default = 20
    
class PapyrusSanity(Toggle):
    """
    Includes each level up as an item location.
    (Adds 80 locations.)
    """
    display_name = "Include Levelsanity"
    
class PapyrusLevels(Range):
    """
    The number of levels to include in the randomizer.
    (Default: 80)
    """
    range_start = 2
    range_end = 99
    default = 20
    
class SerekSanity(Toggle):
    """
    Includes each level up as an item location.
    (Adds 80 locations.)
    """
    display_name = "Include Levelsanity"
    
class SerekLevels(Range):
    """
    The number of levels to include in the randomizer.
    (Default: 80)
    """
    range_start = 2
    range_end = 50
    default = 20

#class DeathLink(Toggle):
#    """
#    If your party dies, so do your friends! The opposite is also true, of course.
#    """
#    display_name = "Deathlink"


kroniki_elevena_options: Dict[str, type(Option)] = { 
#    "kontroler": Kontroler,
#    "telefon": Telefon,
#    "krutkofalowka": Krutkofalowka,
#    "elevenSanity": ElevenSanity # gives checks from levels of eleven
#    "papyrussanity": Papyrussanity # gives checks from levels of papyrus
#    "Sereksanity": Papyrussanity # gives checks from levels of papyrus
#    "death_link": DeathLink
#    "trap_link": TrapLink
}