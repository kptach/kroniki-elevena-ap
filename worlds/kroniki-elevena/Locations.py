from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class KronikiElevenaLocation(Location):
    game: str = "Kroniki Elevena"


class KronikiElevenaLocationData(NamedTuple):
    category: str
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, KronikiElevenaLocationData]:
    location_dict: Dict[str, KronikiElevenaLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


location_table: Dict[str, KronikiElevenaLocationData] = {
    # General Checks
    "Pierwsze miasto Dom1 - Skrzynia":                                    KronikiElevenaLocationData("General",   756783_000),
    "Pierwsze miasto Dom4 - Skrzynia":                                    KronikiElevenaLocationData("General",   756783_001),
    "Pierwsze miasto Wodospad - Złoty Muchomor":                          KronikiElevenaLocationData("Quests",   756783_002),
    "Cyberświat - parnter":                                               KronikiElevenaLocationData("Quests",   756783_003),
    "Dom Elevena (gra) - karty":                                         KronikiElevenaLocationData("General",   756783_004),

    "Dom Elevena - List":                                                 KronikiElevenaLocationData("Quests",   756783_005),
    
    "Jaskinia zagłady - Skrzynia1":                                       KronikiElevenaLocationData("General",   756783_008),
    "Jaskinia zagłady - Skrzynia2":                                       KronikiElevenaLocationData("General",   756783_009),

    "Pierwsze miasto Dom 5 - grzyby (Chlebek)":                           KronikiElevenaLocationData("Quests",   756783_010),
    "Pierwsze miasto Dom 5 - grzyby (Galaretka)":                         KronikiElevenaLocationData("Quests",   756783_011),
    "Pierwsze miasto Dom 5 - grzyby (Slender)":                           KronikiElevenaLocationData("Quests",   756783_012),
    "Pierwsze miasto Dom 5 - grzyby (Worms)":                             KronikiElevenaLocationData("Quests",   756783_013),
    "Pierwsze miasto Dom 5 - grzyby (Spooky)":                            KronikiElevenaLocationData("Quests",   756783_014),
    "Pierwsze miasto Dom 5 - grzyby (Sos grzybowy)":                      KronikiElevenaLocationData("Quests",   756783_015),
    
    "Dom Elevena (gra) - Jedzenie":                                      KronikiElevenaLocationData("General",   756783_016),

    
    "Jaskinia zagłady - Skrzynia3":                                       KronikiElevenaLocationData("General",   756783_026),
    
    "Dom Teda - Wyposażenie":                                             KronikiElevenaLocationData("Quests",   756783_027),

    
    "Sekret na prawo - Złoty Muchomor":                                   KronikiElevenaLocationData("Quests",   756783_030), # Droga Południowa
    
    "Droga Południowa cd. Dom2 - Temmie":                                 KronikiElevenaLocationData("Quests",   756783_031), # Droga Południowa cd.
    "Droga Południowa cd. Dom2 - Armor":                                  KronikiElevenaLocationData("Quests",   756783_032),
    
    "Zakazane bezdroża - Skrzynia1":                                      KronikiElevenaLocationData("General",   756783_033),
    "Zakazane bezdroża - Skrzynia2":                                      KronikiElevenaLocationData("General",   756783_034),
    
    "Jaskinia złych snów - Śmierć":                                       KronikiElevenaLocationData("Quests",   756783_035),
    "Jaskinia północ - Krótkofalówka":                                    KronikiElevenaLocationData("Quests",   756783_036),
    "Jaskinia północ - Siekiera":                                         KronikiElevenaLocationData("Quests",   756783_037),
    "Jaskinia północ - Skrzynia1":                                        KronikiElevenaLocationData("General",   756783_038),
    "Jaskinia północ - Skrzynni2":                                        KronikiElevenaLocationData("General",   756783_039),
    "Jaskinia północ - Klucz":                                            KronikiElevenaLocationData("Quests",   756783_040),
    "Jaskinia północ - Robopirat":                                        KronikiElevenaLocationData("Quests",   756783_041),
    "Jaskinia Left - Tajemnicza część":                                   KronikiElevenaLocationData("Quests",   756783_042),
    "Jaskinia treasure chamber - Diament":                                KronikiElevenaLocationData("Quests",   756783_043),
    
        
    
    "Tęczowa Kraina - Postać":                                              KronikiElevenaLocationData("Quests",   756783_044),
    
    "Droga zachodnia 1 - Walka":                                           KronikiElevenaLocationData("General",   756783_045), # Droga zachodnia (1)
    
    
    
    "Nawiedzone domostwo - Switch do drzwi FNaF":                         KronikiElevenaLocationData("Quests",    756783_200), # Droga zachodnia (2)
    "Lokalizacja FNAF - Pomidor":                                         KronikiElevenaLocationData("General",    756783_201), # Droga zachodnia (2)
    "Lokalizacja FNAF - Doggo":                                           KronikiElevenaLocationData("Quests",    756783_202), # Droga zachodnia (2)
    "Nawiedzone domostwo - Temmie":                                       KronikiElevenaLocationData("Quests",    756783_203), # Droga zachodnia (2)
    
    # Ładunki mocy
    **{f"Ładunki mocy {i+1}":                                             KronikiElevenaLocationData("Healing",  756783_600 + i) for i in range(0, 1)},
    
    
    
    
    
    
    
    
    
    
    
    # Quests
    
    #"Restrooms - Turn in Bonnie's Head Voucher":                          KronikiElevenaLocationData("Quests",   756783_006),

    # Trade-Ins
    #"Dining Area - Trade Alpha Voucher":                                  KronikiElevenaLocationData("Trade",   756783_009),
    #"Dining Area - Trade Spades Voucher":                                 KronikiElevenaLocationData("TradeIW",   756783_013),
    
    
    #Interior Walls
    #"Interior Walls - Chest 1":                                           KronikiElevenaLocationData("Walls",   756783_017),
    
    
    # Bosses
    #"Show Stage - Toy Freddy":                                            KronikiElevenaLocationData("Boss",   756783_046),
    #"Interior Walls - ???":                                               KronikiElevenaLocationData("Walls",   756783_051),
    #"Office - Golden Freddy":                                             KronikiElevenaLocationData("Boss",   756783_052),
   
    # Shops
    #"Backroom BB - Item 1":                                               KronikiElevenaLocationData("BackroomBB",   756783_053),
    #"Restrooms BB - Item 1":                                              KronikiElevenaLocationData("RestroomsBB",   756783_059),
    #"Supply Closet BB - Item 1":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_067),
    #"East Hall Corner BB - Item 1":                                       KronikiElevenaLocationData("EastHallBB",   756783_077),

   
    # Cameras
    #"Show Stage - Camera":                                                  KronikiElevenaLocationData("Cameras",   756783_089),

    #"Backroom - Alpha Party Hat":                                           KronikiElevenaLocationData("PartyHats",    756783_099),
    
    # Levels
    #**{f"Freddy - Level {i+1}":                                             KronikiElevenaLocationData("Levelsanity",  756783_110 + i) for i in range(0, 99)}
} 
