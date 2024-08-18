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
    "Show Stage - Left Chest":                                            KronikiElevenaLocationData("General",   756783_000),
    "Show Stage - Right Chest":                                           KronikiElevenaLocationData("General",   756783_001),
    "Dining Area - Punch the fuck out of the kitchen door":               KronikiElevenaLocationData("General",   756783_002),
    "West Hall Corner - Chest":                                           KronikiElevenaLocationData("General",   756783_003),
    "Supply Closet - Chest":                                              KronikiElevenaLocationData("General",   756783_004),
    "Restrooms - Chest":                                                  KronikiElevenaLocationData("General",   756783_005),
    # Quests
    "Restrooms - Turn in Bonnie's Head Voucher":                          KronikiElevenaLocationData("Quests",   756783_006),
    "Backroom - Return Bonnie's Head":                                    KronikiElevenaLocationData("Quests",   756783_007),
    "Pirate Cove - Burn the place to the ground":                         KronikiElevenaLocationData("Quests",   756783_008),
    # Trade-Ins
    "Dining Area - Trade Alpha Voucher":                                  KronikiElevenaLocationData("Trade",   756783_009),
    "Dining Area - Trade Beta Voucher":                                   KronikiElevenaLocationData("Trade",   756783_010),
    "Dining Area - Trade Gamma Voucher":                                  KronikiElevenaLocationData("Trade",   756783_011),
    "Dining Area - Trade Omega Voucher":                                  KronikiElevenaLocationData("Trade",   756783_012),
    "Dining Area - Trade Spades Voucher":                                 KronikiElevenaLocationData("TradeIW",   756783_013),
    "Dining Area - Trade Hearts Voucher":                                 KronikiElevenaLocationData("TradeIW",   756783_014),
    "Dining Area - Trade Diamonds Voucher":                               KronikiElevenaLocationData("TradeIW",   756783_015),
    "Dining Area - Trade Clubs Voucher":                                  KronikiElevenaLocationData("TradeIW",   756783_016),
    #Interior Walls
    "Interior Walls - Chest 1":                                           KronikiElevenaLocationData("Walls",   756783_017),
    "Interior Walls - Chest 2":                                           KronikiElevenaLocationData("Walls",   756783_018),
    "Interior Walls - Chest 3":                                           KronikiElevenaLocationData("Walls",   756783_019),
    "Interior Walls - Chest 4":                                           KronikiElevenaLocationData("Walls",   756783_020),
    "Interior Walls - Chest 5":                                           KronikiElevenaLocationData("Walls",   756783_021),
    "Interior Walls - Chest 6":                                           KronikiElevenaLocationData("Walls",   756783_022),
    "Interior Walls - Chest 7":                                           KronikiElevenaLocationData("Walls",   756783_023),
    "Interior Walls - Chest 8":                                           KronikiElevenaLocationData("Walls",   756783_024),
    "Interior Walls - Chest 9":                                           KronikiElevenaLocationData("Walls",   756783_025),
    "Interior Walls - Chest 10":                                          KronikiElevenaLocationData("Walls",   756783_026),
    "Interior Walls - Chest 11":                                          KronikiElevenaLocationData("Walls",   756783_027),
    "Interior Walls - Chest 12":                                          KronikiElevenaLocationData("Walls",   756783_028),
    "Interior Walls - Chest 13":                                          KronikiElevenaLocationData("Walls",   756783_029),
    "Interior Walls - Chest 14":                                          KronikiElevenaLocationData("Walls",   756783_030),
    "Interior Walls - Chest 15":                                          KronikiElevenaLocationData("Walls",   756783_031),
    "Interior Walls - Chest 16":                                          KronikiElevenaLocationData("Walls",   756783_032),
    "Interior Walls - Chest 17":                                          KronikiElevenaLocationData("Walls",   756783_033),
    "Interior Walls - Chest 18":                                          KronikiElevenaLocationData("Walls",   756783_034),
    "Interior Walls - Chest 19":                                          KronikiElevenaLocationData("Walls",   756783_035),
    "Interior Walls - Chest 20":                                          KronikiElevenaLocationData("Walls",   756783_036),
    "Interior Walls - Chest 21":                                          KronikiElevenaLocationData("Walls",   756783_037),
    "Interior Walls - Chest 22":                                          KronikiElevenaLocationData("Walls",   756783_038),
    "Interior Walls - Chest 23":                                          KronikiElevenaLocationData("Walls",   756783_039),
    "Interior Walls - Chest 24":                                          KronikiElevenaLocationData("Walls",   756783_040),
    "Interior Walls - Chest 25":                                          KronikiElevenaLocationData("Walls",   756783_041),
    "Interior Walls - Chest 26":                                          KronikiElevenaLocationData("Walls",   756783_042),
    "Interior Walls - Chest 27":                                          KronikiElevenaLocationData("Walls",   756783_043),
    "Interior Walls - Chest 28":                                          KronikiElevenaLocationData("Walls",   756783_044),
    "Interior Walls - Chest 29":                                          KronikiElevenaLocationData("Walls",   756783_045),
    # Bosses
    "Show Stage - Toy Freddy":                                            KronikiElevenaLocationData("Boss",   756783_046),
    "Backroom - Toy Bonnie":                                              KronikiElevenaLocationData("Boss",   756783_047),
    "Restrooms - Toy Chica":                                              KronikiElevenaLocationData("Boss",   756783_048),
    "Pirate Cove - Mangle":                                               KronikiElevenaLocationData("Boss",   756783_049),
    "The Puppet":                                                         KronikiElevenaLocationData("Boss",   756783_050),
    "Interior Walls - ???":                                               KronikiElevenaLocationData("Walls",   756783_051),
    "Office - Golden Freddy":                                             KronikiElevenaLocationData("Boss",   756783_052),
    # Shops
    "Backroom BB - Item 1":                                               KronikiElevenaLocationData("BackroomBB",   756783_053),
    "Backroom BB - Item 2":                                               KronikiElevenaLocationData("BackroomBB",   756783_054),
    "Backroom BB - Item 3":                                               KronikiElevenaLocationData("BackroomBB",   756783_055),
    "Backroom BB - Item 4":                                               KronikiElevenaLocationData("BackroomBB",   756783_056),
    "Backroom BB - Item 5":                                               KronikiElevenaLocationData("BackroomBB",   756783_057),
    "Backroom BB - Item 6":                                               KronikiElevenaLocationData("BackroomBB",   756783_058),
    "Restrooms BB - Item 1":                                              KronikiElevenaLocationData("RestroomsBB",   756783_059),
    "Restrooms BB - Item 2":                                              KronikiElevenaLocationData("RestroomsBB",   756783_060),
    "Restrooms BB - Item 3":                                              KronikiElevenaLocationData("RestroomsBB",   756783_061),
    "Restrooms BB - Item 4":                                              KronikiElevenaLocationData("RestroomsBB",   756783_062),
    "Restrooms BB - Item 5":                                              KronikiElevenaLocationData("RestroomsBB",   756783_063),
    "Restrooms BB - Item 6":                                              KronikiElevenaLocationData("RestroomsBB",   756783_064),
    "Restrooms BB - Item 7":                                              KronikiElevenaLocationData("RestroomsBB",   756783_065),
    "Restrooms BB - Item 8":                                              KronikiElevenaLocationData("RestroomsBB",   756783_066),
    "Supply Closet BB - Item 1":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_067),
    "Supply Closet BB - Item 2":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_068),
    "Supply Closet BB - Item 3":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_069),
    "Supply Closet BB - Item 4":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_070),
    "Supply Closet BB - Item 5":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_071),
    "Supply Closet BB - Item 6":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_072),
    "Supply Closet BB - Item 7":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_073),
    "Supply Closet BB - Item 8":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_074),
    "Supply Closet BB - Item 9":                                          KronikiElevenaLocationData("SupplyClosetBB",   756783_075),
    "Supply Closet BB - Item 10":                                         KronikiElevenaLocationData("SupplyClosetBB",   756783_076),
    "East Hall Corner BB - Item 1":                                       KronikiElevenaLocationData("EastHallBB",   756783_077),
    "East Hall Corner BB - Item 2":                                       KronikiElevenaLocationData("EastHallBB",   756783_078),
    "East Hall Corner BB - Item 3":                                       KronikiElevenaLocationData("EastHallBB",   756783_079),
    "East Hall Corner BB - Item 4":                                       KronikiElevenaLocationData("EastHallBB",   756783_080),
    "East Hall Corner BB - Item 5":                                       KronikiElevenaLocationData("EastHallBB",   756783_081),
    "East Hall Corner BB - Item 6":                                       KronikiElevenaLocationData("EastHallBB",   756783_082),
    "East Hall Corner BB - Item 7":                                       KronikiElevenaLocationData("EastHallBB",   756783_083),
    "East Hall Corner BB - Item 8":                                       KronikiElevenaLocationData("EastHallBB",   756783_084),
    "East Hall Corner BB - Item 9":                                       KronikiElevenaLocationData("EastHallBB",   756783_085),
    "East Hall Corner BB - Item 10":                                      KronikiElevenaLocationData("EastHallBB",   756783_086),
    "East Hall Corner BB - Item 11":                                      KronikiElevenaLocationData("EastHallBB",   756783_087),
    "East Hall Corner BB - Item 12":                                      KronikiElevenaLocationData("EastHallBB",   756783_088),
    # Cameras
    "Show Stage - Camera":                                                  KronikiElevenaLocationData("Cameras",   756783_089),
    "Dining Area - Camera":                                                 KronikiElevenaLocationData("Cameras",   756783_090),
    "Backroom - Camera":                                                    KronikiElevenaLocationData("Cameras",   756783_091),
    "West Hall - Camera":                                                   KronikiElevenaLocationData("Cameras",   756783_092),
    "East Hall - Camera":                                                   KronikiElevenaLocationData("Cameras",   756783_093),
    "Restrooms - Camera":                                                   KronikiElevenaLocationData("Cameras",   756783_094),
    "Pirate Cove - Camera":                                                 KronikiElevenaLocationData("Cameras",   756783_095),
    "Supply Closet - Camera":                                               KronikiElevenaLocationData("Cameras",   756783_096),
    "East Hall Corner - Camera":                                            KronikiElevenaLocationData("Cameras",   756783_097),
    "West Hall Corner - Camera":                                            KronikiElevenaLocationData("Cameras",   756783_098),
    # Party Hats
    "Backroom - Alpha Party Hat":                                           KronikiElevenaLocationData("PartyHats",    756783_099),
    "Restrooms - Beta Party Hat":                                           KronikiElevenaLocationData("PartyHats",    756783_100),
    "Supply Closet - Gamma Party Hat":                                      KronikiElevenaLocationData("PartyHats",    756783_101),
    "East Hall Corner - Omega Party Hat":                                   KronikiElevenaLocationData("PartyHats",    756783_102),
    # Whoops I forgot this one
    "Kitchen - Chica":                                                      KronikiElevenaLocationData("General",      756783_103),
    # Levels
    **{f"Freddy - Level {i+1}":                                             KronikiElevenaLocationData("Levelsanity",  756783_110 + i) for i in range(0, 20)},
    **{f"Bonnie - Level {i+1}":                                             KronikiElevenaLocationData("Levelsanity",  756783_140 + i) for i in range(0, 20)},
    **{f"Chica - Level {i+1}":                                              KronikiElevenaLocationData("Levelsanity",  756783_170 + i) for i in range(0, 20)},
    **{f"Foxy - Level {i+1}":                                               KronikiElevenaLocationData("Levelsanity",  756783_200 + i) for i in range(0, 20)}
}
