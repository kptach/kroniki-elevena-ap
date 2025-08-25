from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region
from .Locations import KronikiElevenaLocation, location_table, get_locations_by_category
from Options import Toggle


class KronikiElevenaRegionData(NamedTuple):
    locations: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, KronikiElevenaRegionData] = {
        "Menu":                                         KronikiElevenaRegionData(None),
        
        "Dom Elevena":                                  KronikiElevenaRegionData(["Dom Elevena - List"]),
        
        "Cyberświat - klasy":                           KronikiElevenaRegionData([]),
        "Cyberświat - walka":                           KronikiElevenaRegionData([]),
        "Cyberświat - partnerzy":                       KronikiElevenaRegionData(["Cyberświat - parnter"]),

        "Eleven Level":                                 KronikiElevenaRegionData([]),
        
        "Papyrus Level":                                KronikiElevenaRegionData([]), 

        "Serek Level":                                  KronikiElevenaRegionData([]),

        "Pierwsze miasto":                              KronikiElevenaRegionData(["Pierwsze miasto Wodospad - Złoty Muchomor"]),

        "Dom Elevena (gra)":                            KronikiElevenaRegionData(["Dom Elevena (gra) - karty",
                                                                                  "Dom Elevena (gra) - jedzenie"]),

        "Pierwsze miasto Dom1":                         KronikiElevenaRegionData(["Pierwsze miasto Dom1 - Skrzynia"]),

        "Pierwsze miasto Dom4":                         KronikiElevenaRegionData(["Pierwsze miasto Dom4 - Skrzynia"]),

        "Pierwsze miasto Dom 5 - grzyby":               KronikiElevenaRegionData(["Pierwsze miasto Dom 5 - grzyby (Chlebek)",
                                                                                  "Pierwsze miasto Dom 5 - grzyby (Galaretka)",
                                                                                  "Pierwsze miasto Dom 5 - grzyby (Slender)",
                                                                                  "Pierwsze miasto Dom 5 - grzyby (Worms)",
                                                                                  "Pierwsze miasto Dom 5 - grzyby (Spooky)",
                                                                                  "Pierwsze miasto Dom 5 - grzyby (Sos grzybowy)"]),
        
        "Pierwsze miasto Dom 9 - sklep":                KronikiElevenaRegionData([]),
        "Pierwsze miasto Dom 9 - sklep 1F":             KronikiElevenaRegionData([]),
        
        "Jaskinia zagłady":                             KronikiElevenaRegionData(["Jaskinia zagłady - Skrzynia1",
                                                                                  "Jaskinia zagłady - Skrzynia2",
                                                                                  "Jaskinia zagłady - Skrzynia3"]),
        
        
        #"Droga Zachodnia(1)":                           KronikiElevenaRegionData([]),
        #"Droga Zachodnia(2)":                           KronikiElevenaRegionData([]),
        "Droga połódniowa":                             KronikiElevenaRegionData(["Droga Południowa - Walka",
                                                                                  "Sekret na prawo - Złoty Muchomor",
                                                                                  "Dom Teda - Wyposażenie"]),
        
        "Droga połódniowa cd.":                         KronikiElevenaRegionData(["Droga Południowa cd. Dom2 - Temmie",
                                                                                  "Droga Południowa cd. Dom2 - Armor"]),
        "Zakazane bezdroża":                            KronikiElevenaRegionData(["Zakazane bezdroża - Skrzynia1",
                                                                                  "Zakazane bezdroża - Skrzynia2"]),
        
        "Tęczowa Kraina":                           KronikiElevenaRegionData(["Tęczowa Kraina - Postać"]),
        
        "Jaskinia złych snów":                            KronikiElevenaRegionData([    "Jaskinia złych snów - Śmierć",
                                                                                        "Jaskinia północ - Krótkofalówka",
                                                                                        "Jaskinia północ - Siekiera",
                                                                                        "Jaskinia północ - Skrzynia1",
                                                                                        "Jaskinia północ - Skrzynni2",
                                                                                        "Jaskinia północ - Klucz",
                                                                                        "Jaskinia północ - Robopirat",
                                                                                        "Jaskinia treasure chamber - Diament"]),
        "Jaskinia Left":                           KronikiElevenaRegionData(["Jaskinia Left - Tajemnicza część"]),
        
        "Droga zachodnia(1)":                           KronikiElevenaRegionData(["Droga zachodnia 1 - Walka"]),
        "Droga zachodnia(2)":                           KronikiElevenaRegionData([]),
        # #"Droga zachodnia(2) Dom Bestingtonów":                           KronikiElevenaRegionData([]),
        "Droga zachodnia(2) Nawiedzone domostwo":       KronikiElevenaRegionData(["Nawiedzone domostwo - Switch do drzwi FNaF",
                                                                                  "Nawiedzone domostwo - Temmie"]),
        
        "Droga zachodnia(2) Lokalizacja FNAF":          KronikiElevenaRegionData(["Lokalizacja FNAF - Pomidor",
                                                                                  "Lokalizacja FNAF - Doggo"]),
        
        "Nieskończony las":                             KronikiElevenaRegionData(["Nieskończony las - Temmie",
                                                                                  "Nieskończony las - Skrzynia",
                                                                                    "Nieskończony las - Jad"])
        
        

        # "Pierwsze miasto Dom6":                         KronikiElevenaRegionData([]),
        
        # "Pierwsze miasto Dom7 - Biblioteka Partner":    KronikiElevenaRegionData([]),
        
        # "Pierwsze miasto Dom7 - Biblioteka 1P":         KronikiElevenaRegionData([]),
        
        # "Pierwsze miasto Dom8 - szaman":                KronikiElevenaRegionData([]),

        # "Pierwsze miasto Dom 9 - sklep":                KronikiElevenaRegionData([]),
        
        # "Pierwsze miasto Dom 9 - sklep 1F":             KronikiElevenaRegionData([]),
        
        # "Jaskinia zagłady":                             KronikiElevenaRegionData([]),

        # "Dark room":                                    KronikiElevenaRegionData([]),

        # "Droga Zachodnia(1)":                           KronikiElevenaRegionData([]),

        # "Droga Zachodnia(1) Namiot":                    KronikiElevenaRegionData([]),

        # "Droga Zachodnia(1) Dom1":                      KronikiElevenaRegionData([]),
        
        # "Droga Zachodnia(1) Dom2":                      KronikiElevenaRegionData([])
        
    }

    # Category hell
    # for supplybb in get_locations_by_category("SupplyClosetBB").keys():
    #     regions["Supply Closet BB"].locations.append(supplybb)
    # for cornerbb in get_locations_by_category("EastHallBB").keys():
    #     regions["East Hall Corner BB"].locations.append(cornerbb)
    # for restroomsbb in get_locations_by_category("RestroomsBB").keys():
    #     regions["Restrooms BB"].locations.append(restroomsbb)
    # for backroombb in get_locations_by_category("BackroomBB").keys():
    #     regions["Backroom BB"].locations.append(backroombb)
    # for walls in get_locations_by_category("Walls").keys():
    #     regions["Interior Walls"].locations.append(walls)
    # for voucher in get_locations_by_category("Trade").keys():
    #     regions["Trade Machine"].locations.append(voucher)
    # for voucheriw in get_locations_by_category("TradeIW").keys():
    #     regions["Trade Machine IW"].locations.append(voucheriw)   
    # for levels in get_locations_by_category("Levelsanity").keys():
    #     regions["Levelsanity"].locations.append(levels)

    for name, data in regions.items():
    #     if name == "Interior Walls" and multiworld.interior_walls[player] == Toggle.option_false:
    #         continue
    #     if name == "Trade Machine IW" and (multiworld.interior_walls[player] == Toggle.option_false or multiworld.trade_quest[player] == Toggle.option_false):
    #         continue
    #     if name == "Trade Machine" and multiworld.trade_quest[player] == Toggle.option_false:
    #         continue
    #     if name == "Levelsanity" and multiworld.levelsanity[player] == Toggle.option_false:
    #         continue
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