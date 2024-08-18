from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class KronikiElevenaLocation(Location):
    game: str = "Five Nights at Fuckboy's"


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
