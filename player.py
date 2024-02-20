from base_item import base_item
from room_map import Item


class Player:

    def __init__(self, data):
        self.items = []  # Initialize items as an empty list
        self.health = 0

        if "items" in data:
            # Iterate over the items in the data and create Item instances
            for item_name, item_data in data["items"].items():
                item_instance = Item(item_data)
                # Add the Item instance to the list
                self.items.append(item_instance)

        if "health" in data:
            self.health = data["health"]

    def add_item(self, item):
        # Add the provided item to the items list
        self.items.append(item)
