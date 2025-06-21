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
    "Pierwsze miasto Dom1 - Skrzynia":                                    KronikiElevenaLocationData("General",   213700_000),
    "Pierwsze miasto Dom4 - Skrzynia":                                    KronikiElevenaLocationData("General",   213700_001),
    "Pierwsze miasto Wodospad - Złoty Muchomor":                          KronikiElevenaLocationData("Quests",   213700_002),
    "Cyberświat - parnter":                                               KronikiElevenaLocationData("Quests",   213700_003),
    "Dom Elevena (gra) - karty":                                          KronikiElevenaLocationData("General",   213700_004),

    "Dom Elevena - List":                                                 KronikiElevenaLocationData("Quests",   213700_005),
    
    "Jaskinia zagłady - Skrzynia1":                                       KronikiElevenaLocationData("General",   213700_008),
    "Jaskinia zagłady - Skrzynia2":                                       KronikiElevenaLocationData("General",   213700_009),

    "Pierwsze miasto Dom 5 - grzyby (Chlebek)":                           KronikiElevenaLocationData("Quests",   213700_010),
    "Pierwsze miasto Dom 5 - grzyby (Galaretka)":                         KronikiElevenaLocationData("Quests",   213700_011),
    "Pierwsze miasto Dom 5 - grzyby (Slender)":                           KronikiElevenaLocationData("Quests",   213700_012),
    "Pierwsze miasto Dom 5 - grzyby (Worms)":                             KronikiElevenaLocationData("Quests",   213700_013),
    "Pierwsze miasto Dom 5 - grzyby (Spooky)":                            KronikiElevenaLocationData("Quests",   213700_014),
    "Pierwsze miasto Dom 5 - grzyby (Sos grzybowy)":                      KronikiElevenaLocationData("Quests",   213700_015),
    
    "Dom Elevena (gra) - Jedzenie":                                       KronikiElevenaLocationData("General",   213700_016),
    "Droga Południowa - Walka":                                           KronikiElevenaLocationData("General",   213700_017), # Droga Południowa

    
    "Jaskinia zagłady - Skrzynia3":                                       KronikiElevenaLocationData("General",   213700_026),
    
    "Dom Teda - Wyposażenie":                                             KronikiElevenaLocationData("Quests",   213700_027),

    
    "Sekret na prawo - Złoty Muchomor":                                   KronikiElevenaLocationData("Quests",   213700_030), # Droga Południowa
    
    "Droga Południowa cd. Dom2 - Temmie":                                 KronikiElevenaLocationData("Quests",   213700_031), # Droga Południowa cd.
    "Droga Południowa cd. Dom2 - Armor":                                  KronikiElevenaLocationData("Quests",   213700_032),
    
    "Zakazane bezdroża - Skrzynia1":                                      KronikiElevenaLocationData("General",   213700_033),
    "Zakazane bezdroża - Skrzynia2":                                      KronikiElevenaLocationData("General",   213700_034),
    
    "Jaskinia złych snów - Śmierć":                                       KronikiElevenaLocationData("Quests",   213700_035),
    "Jaskinia północ - Krótkofalówka":                                    KronikiElevenaLocationData("Quests",   213700_036),
    "Jaskinia północ - Siekiera":                                         KronikiElevenaLocationData("Quests",   213700_037),
    "Jaskinia północ - Skrzynia1":                                        KronikiElevenaLocationData("General",   213700_038),
    "Jaskinia północ - Skrzynni2":                                        KronikiElevenaLocationData("General",   213700_039),
    "Jaskinia północ - Klucz":                                            KronikiElevenaLocationData("Quests",   213700_040),
    "Jaskinia północ - Robopirat":                                        KronikiElevenaLocationData("Quests",   213700_041),
    "Jaskinia Left - Tajemnicza część":                                   KronikiElevenaLocationData("Quests",   213700_042),
    "Jaskinia treasure chamber - Diament":                                KronikiElevenaLocationData("Quests",   213700_043),
    
        
    
    "Tęczowa Kraina - Postać":                                              KronikiElevenaLocationData("Quests",   213700_044),
    
    "Droga zachodnia 1 - Walka":                                           KronikiElevenaLocationData("General",   213700_045), # Droga zachodnia (1)
    
    
    
    "Nawiedzone domostwo - Switch do drzwi FNaF":                         KronikiElevenaLocationData("Quests",    213700_200), # Droga zachodnia (2)
    "Lokalizacja FNAF - Pomidor":                                         KronikiElevenaLocationData("General",    213700_201), # Droga zachodnia (2)
    "Lokalizacja FNAF - Doggo":                                           KronikiElevenaLocationData("Quests",    213700_202), # Droga zachodnia (2)
    "Nawiedzone domostwo - Temmie":                                       KronikiElevenaLocationData("Quests",    213700_203), # Droga zachodnia (2)
    
    # Ładunki mocy
    **{f"Ładunki mocy {i+1}":                                             KronikiElevenaLocationData("Healing",  213700_600 + i) for i in range(0, 1)},
    
    
    
    
    
    
    
    
    
    
    
    # Quests
    
    #"Restrooms - Turn in Bonnie's Head Voucher":                          KronikiElevenaLocationData("Quests",   213700_006),

    # Trade-Ins
    #"Dining Area - Trade Alpha Voucher":                                  KronikiElevenaLocationData("Trade",   213700_009),
    #"Dining Area - Trade Spades Voucher":                                 KronikiElevenaLocationData("TradeIW",   213700_013),
    
    
    #Interior Walls
    #"Interior Walls - Chest 1":                                           KronikiElevenaLocationData("Walls",   213700_017),
    
    
    # Bosses
    #"Show Stage - Toy Freddy":                                            KronikiElevenaLocationData("Boss",   213700_046),
    #"Interior Walls - ???":                                               KronikiElevenaLocationData("Walls",   213700_051),
    #"Office - Golden Freddy":                                             KronikiElevenaLocationData("Boss",   213700_052),
   
    # Shops
    #"Backroom BB - Item 1":                                               KronikiElevenaLocationData("BackroomBB",   213700_053),
    #"Restrooms BB - Item 1":                                              KronikiElevenaLocationData("RestroomsBB",   213700_059),
    #"Supply Closet BB - Item 1":                                          KronikiElevenaLocationData("SupplyClosetBB",   213700_067),
    #"East Hall Corner BB - Item 1":                                       KronikiElevenaLocationData("EastHallBB",   213700_077),

   
    # Cameras
    #"Show Stage - Camera":                                                  KronikiElevenaLocationData("Cameras",   213700_089),

    #"Backroom - Alpha Party Hat":                                           KronikiElevenaLocationData("PartyHats",    213700_099),
    
    # Levels
    #**{f"Freddy - Level {i+1}":                                             KronikiElevenaLocationData("Levelsanity",  213700_110 + i) for i in range(0, 99)}
} 
