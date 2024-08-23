from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class KronikiElevenaItem(Item):
    game: str = "Kroniki Elevena"


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
    "Serek(Kapłan)":             KronikiElevenaItemData("Party",      756783_050, ItemClassification.progression),
    "Lara Croft":                KronikiElevenaItemData("Party",      756783_051, ItemClassification.useful),
    "Serek(Wsparcie)":           KronikiElevenaItemData("Party",      756783_052, ItemClassification.useful),
    "Kaktus mag":                KronikiElevenaItemData("Party",      756783_053, ItemClassification.useful),
    "Papyrus":                   KronikiElevenaItemData("Party",      756783_054, ItemClassification.progression),
    
    # Key Items
    "Kontroler":                 KronikiElevenaItemData("Progressive",   756783_055, ItemClassification.progression),
    "Krótkofalówka":             KronikiElevenaItemData("Progressive",   756783_056, ItemClassification.progression),
    "Siekiera":                  KronikiElevenaItemData("Progressive",   756783_057, ItemClassification.progression),
    "Młotek":                    KronikiElevenaItemData("Progressive",   756783_058, ItemClassification.progression),
    "Karta klucz I":             KronikiElevenaItemData("Progressive",   756783_059, ItemClassification.progression),
    "Karta klucz II":            KronikiElevenaItemData("Progressive",   756783_060, ItemClassification.progression),
    "Karta klucz V":             KronikiElevenaItemData("Progressive",   756783_061, ItemClassification.progression),
    "Przenośny teleport":        KronikiElevenaItemData("Progressive",   756783_062, ItemClassification.progression),
    "Kartka papieru":            KronikiElevenaItemData("Progressive",   756783_063, ItemClassification.progression),
    "Tajemnicza część":          KronikiElevenaItemData("Quest",         756783_064, ItemClassification.progression,           4),
    "Buty Laury":                KronikiElevenaItemData("Progressive",   756783_065, ItemClassification.progression),
    "Dysk do rzucania":          KronikiElevenaItemData("Progressive",   756783_066, ItemClassification.progression),
    "Złoty klucz":               KronikiElevenaItemData("Progressive",   756783_067, ItemClassification.progression),
    "Guziczek":                  KronikiElevenaItemData("Progressive",   756783_068, ItemClassification.progression),
    "Ołówek i gumka":            KronikiElevenaItemData("Progressive",   756783_069, ItemClassification.progression),
    "Antygrawitacyjne buty":     KronikiElevenaItemData("Progressive",   756783_070, ItemClassification.progression),
    "Klucz":                     KronikiElevenaItemData("Progressive",   756783_071, ItemClassification.progression),
    
    # Quest Items
    "Złoty grzyb":               KronikiElevenaItemData("Quest",         756783_072, ItemClassification.progression,           5),
    "Sos grzybowy":              KronikiElevenaItemData("Quest",         756783_073, ItemClassification.useful),
    
    # Fillers
    "Jabłko":                    KronikiElevenaItemData("Filler",        756783_074, weight=4),
    "Winogrono":                 KronikiElevenaItemData("Filler",        756783_075, weight=4),
    "Mandarynka":                KronikiElevenaItemData("Filler",        756783_076, weight=2),
    "Wiśnie":                    KronikiElevenaItemData("Filler",        756783_077, weight=3),
    "Zioła":                     KronikiElevenaItemData("Filler",        756783_078, weight=1),
    "Czerwony lum":              KronikiElevenaItemData("Filler",        756783_079, weight=1),
    "Niebieski lum":             KronikiElevenaItemData("Filler",        756783_080, weight=1),
    "Żółty lum":                 KronikiElevenaItemData("Filler",        756783_081, weight=1),
    "Marchewka":                 KronikiElevenaItemData("Filler",        756783_082, weight=2),
    "Srebrny klucz":             KronikiElevenaItemData("Filler",        756783_083, weight=2),
    "Pomidor":                   KronikiElevenaItemData("Filler",        756783_084, weight=3),
    "Koniczyna":                 KronikiElevenaItemData("Filler",        756783_085, weight=2),
    "Pikantna papryka":          KronikiElevenaItemData("Filler",        756783_086, weight=2),
    "Cytryna":                   KronikiElevenaItemData("Filler",        756783_087, weight=1),
    "Wyciąg z kaktusa":          KronikiElevenaItemData("Filler",        756783_088, weight=1),
    "Penizol":                   KronikiElevenaItemData("Filler",        756783_089, weight=1),
    "Prezent":                   KronikiElevenaItemData("Filler",        756783_090, weight=1),
    "Mała ognista bomba":        KronikiElevenaItemData("Filler",        756783_091, weight=2),
    "Duża ognista bomba":        KronikiElevenaItemData("Filler",        756783_092, weight=2),
    "Mała wodna bomba":          KronikiElevenaItemData("Filler",        756783_093, weight=2),
    "Duża wodna bomba":          KronikiElevenaItemData("Filler",        756783_094, weight=2),
    "Mała ziemna bomba":         KronikiElevenaItemData("Filler",        756783_095, weight=2),
    "Duża ziemna bomba":         KronikiElevenaItemData("Filler",        756783_096, weight=2),
    "Smocza miłość":             KronikiElevenaItemData("Filler",        756783_097, weight=1),
    "Meteoryt ataku":            KronikiElevenaItemData("Filler",        756783_098, weight=2),
    "Meteoryt magii":            KronikiElevenaItemData("Filler",        756783_099, weight=2),
    "Meteoryt szybkości":        KronikiElevenaItemData("Filler",        756783_100, weight=2),
    "Mikstura zdrowia":          KronikiElevenaItemData("Filler",        756783_101, weight=1),
    "Mikstura energii":          KronikiElevenaItemData("Filler",        756783_102, weight=1),
    "Płynny szał":               KronikiElevenaItemData("Filler",        756783_103, weight=1),
    "Gwiezdne Chrupki":          KronikiElevenaItemData("Filler",        756783_104, weight=2),
    "Psia kupa":                 KronikiElevenaItemData("Filler",        756783_105, weight=3),
    "Kokarda Tarkopsa":          KronikiElevenaItemData("Filler",        756783_106, weight=1),
    "Płatek róży":               KronikiElevenaItemData("Filler",        756783_107, weight=1),
    "Płatek Tem":                KronikiElevenaItemData("Filler",        756783_108, weight=2),
    "Płatek Tem (wyprzedaż)":    KronikiElevenaItemData("Filler",        756783_109, weight=4),
    "Płatek Tem (zatruty)":      KronikiElevenaItemData("Filler",        756783_110, weight=3),
    "Klejnot many":              KronikiElevenaItemData("Filler",        756783_111, weight=1),
    "Klejnot cyberpunktów":      KronikiElevenaItemData("Filler",        756783_112, weight=1),
    "Klejnot obrażeń":           KronikiElevenaItemData("Filler",        756783_113, weight=1),
    "Klejnot życia":             KronikiElevenaItemData("Filler",        756783_114, weight=1),
    "Klejnot ruchu":             KronikiElevenaItemData("Filler",        756783_115, weight=1),
    "Olbrzymia ognista bomba":   KronikiElevenaItemData("Filler",        756783_116, weight=1),
    "Gwiezdne Chrupki XL":       KronikiElevenaItemData("Filler",        756783_117, weight=1),
    "Spaghetti":                 KronikiElevenaItemData("Filler",        756783_118, weight=3),
    "Klejnot żywiołów":          KronikiElevenaItemData("Filler",        756783_119, weight=1),
    "Babeczka":                  KronikiElevenaItemData("Filler",        756783_120, weight=2),
    
    # Key Items 2
    "Jad Venesosa Planta":       KronikiElevenaItemData("Progressive",        756783_121, ItemClassification.progression),
    
    # Key Items(Dwienków)
    "Świeczka":                  KronikiElevenaItemData("Progressive",        756783_122, ItemClassification.progression),
    "Info. o skrzyni":           KronikiElevenaItemData("Progressive",        756783_123, ItemClassification.progression),
    "Info. o książkach":         KronikiElevenaItemData("Progressive",        756783_124, ItemClassification.progression),
    "Info. o kominku":           KronikiElevenaItemData("Progressive",        756783_125, ItemClassification.progression),
    "Materiał":                  KronikiElevenaItemData("Progressive",        756783_126, ItemClassification.progression),
    "Odcisk stopy":              KronikiElevenaItemData("Progressive",        756783_127, ItemClassification.progression),
    "Info. o diamencie":         KronikiElevenaItemData("Progressive",        756783_128, ItemClassification.progression),
    
    # Key Items(Snowdin)
    "Zeznania Blooka":           KronikiElevenaItemData("Progressive",        756783_129, ItemClassification.progression),
    "Zeznania Snowdrake'a":      KronikiElevenaItemData("Progressive",        756783_130, ItemClassification.progression),
    "Zielony materiał":          KronikiElevenaItemData("Progressive",        756783_131, ItemClassification.progression),
    "Lodowy kolec":              KronikiElevenaItemData("Progressive",        756783_132, ItemClassification.progression),
    "Miejsce zbrodni":           KronikiElevenaItemData("Progressive",        756783_133, ItemClassification.progression),
    
    # Kapsuły
    "Kapsuła Plush Foxy'ego":    KronikiElevenaItemData("Quest",        756783_134, ItemClassification.useful),
    "Kapsuła Hatera":            KronikiElevenaItemData("Quest",        756783_135, ItemClassification.useful),
    "Kapsuła Dingle'a":          KronikiElevenaItemData("Quest",        756783_136, ItemClassification.useful),
    "Kapsuła Alex'a":            KronikiElevenaItemData("Quest",        756783_137, ItemClassification.useful),
    "Kapsuła Złotego Freddy'ego":KronikiElevenaItemData("Quest",        756783_138, ItemClassification.useful),
    "Kapsuła Kangurka Kao":      KronikiElevenaItemData("Quest",        756783_139, ItemClassification.useful),
    "Kapsuła Fuckboy'a":         KronikiElevenaItemData("Quest",        756783_140, ItemClassification.useful),
    "Kapsuła Anima":             KronikiElevenaItemData("Quest",        756783_141, ItemClassification.useful),
    "Kapsuła Turreta":           KronikiElevenaItemData("Quest",        756783_142, ItemClassification.useful),
    "Kapsuła Mrokluma":          KronikiElevenaItemData("Quest",        756783_143, ItemClassification.useful),
    "Kapsuła Andre":             KronikiElevenaItemData("Quest",        756783_144, ItemClassification.useful),
    "Kapsuła Specimena 2":       KronikiElevenaItemData("Quest",        756783_145, ItemClassification.useful),
    "Kapsuła Foxy'ego":          KronikiElevenaItemData("Quest",        756783_146, ItemClassification.useful),
    "Kapsuła Jeffa":             KronikiElevenaItemData("Quest",        756783_147, ItemClassification.useful),
    "Kapsuła Kukiełki":          KronikiElevenaItemData("Quest",        756783_148, ItemClassification.useful),
    "Kapsuła Ultra Greeda":      KronikiElevenaItemData("Quest",        756783_149, ItemClassification.useful),
    
    # Key Items 3
    "Doggo":                     KronikiElevenaItemData("Progressive",        756783_150, ItemClassification.progression),
    "Telefon":                   KronikiElevenaItemData("Progressive",        756783_151, ItemClassification.progression),
    "Dusza":                     KronikiElevenaItemData("Progressive",        756783_152, ItemClassification.progression),
    "Diament":                   KronikiElevenaItemData("Progressive",        756783_153, ItemClassification.progression_skip_balancing,           5),
    
    # Armors
    "Niszczyciel":           KronikiElevenaItemData("Progressive",        756783_154, ItemClassification.useful),
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