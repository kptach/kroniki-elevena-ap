from typing import List

from BaseClasses import Tutorial, Location, LocationProgressType, CollectionState, MultiWorld, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import KronikiElevenaItem, KronikiElevenaItemData, get_items_by_category, item_table
from .Locations import KronikiElevenaLocation, location_table
from .Options import kroniki_elevena_options
from .Regions import create_regions
from .Rules import set_rules


class KronikiElevenaWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Kroniki Elevena client for use with Archipelago.",
        "English",
        "kronikielevena_en.md",
        "kronkikelevena/en",
        ["fredzio2006"]
    )]


class KronikiElevenaWorld(World):
    """
    Kroniki Elevena is an RPG game made for Polish youtuber called Eleven and written in's written in Polish.
    """
    game = "Kroniki Elevena"
    option_definitions = kroniki_elevena_options
    topology_present = True
    data_version = 4
    required_client_version = (0, 5, 0)
    web = KronikiElevenaWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        return {option_name: self.get_setting(option_name).value for option_name in kroniki_elevena_options}

    def create_items(self):
        item_pool: List[KronikiElevenaItem] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for name, data in item_table.items():
            quantity = data.max_quantity
            category = data.category
            classification = data.classification
            """
            # Ignore Interior Walls if it's not enabled.
            if name == "Reveal Interior Walls" and not self.get_setting("interior_walls"):
                continue

            # Remove one of each weapon type if Interior Walls is not active
            if name == "Progressive Microphone" and not self.get_setting("interior_walls"):
                quantity -= 1
            if name == "Progressive Guitar" and not self.get_setting("interior_walls"):
                quantity -= 1
            if name == "Progressive Cupcakes" and not self.get_setting("interior_walls"):
                quantity -= 1
            if name == "Progressive Hook" and not self.get_setting("interior_walls"):
                quantity -= 1
            if name == "Dragon ..." and not self.get_setting("interior_walls"):
                continue
            
            # Remove more unneccessary items when Interior Walls/Trade Quest is not active to make room for filler
            if category == "Armor" and classification == ItemClassification.useful and not self.get_setting("interior_walls"):
                continue
            if name == "Fazbear Combo" and not self.get_setting("trade_quest"):
                continue
            if name == "Flighty Combo" and not self.get_setting("trade_quest"):
                continue
            if name == "Bonbon Combo" and not self.get_setting("trade_quest"):
                continue
            if name == "Pirate Combo" and not self.get_setting("trade_quest"):
                continue
            if name == "Fearless Flight" and not self.get_setting("interior_walls"):
                continue
            if name == "Speed Share" and not self.get_setting("interior_walls"):
                continue

            # Ignore filler, it will be added in a later stage.
            if data.category == "Filler":
                continue
            """

            item_pool += [self.create_item(name) for _ in range(0, quantity)]


        self.multiworld.itempool += item_pool

    def create_item(self, name: str) -> KronikiElevenaItem:
        data = item_table[name]
        return KronikiElevenaItem(name, data.classification, data.code, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)