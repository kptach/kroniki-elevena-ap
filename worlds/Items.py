from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class KronikiElevenaItem(Item):
    game: str = "Five Nights at Fuckboy's"


class KronikiElevenaItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


def get_items_by_category(category: str) -> Dict[str, KronikiElevenaItemData]:
    item_dict: Dict[str, KronikiElevenaItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict


item_table: Dict[str, KronikiElevenaItemData] = {
    # Characters
    "Cupcake":                   KronikiElevenaItemData("Party",      756783_000, ItemClassification.useful),
    "Plush Foxy":                KronikiElevenaItemData("Party",      756783_001, ItemClassification.useful),
    "Turret":                    KronikiElevenaItemData("Party",      756783_002, ItemClassification.useful),
    "Zombie":                    KronikiElevenaItemData("Party",      756783_003, ItemClassification.useful),
    "Pająk":                     KronikiElevenaItemData("Party",      756783_004, ItemClassification.useful),
    "Chlebek":                   KronikiElevenaItemData("Party",      756783_005, ItemClassification.useful),
    "Galaretka":                 KronikiElevenaItemData("Party",      756783_006, ItemClassification.useful),
    "Hater":                     KronikiElevenaItemData("Party",      756783_007, ItemClassification.useful),
    "Dip":                       KronikiElevenaItemData("Party",      756783_008, ItemClassification.useful),
    "Bob's Brain":               KronikiElevenaItemData("Party",      756783_009, ItemClassification.useful),
    "Bóbr":                      KronikiElevenaItemData("Party",      756783_010, ItemClassification.useful),
    "Mroklum":                   KronikiElevenaItemData("Party",      756783_011, ItemClassification.useful),
    "Robopirat":                 KronikiElevenaItemData("Party",      756783_012, ItemClassification.useful),
    "Worms":                     KronikiElevenaItemData("Party",      756783_013, ItemClassification.useful),
    "Slender":                   KronikiElevenaItemData("Party",      756783_014, ItemClassification.useful),
    "Dingle":                    KronikiElevenaItemData("Party",      756783_015, ItemClassification.useful),
    "Chica":                     KronikiElevenaItemData("Party",      756783_016, ItemClassification.useful),
    "SCP-173":                   KronikiElevenaItemData("Party",      756783_017, ItemClassification.useful),
    "Blue Baby":                 KronikiElevenaItemData("Party",      756783_018, ItemClassification.useful),
    "Alex":                      KronikiElevenaItemData("Party",      756783_019, ItemClassification.useful),
    "Robopirat Ninja":           KronikiElevenaItemData("Party",      756783_020, ItemClassification.useful),
    "Andre":                     KronikiElevenaItemData("Party",      756783_021, ItemClassification.useful),
    "Globox":                    KronikiElevenaItemData("Party",      756783_022, ItemClassification.useful),
    "Android":                   KronikiElevenaItemData("Party",      756783_023, ItemClassification.useful),
    "Specimen 2":                KronikiElevenaItemData("Party",      756783_024, ItemClassification.useful),
    "Baloon Boy":                KronikiElevenaItemData("Party",      756783_025, ItemClassification.useful),
    "Toy Bonnie":                KronikiElevenaItemData("Party",      756783_026, ItemClassification.useful),
    "Rayman":                    KronikiElevenaItemData("Party",      756783_027, ItemClassification.useful),
    "Kao":                       KronikiElevenaItemData("Party",      756783_028, ItemClassification.useful),
    "Boogeyman":                 KronikiElevenaItemData("Party",      756783_029, ItemClassification.useful),
    "Spooky":                    KronikiElevenaItemData("Party",      756783_030, ItemClassification.useful),
    "Freddy":                    KronikiElevenaItemData("Party",      756783_031, ItemClassification.useful),
    "Złoty Freddy":              KronikiElevenaItemData("Party",      756783_032, ItemClassification.useful),
    "Phantom Foxy":              KronikiElevenaItemData("Party",      756783_033, ItemClassification.useful),
    "SCP-049":                   KronikiElevenaItemData("Party",      756783_034, ItemClassification.useful),
    "Reflux":                    KronikiElevenaItemData("Party",      756783_035, ItemClassification.useful),
    "Jeff":                      KronikiElevenaItemData("Party",      756783_036, ItemClassification.useful),
    "Isaac":                     KronikiElevenaItemData("Party",      756783_037, ItemClassification.useful),
    "Azazel":                    KronikiElevenaItemData("Party",      756783_038, ItemClassification.useful),
    "Monstro II":                KronikiElevenaItemData("Party",      756783_039, ItemClassification.useful),
    "Brzytwobrody":              KronikiElevenaItemData("Party",      756783_040, ItemClassification.useful),
    "Fuckboy":                   KronikiElevenaItemData("Party",      756783_041, ItemClassification.useful),
    "Purple Guy":                KronikiElevenaItemData("Party",      756783_042, ItemClassification.useful),
    "BB":                        KronikiElevenaItemData("Party",      756783_043, ItemClassification.useful),
    "SCP-106":                   KronikiElevenaItemData("Party",      756783_044, ItemClassification.useful),
    "Kukiełka":                  KronikiElevenaItemData("Party",      756783_045, ItemClassification.useful),
    "Ultra Greed":               KronikiElevenaItemData("Party",      756783_046, ItemClassification.useful),
    "Anim":                      KronikiElevenaItemData("Party",      756783_047, ItemClassification.useful),
    "Cat Mario":                 KronikiElevenaItemData("Party",      756783_048, ItemClassification.useful),
    "Indiana":                   KronikiElevenaItemData("Party",      756783_049, ItemClassification.useful),
    "Serek(Kapłan)":             KronikiElevenaItemData("Party",      756783_050, ItemClassification.useful),
    "Lara Croft":                KronikiElevenaItemData("Party",      756783_051, ItemClassification.useful),
    "Serek(Wsparcie)":           KronikiElevenaItemData("Party",      756783_052, ItemClassification.useful),
    "Kaktus mag":                KronikiElevenaItemData("Party",      756783_053, ItemClassification.useful),
    "Papyrus":                   KronikiElevenaItemData("Party",      756783_054, ItemClassification.useful),
}

"""
    # Weapons
    "Progressive Microphone":   KronikiElevenaItemData("FreddyWeapons",    756783_003, ItemClassification.progression,                 6),
    "Progressive Guitar":       KronikiElevenaItemData("BonnieWeapons",    756783_004, ItemClassification.progression,                 6),
    "Progressive Cupcakes":     KronikiElevenaItemData("ChicaWeapons",     756783_005, ItemClassification.progression,                 6),
    "Progressive Hook":         KronikiElevenaItemData("FoxyWeapons",      756783_006, ItemClassification.progression,                 6),
    "Dragon ...":             KronikiElevenaItemData("Useful",           756783_007, ItemClassification.useful),

    # Skills
    "Tophat Toss":              KronikiElevenaItemData("FreddySkills",     756783_008, ItemClassification.progression),
    "Lead Stinger":             KronikiElevenaItemData("FreddySkills",     756783_009, ItemClassification.progression),
    "Toreador March":           KronikiElevenaItemData("FreddySkills",     756783_010, ItemClassification.progression),
    "Bunny Hop":                KronikiElevenaItemData("BonnieSkills",     756783_011, ItemClassification.progression),
    "Backup Bash":              KronikiElevenaItemData("BonnieSkills",     756783_012, ItemClassification.progression),
    "Guitar Smash":             KronikiElevenaItemData("BonnieSkills",     756783_013, ItemClassification.progression),
    "Fearless Flight":          KronikiElevenaItemData("ChicaSkills",      756783_014, ItemClassification.useful),
    "Pizza Pass":               KronikiElevenaItemData("ChicaSkills",      756783_015, ItemClassification.progression),
    "Caffeine Revival":         KronikiElevenaItemData("ChicaSkills",      756783_016, ItemClassification.progression),
    "Plank Walk":               KronikiElevenaItemData("FoxySkills",       756783_017, ItemClassification.progression),
    "Speed Share":              KronikiElevenaItemData("FoxySkills",       756783_018, ItemClassification.useful),
    "Rushdown":                 KronikiElevenaItemData("FoxySkills",       756783_019, ItemClassification.progression),
    "Fazbear Combo":            KronikiElevenaItemData("FreddySkills",     756783_020, ItemClassification.useful),
    "Flighty Combo":            KronikiElevenaItemData("ChicaSkills",      756783_021, ItemClassification.useful),
    "Bonbon Combo":             KronikiElevenaItemData("BonnieSkills",     756783_022, ItemClassification.useful),
    "Pirate Combo":             KronikiElevenaItemData("FoxySkills",       756783_023, ItemClassification.useful),

    # Armor/Defense
    "Progressive Body Endoskeletons":   KronikiElevenaItemData("Armor", 756783_024, ItemClassification.progression,                4),
    "Progressive Head Endoskeletons":   KronikiElevenaItemData("Armor", 756783_025, ItemClassification.progression,                4),
    "Progressive Pizza Shields":        KronikiElevenaItemData("Armor", 756783_026, ItemClassification.progression,                4),
    "Progressive Caffeine Sodas":       KronikiElevenaItemData("Armor", 756783_027, ItemClassification.progression,                4),
    "Lucky Soda":                       KronikiElevenaItemData("Armor", 756783_028, ItemClassification.useful),
    "Double Pizza":                     KronikiElevenaItemData("Armor", 756783_029, ItemClassification.useful),
    "Ice Water":                        KronikiElevenaItemData("Armor", 756783_030, ItemClassification.useful),
    "Sneaky Juice":                     KronikiElevenaItemData("Armor", 756783_031, ItemClassification.useful),
    "Stealth Preserve":                 KronikiElevenaItemData("Armor", 756783_032, ItemClassification.useful),
    "Heist Cream":                      KronikiElevenaItemData("Armor", 756783_033, ItemClassification.useful),
    "Lunate Wine":                      KronikiElevenaItemData("Armor", 756783_034, ItemClassification.useful),
    "Thrifty Pretzels":                 KronikiElevenaItemData("Armor", 756783_035, ItemClassification.useful),

    # Progression
    "Lighter":                          KronikiElevenaItemData("Quest",      756783_036, ItemClassification.progression),
    "Bonnie's Head Voucher":            KronikiElevenaItemData("Quest",      756783_037, ItemClassification.progression),
    "Bonnie's Head":                    KronikiElevenaItemData("Quest",      756783_038, ItemClassification.progression),
    "Kitchen Key":                      KronikiElevenaItemData("Quest",      756783_039, ItemClassification.progression),
    "Reveal Interior Walls":            KronikiElevenaItemData("Quest",      756783_040, ItemClassification.progression),
    "Office Key Piece":                 KronikiElevenaItemData("Quest",      756783_041, ItemClassification.progression_skip_balancing,           4),
    "Backroom BB":                      KronikiElevenaItemData("Quest",      756783_042, ItemClassification.progression),
    "Restrooms BB":                     KronikiElevenaItemData("Quest",      756783_043, ItemClassification.progression),
    "Supply Closet BB":                 KronikiElevenaItemData("Quest",      756783_044, ItemClassification.progression),
    "East Hall Corner BB":              KronikiElevenaItemData("Quest",      756783_045, ItemClassification.progression),

    # Junk
    "Small Pizza":              KronikiElevenaItemData("Filler",     756783_046, weight=2),
    "Medium Pizza":             KronikiElevenaItemData("Filler",     756783_047, weight=4),
    "Large Pizza":              KronikiElevenaItemData("Filler",     756783_048, weight=3),
    "Small Soda":               KronikiElevenaItemData("Filler",     756783_049, weight=2),
    "Medium Soda":              KronikiElevenaItemData("Filler",     756783_050, weight=4),
    "Large Soda":               KronikiElevenaItemData("Filler",     756783_051, weight=3),
    "Pizza Slice":              KronikiElevenaItemData("Filler",     756783_052, weight=1),
    "Cake":                     KronikiElevenaItemData("Filler",     756783_053, weight=2),
    "Birthday Present":         KronikiElevenaItemData("Filler",     756783_054, weight=1),
    "X-Large Pizza":            KronikiElevenaItemData("Filler",     756783_055, weight=2),
    "X-Large Soda":             KronikiElevenaItemData("Filler",     756783_056, weight=2),
    "HP Boost":                 KronikiElevenaItemData("Filler",     756783_057, weight=1),
    "MP Boost":                 KronikiElevenaItemData("Filler",     756783_058, weight=1),
    "Attack Boost":             KronikiElevenaItemData("Filler",     756783_059, weight=1),
    "Defense Boost":            KronikiElevenaItemData("Filler",     756783_060, weight=1),
    "Interior Walls Key":       KronikiElevenaItemData("Filler",     756783_061, weight=1)
    
}
    """