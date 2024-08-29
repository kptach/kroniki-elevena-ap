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
    "Dom Elevena (gra) - karta1":                                         KronikiElevenaLocationData("General",   756783_004),
    "Dom Elevena (gra) - karta2":                                         KronikiElevenaLocationData("General",   756783_005),
    "Dom Elevena (gra) - karta3":                                         KronikiElevenaLocationData("General",   756783_006),
    "Dom Elevena - List":                                                 KronikiElevenaLocationData("Quests",   756783_007),
    
    "Jaskinia zagłady - Skrzynia1":                                       KronikiElevenaLocationData("General",   756783_008),
    "Jaskinia zagłady - Skrzynia2":                                       KronikiElevenaLocationData("General",   756783_009),

    "Pierwsze miasto Dom 5 - grzyby (Chlebek)":                           KronikiElevenaLocationData("Quests",   756783_010),
    "Pierwsze miasto Dom 5 - grzyby (Galaretka)":                         KronikiElevenaLocationData("Quests",   756783_011),
    "Pierwsze miasto Dom 5 - grzyby (Slender)":                           KronikiElevenaLocationData("Quests",   756783_012),
    "Pierwsze miasto Dom 5 - grzyby (Worms)":                             KronikiElevenaLocationData("Quests",   756783_013),
    "Pierwsze miasto Dom 5 - grzyby (Spooky)":                            KronikiElevenaLocationData("Quests",   756783_014),
    "Pierwsze miasto Dom 5 - grzyby (Sos grzybowy)":                      KronikiElevenaLocationData("Quests",   756783_015),
    
    "Dom Elevena (gra) - jedzenie1":                                      KronikiElevenaLocationData("General",   756783_016),
    "Dom Elevena (gra) - jedzenie2":                                      KronikiElevenaLocationData("General",   756783_017),
    "Dom Elevena (gra) - jedzenie3":                                      KronikiElevenaLocationData("General",   756783_018),
    "Dom Elevena (gra) - jedzenie4":                                      KronikiElevenaLocationData("General",   756783_019),
    "Dom Elevena (gra) - jedzenie5":                                      KronikiElevenaLocationData("General",   756783_020),
    "Dom Elevena (gra) - jedzenie6":                                      KronikiElevenaLocationData("General",   756783_021),
    "Dom Elevena (gra) - jedzenie7":                                      KronikiElevenaLocationData("General",   756783_022),
    "Dom Elevena (gra) - jedzenie8":                                      KronikiElevenaLocationData("General",   756783_023),
    "Dom Elevena (gra) - jedzenie9":                                      KronikiElevenaLocationData("General",   756783_024),
    "Dom Elevena (gra) - jedzenie10":                                     KronikiElevenaLocationData("General",   756783_025),
    
    "Jaskinia zagłady - Skrzynia3":                                       KronikiElevenaLocationData("General",   756783_026),
    
    "Nawiedzone domostwo - Switch do drzwi FNaF":                         KronikiElevenaLocationData("Quests",    756783_200), # Droga zachodnia (2)
    "Lokalizacja FNAF - Pomidor":                                         KronikiElevenaLocationData("General",    756783_201), # Droga zachodnia (2)
    "Lokalizacja FNAF - Doggo":                                           KronikiElevenaLocationData("Quests",    756783_202), # Droga zachodnia (2)
    "Nawiedzone domostwo - Temmie":                                       KronikiElevenaLocationData("Quests",    756783_203), # Droga zachodnia (2)
    
    
    
    
    
    
    
    
    
    
    
    
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
