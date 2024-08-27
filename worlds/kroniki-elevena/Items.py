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
    "Kontroler":                 KronikiElevenaItemData("Quest",         756783_055, ItemClassification.progression),
    "Krótkofalówka":             KronikiElevenaItemData("Quest",         756783_056, ItemClassification.progression),
    "Siekiera":                  KronikiElevenaItemData("Quest",         756783_057, ItemClassification.progression),
    "Młotek":                    KronikiElevenaItemData("Quest",         756783_058, ItemClassification.progression),
    "Karta klucz I":             KronikiElevenaItemData("Quest",         756783_059, ItemClassification.progression),
    "Karta klucz II":            KronikiElevenaItemData("Quest",         756783_060, ItemClassification.progression),
    "Karta klucz V":             KronikiElevenaItemData("Quest",         756783_061, ItemClassification.progression),
    "Przenośny teleport":        KronikiElevenaItemData("Quest",         756783_062, ItemClassification.progression),
    "Kartka papieru":            KronikiElevenaItemData("Quest",         756783_063, ItemClassification.progression),
    "Tajemnicza część":          KronikiElevenaItemData("Quest",         756783_064, ItemClassification.progression,           4),
    "Buty Laury":                KronikiElevenaItemData("Quest",         756783_065, ItemClassification.progression),
    "Dysk do rzucania":          KronikiElevenaItemData("Quest",         756783_066, ItemClassification.progression),
    "Złoty klucz":               KronikiElevenaItemData("Quest",         756783_067, ItemClassification.progression),
    "Guziczek":                  KronikiElevenaItemData("Quest",         756783_068, ItemClassification.progression),
    "Ołówek i gumka":            KronikiElevenaItemData("Quest",         756783_069, ItemClassification.progression),
    "Antygrawitacyjne buty":     KronikiElevenaItemData("Quest",         756783_070, ItemClassification.progression),
    "Klucz":                     KronikiElevenaItemData("Quest",         756783_071, ItemClassification.progression),
    
    # Quest Items
    "Złoty grzyb":               KronikiElevenaItemData("Quest",         756783_072, ItemClassification.progression,           5),
    "Sos grzybowy":              KronikiElevenaItemData("Quest",         756783_073, ItemClassification.useful),
    
    # Fillers
    "Jabłko":                    KronikiElevenaItemData("Filler",        756783_074, weight=4, max_quantity=15),
    "Winogrono":                 KronikiElevenaItemData("Filler",        756783_075, weight=4, max_quantity=15),
    "Mandarynka":                KronikiElevenaItemData("Filler",        756783_076, weight=2, max_quantity=15),
    "Wiśnie":                    KronikiElevenaItemData("Filler",        756783_077, weight=3, max_quantity=15),
    "Zioła":                     KronikiElevenaItemData("Filler",        756783_078, weight=1, max_quantity=15),
    "Czerwony lum":              KronikiElevenaItemData("Filler",        756783_079, weight=1, max_quantity=10),
    "Niebieski lum":             KronikiElevenaItemData("Filler",        756783_080, weight=1, max_quantity=10),
    "Żółty lum":                 KronikiElevenaItemData("Filler",        756783_081, weight=1, max_quantity=10),
    "Marchewka":                 KronikiElevenaItemData("Filler",        756783_082, weight=2, max_quantity=15),
    "Srebrny klucz":             KronikiElevenaItemData("Filler",        756783_083, weight=2, max_quantity=10), # i will change it later
    "Pomidor":                   KronikiElevenaItemData("Filler",        756783_084, weight=3, max_quantity=15), 
    "Koniczyna":                 KronikiElevenaItemData("Filler",        756783_085, weight=2, max_quantity=15),
    "Pikantna papryka":          KronikiElevenaItemData("Filler",        756783_086, weight=2, max_quantity=15),
    "Cytryna":                   KronikiElevenaItemData("Filler",        756783_087, weight=1, max_quantity=15),
    "Wyciąg z kaktusa":          KronikiElevenaItemData("Filler",        756783_088, weight=1, max_quantity=15),
    "Penizol":                   KronikiElevenaItemData("Filler",        756783_089, weight=1, max_quantity=5),
    "Prezent":                   KronikiElevenaItemData("Filler",        756783_090, weight=1, max_quantity=10),
    "Mała ognista bomba":        KronikiElevenaItemData("Filler",        756783_091, weight=2, max_quantity=10),
    "Duża ognista bomba":        KronikiElevenaItemData("Filler",        756783_092, weight=2, max_quantity=10),
    "Mała wodna bomba":          KronikiElevenaItemData("Filler",        756783_093, weight=2, max_quantity=10),
    "Duża wodna bomba":          KronikiElevenaItemData("Filler",        756783_094, weight=2, max_quantity=10),
    "Mała ziemna bomba":         KronikiElevenaItemData("Filler",        756783_095, weight=2, max_quantity=10),
    "Duża ziemna bomba":         KronikiElevenaItemData("Filler",        756783_096, weight=2, max_quantity=10),
    "Smocza miłość":             KronikiElevenaItemData("Filler",        756783_097, weight=1, max_quantity=10),
    "Meteoryt ataku":            KronikiElevenaItemData("Filler",        756783_098, weight=2, max_quantity=10),
    "Meteoryt magii":            KronikiElevenaItemData("Filler",        756783_099, weight=2, max_quantity=10),
    "Meteoryt szybkości":        KronikiElevenaItemData("Filler",        756783_100, weight=2, max_quantity=10),
    "Mikstura zdrowia":          KronikiElevenaItemData("Filler",        756783_101, weight=1, max_quantity=10),
    "Mikstura energii":          KronikiElevenaItemData("Filler",        756783_102, weight=1, max_quantity=10),
    "Płynny szał":               KronikiElevenaItemData("Filler",        756783_103, weight=1, max_quantity=10),
    "Gwiezdne Chrupki":          KronikiElevenaItemData("Filler",        756783_104, weight=2, max_quantity=15),
    "Psia kupa":                 KronikiElevenaItemData("Filler",        756783_105, weight=3, max_quantity=10),
    "Kokarda Tarkopsa":          KronikiElevenaItemData("Filler",        756783_106, weight=1, max_quantity=15),
    "Płatek róży":               KronikiElevenaItemData("Filler",        756783_107, weight=1, max_quantity=5),
    "Płatek Tem":                KronikiElevenaItemData("Filler",        756783_108, weight=2, max_quantity=5),
    "Płatek Tem (wyprzedaż)":    KronikiElevenaItemData("Filler",        756783_109, weight=4, max_quantity=5),
    "Płatek Tem (zatruty)":      KronikiElevenaItemData("Filler",        756783_110, weight=3, max_quantity=5),
    "Klejnot many":              KronikiElevenaItemData("Filler",        756783_111, weight=1, max_quantity=10),
    "Klejnot cyberpunktów":      KronikiElevenaItemData("Filler",        756783_112, weight=1, max_quantity=10),
    "Klejnot obrażeń":           KronikiElevenaItemData("Filler",        756783_113, weight=1, max_quantity=10),
    "Klejnot życia":             KronikiElevenaItemData("Filler",        756783_114, weight=1, max_quantity=10),
    "Klejnot ruchu":             KronikiElevenaItemData("Filler",        756783_115, weight=1, max_quantity=10),
    "Olbrzymia ognista bomba":   KronikiElevenaItemData("Filler",        756783_116, weight=1, max_quantity=10),
    "Gwiezdne Chrupki XL":       KronikiElevenaItemData("Filler",        756783_117, weight=1, max_quantity=10),
    "Spaghetti":                 KronikiElevenaItemData("Filler",        756783_118, weight=3, max_quantity=10),
    "Klejnot żywiołów":          KronikiElevenaItemData("Filler",        756783_119, weight=1, max_quantity=5),
    "Babeczka":                  KronikiElevenaItemData("Filler",        756783_120, weight=2, max_quantity=5),
    
    # Key Items 2
    "Jad Venesosa Planta":       KronikiElevenaItemData("Quest",        756783_121, ItemClassification.progression,       1), # I will leater change number if nessesary
    
    # Key Items(Dwienków)
    "Świeczka":                  KronikiElevenaItemData("Quest",        756783_122, ItemClassification.progression),
    "Info. o skrzyni":           KronikiElevenaItemData("Quest",        756783_123, ItemClassification.progression),
    "Info. o książkach":         KronikiElevenaItemData("Quest",        756783_124, ItemClassification.progression),
    "Info. o kominku":           KronikiElevenaItemData("Quest",        756783_125, ItemClassification.progression),
    "Materiał":                  KronikiElevenaItemData("Quest",        756783_126, ItemClassification.progression),
    "Odcisk stopy":              KronikiElevenaItemData("Quest",        756783_127, ItemClassification.progression),
    "Info. o diamencie":         KronikiElevenaItemData("Quest",        756783_128, ItemClassification.progression),
    
    # Key Items(Snowdin)
    "Zeznania Blooka":           KronikiElevenaItemData("Quest",        756783_129, ItemClassification.progression),
    "Zeznania Snowdrake'a":      KronikiElevenaItemData("Quest",        756783_130, ItemClassification.progression),
    "Zielony materiał":          KronikiElevenaItemData("Quest",        756783_131, ItemClassification.progression),
    "Lodowy kolec":              KronikiElevenaItemData("Quest",        756783_132, ItemClassification.progression),
    "Miejsce zbrodni":           KronikiElevenaItemData("Quest",        756783_133, ItemClassification.progression),
    
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
    "Doggo":                     KronikiElevenaItemData("Quest",        756783_150, ItemClassification.progression),
    "Różowe majciochy":          KronikiElevenaItemData("Quest",        756783_151, ItemClassification.progression),
    "Dusza":                     KronikiElevenaItemData("Quest",        756783_152, ItemClassification.progression),
    "Diament":                   KronikiElevenaItemData("Quest",        756783_153, ItemClassification.progression_skip_balancing,           5),
    
    # Armors
    "Niszczyciel":               KronikiElevenaItemData("Armor",        756783_154, ItemClassification.useful, 4),
    "Deska":                     KronikiElevenaItemData("Armor",        756783_155, ItemClassification.useful, 4),
    "Wzmacniacz zdrowia":        KronikiElevenaItemData("Armor",        756783_156, ItemClassification.useful, 4),
    "Ubijaczka":                 KronikiElevenaItemData("Armor",        756783_157, ItemClassification.useful, 4),
    "Kołdra":                    KronikiElevenaItemData("Armor",        756783_158, ItemClassification.useful, 4),
    "Wspomagacz":                KronikiElevenaItemData("Armor",        756783_159, ItemClassification.useful, 4),
    
    "Kask":                      KronikiElevenaItemData("Armor",        756783_160, ItemClassification.useful, 2),
    "Drewniana tarcza":          KronikiElevenaItemData("Armor",        756783_161, ItemClassification.useful, 2),
    "Kapelusz":                  KronikiElevenaItemData("Armor",        756783_162, ItemClassification.useful, 2),
    "Rubinowy naszyjnik":        KronikiElevenaItemData("Armor",        756783_163, ItemClassification.useful, 2),
    "Pelerynka":                 KronikiElevenaItemData("Armor",        756783_164, ItemClassification.useful, 2),
    "Kapelusz wiedźmy":          KronikiElevenaItemData("Armor",        756783_165, ItemClassification.useful, 2),
    
    "Wilcze szpony":             KronikiElevenaItemData("Armor",        756783_166, ItemClassification.useful, 4),
    "Wilcze futro":              KronikiElevenaItemData("Armor",        756783_167, ItemClassification.useful, 4),
    "Szczurzy ogon":             KronikiElevenaItemData("Armor",        756783_168, ItemClassification.useful, 4),
    "Złote pięści":              KronikiElevenaItemData("Armor",        756783_169, ItemClassification.useful, 4),
    "Różaniec":                  KronikiElevenaItemData("Armor",        756783_170, ItemClassification.useful, 4),
    "Karta Mądrości":            KronikiElevenaItemData("Armor",        756783_171, ItemClassification.useful, 4),
    "Lewy but":                  KronikiElevenaItemData("Armor",        756783_172, ItemClassification.useful, 4),
    "Czarna dziura":             KronikiElevenaItemData("Armor",        756783_173, ItemClassification.useful, 4),
    "Pistolet":                  KronikiElevenaItemData("Armor",        756783_174, ItemClassification.useful, 4),
    "Błyskawica":                KronikiElevenaItemData("Armor",        756783_175, ItemClassification.useful, 4),
    "Głaz":                      KronikiElevenaItemData("Armor",        756783_176, ItemClassification.useful, 4),
    "Kupa gruzu":                KronikiElevenaItemData("Armor",        756783_177, ItemClassification.useful, 4),
    "Toksyczna zbroja":          KronikiElevenaItemData("Armor",        756783_178, ItemClassification.useful, 4),
    "Dopalacz":                  KronikiElevenaItemData("Armor",        756783_179, ItemClassification.useful, 4),
    "Kapelusz złodzieja":        KronikiElevenaItemData("Armor",        756783_180, ItemClassification.useful, 4),
    "Odnawiacz zdrowia I":       KronikiElevenaItemData("Armor",        756783_181, ItemClassification.useful, 4),

    "Kamienna tarcza":           KronikiElevenaItemData("Armor",        756783_182, ItemClassification.useful, 2),
    "Drewniany puklerz":         KronikiElevenaItemData("Armor",        756783_183, ItemClassification.useful, 2),
    "Kamienny puklerz":          KronikiElevenaItemData("Armor",        756783_184, ItemClassification.useful, 2),
    "Peleryna":                  KronikiElevenaItemData("Armor",        756783_185, ItemClassification.useful, 2),
    "Szata ciemności":           KronikiElevenaItemData("Armor",        756783_186, ItemClassification.useful, 2),
    "Szaty księcia":             KronikiElevenaItemData("Armor",        756783_187, ItemClassification.useful, 2),
    "Żelazne rękawice":          KronikiElevenaItemData("Armor",        756783_188, ItemClassification.useful, 2),
    "Mistyczny kapelusz":        KronikiElevenaItemData("Armor",        756783_189, ItemClassification.useful, 2),
    "Hełm rycerza":              KronikiElevenaItemData("Armor",        756783_190, ItemClassification.useful, 2),
    "Królicze uszy":             KronikiElevenaItemData("Armor",        756783_191, ItemClassification.useful, 2),

    "Srebrny miecz":             KronikiElevenaItemData("Armor",         756783_192, ItemClassification.useful, 4),
    "Obieraczka":                KronikiElevenaItemData("Armor",         756783_193, ItemClassification.useful, 4),
    "Mistyczne ostrze":          KronikiElevenaItemData("Armor",         756783_194, ItemClassification.useful, 4),
    "Złoty łuk":                 KronikiElevenaItemData("Armor",         756783_195, ItemClassification.useful, 4),
    "Różdżka":                   KronikiElevenaItemData("Armor",         756783_196, ItemClassification.useful, 4),
    "Patyk":                     KronikiElevenaItemData("Armor",         756783_197, ItemClassification.useful, 4),
    "Zachód słońca":             KronikiElevenaItemData("Armor",         756783_198, ItemClassification.useful, 4),
    "Gówniana tarcza":           KronikiElevenaItemData("Armor",         756783_199, ItemClassification.useful, 4),
    "Kartka papieru":            KronikiElevenaItemData("Armor",         756783_200, ItemClassification.useful, 4),
    "Narysowany pancerz":        KronikiElevenaItemData("Armor",         756783_201, ItemClassification.useful, 4),
    "Gówniany zapach":           KronikiElevenaItemData("Armor",         756783_202, ItemClassification.useful, 4),
    "Technologia":               KronikiElevenaItemData("Armor",         756783_203, ItemClassification.useful, 4),
    "Złote pióro":               KronikiElevenaItemData("Armor",         756783_204, ItemClassification.useful, 4),
    "Zajebisty but":             KronikiElevenaItemData("Armor",         756783_205, ItemClassification.useful, 4),
    "Armor mocy":                KronikiElevenaItemData("Armor",         756783_206, ItemClassification.useful, 4),
    "Karta Skilla I":            KronikiElevenaItemData("Armor",         756783_207, ItemClassification.useful, 4),

    "Opaska bohatera":           KronikiElevenaItemData("Armor",         756783_208, ItemClassification.useful, 2),
    "Smoczy amulet":             KronikiElevenaItemData("Armor",         756783_209, ItemClassification.useful, 2),
    "Cegła":                     KronikiElevenaItemData("Armor",         756783_210, ItemClassification.useful, 2),
    "Magiczna tarcza":           KronikiElevenaItemData("Armor",         756783_211, ItemClassification.useful, 2),

    "Jopek":                     KronikiElevenaItemData("Armor",         756783_212, ItemClassification.useful, 4),
    "Damka":                     KronikiElevenaItemData("Armor",         756783_213, ItemClassification.useful, 4),
    "Król":                      KronikiElevenaItemData("Armor",         756783_214, ItemClassification.useful, 4),
    "As":                        KronikiElevenaItemData("Armor",         756783_215, ItemClassification.useful, 4),
    "Dzida":                     KronikiElevenaItemData("Armor",         756783_216, ItemClassification.useful, 4),
    "Srebrna Dzida":             KronikiElevenaItemData("Armor",         756783_217, ItemClassification.useful, 4),
    "Złota Dzida":               KronikiElevenaItemData("Armor",         756783_218, ItemClassification.useful, 4),
    "Diamentowa Dzida":          KronikiElevenaItemData("Armor",         756783_219, ItemClassification.useful, 4),
    "Kubek Zdrowia":             KronikiElevenaItemData("Armor",         756783_220, ItemClassification.useful, 4),
    "Worek Zdrowia":             KronikiElevenaItemData("Armor",         756783_221, ItemClassification.useful, 4),
    "Wiadro Zdrowia":            KronikiElevenaItemData("Armor",         756783_222, ItemClassification.useful, 4),
    "Beczka zdrowia":            KronikiElevenaItemData("Armor",         756783_223, ItemClassification.useful, 4),
    "Skóra Knaarena":            KronikiElevenaItemData("Armor",         756783_224, ItemClassification.useful, 4),




}