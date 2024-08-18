from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region
from .Locations import KronikiElevenaLocation, location_table, get_locations_by_category
from Options import Toggle


class KronikiElevenaRegionData(NamedTuple):
    locations: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, KronikiElevenaRegionData] = {
        "Menu":                         KronikiElevenaRegionData(None),
        
        "Dom Elevena":                  KronikiElevenaRegionData([]),
        
        "Cyberświat - start":                          KronikiElevenaRegionData([]),
        "Cyberświat - klasy":                          KronikiElevenaRegionData([]),
        "Endless corridor":                            KronikiElevenaRegionData([]),
        "Cyberświat - walka":                          KronikiElevenaRegionData([]),
        "Cyberświat - partnerzy":                      KronikiElevenaRegionData([]),

        "Pierwsze miasto":              KronikiElevenaRegionData(["Wodospad 1 - Złoty grzyb"]),

        "Dom Elevena (gra)":            KronikiElevenaRegionData([]),

        "Pierwsze miasto Dom1":                         KronikiElevenaRegionData(["Pierwsze miasto Dom1 - Skrzynia",]),

        "Pierwsze miasto Dom2":                         KronikiElevenaRegionData([]),

        "Pierwsze miasto Dom3":                         KronikiElevenaRegionData(["West Hall - Camera"]),

        "Pierwsze miasto Dom4":                         KronikiElevenaRegionData(["West Hall Corner - Chest",
                                                 "West Hall Corner - Camera"]),

        "Pierwsze miasto Dom 5 - grzyby":               KronikiElevenaRegionData(["East Hall - Camera"]),

        "Pierwsze miasto Dom6":                         KronikiElevenaRegionData(["East Hall Corner - Camera",
                                                 "East Hall Corner - Omega Party Hat"]),
        "Pierwsze miasto Dom7 - Biblioteka Partner":    KronikiElevenaRegionData([]),
        
        "Pierwsze miasto Dom7 - Biblioteka 1P":  KronikiElevenaRegionData([]),
        
        "Pierwsze miasto Dom8 - szaman":  KronikiElevenaRegionData([]),

        "Pierwsze miasto Dom 9 - sklep":            KronikiElevenaRegionData([]),
        
        "Pierwsze miasto Dom 9 - sklep 1F":        KronikiElevenaRegionData([]),
        
        "Jaskinia zagłady":         KronikiElevenaRegionData([]),

        "Dark room":             KronikiElevenaRegionData(["Backroom - Camera",
                                                 "Backroom - Alpha Party Hat",
                                                 "Backroom - Return Bonnie's Head",
                                                 "Backroom - Toy Bonnie",
                                                 "Backroom - Alpha Party Hat"]),

        "Droga Zachodnia(1)":          KronikiElevenaRegionData([]),

        "Namiot":       KronikiElevenaRegionData(["Interior Walls - ???"]),

        "Droga Zachodnia(1) Dom1":               KronikiElevenaRegionData(["Office - Golden Freddy"]),
        
        "Droga Zachodnia(1) Dom2":               KronikiElevenaRegionData(["Office - Golden Freddy"])
        
    }

    # Category hell
    for supplybb in get_locations_by_category("SupplyClosetBB").keys():
        regions["Supply Closet BB"].locations.append(supplybb)
    for cornerbb in get_locations_by_category("EastHallBB").keys():
        regions["East Hall Corner BB"].locations.append(cornerbb)
    for restroomsbb in get_locations_by_category("RestroomsBB").keys():
        regions["Restrooms BB"].locations.append(restroomsbb)
    for backroombb in get_locations_by_category("BackroomBB").keys():
        regions["Backroom BB"].locations.append(backroombb)
    for walls in get_locations_by_category("Walls").keys():
        regions["Interior Walls"].locations.append(walls)
    for voucher in get_locations_by_category("Trade").keys():
        regions["Trade Machine"].locations.append(voucher)
    for voucheriw in get_locations_by_category("TradeIW").keys():
        regions["Trade Machine IW"].locations.append(voucheriw)   
    for levels in get_locations_by_category("Levelsanity").keys():
        regions["Levelsanity"].locations.append(levels)

    for name, data in regions.items():
        if name == "Interior Walls" and multiworld.interior_walls[player] == Toggle.option_false:
            continue
        if name == "Trade Machine IW" and (multiworld.interior_walls[player] == Toggle.option_false or multiworld.trade_quest[player] == Toggle.option_false):
            continue
        if name == "Trade Machine" and multiworld.trade_quest[player] == Toggle.option_false:
            continue
        if name == "Levelsanity" and multiworld.levelsanity[player] == Toggle.option_false:
            continue
        multiworld.regions.append(create_region(multiworld, player, name, data))


def create_region(multiworld: MultiWorld, player: int, name: str, data: KronikiElevenaRegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = KronikiElevenaLocation(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    return region
    
def connect_regions(multiworld: MultiWorld, player: int, source: str, target: List[str], rule=None):
    sourceRegion = multiworld.get_region(source, player)
    targetRegion = multiworld.get_region(target, player)
    sourceRegion.connect(targetRegion, rule=rule)