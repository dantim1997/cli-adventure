from base_item import base_item


class RoomMap:
    def __init__(self, data):
        self.rooms = []
        if "rooms" in data:
            for room_data in data["rooms"]:
                room = Room(room_data)
                self.rooms.append(room)

class Room:
    def __init__(self, data):
        self.roomID = data.get("roomID", None)
        self.description = data.get("description", "")
        self.routes = {}
        self.items = []

        if "routes" in data:
            self.routes = {direction: Route(route_data) for direction, route_data in data["routes"].items()}

        if "items" in data:
            self.items = {item_name: Item(item_data) for item_name, item_data in data["items"].items()}
        
    def get_route(self, route):
        return self.routes.get(route, None)

    def get_item_info(self, item_name):
        return self.items.get(item_name, None)
    
    def set_item_taken(self, item_name, value):
        item = self.items.get(item_name, None)
        item.taken = value
        return self.items.get(item_name, None)


class Route:
    def __init__(self, data):
        if isinstance(data, int):
            # Handle the case where data is an int
            self.location = data
            self.is_locked = False  # You may want to set a default value
            self.unlock_able = None  # You may want to set a default value
        elif isinstance(data, dict):
            # Handle the case where data is a dictionary
            self.location = data.get("location", None)
            self.is_locked = data.get("is_locked", False)
            self.unlock_able = data.get("unlock_able", None)
        else:
            # Handle other cases as needed
            raise ValueError("Invalid data type for Route")

class Item:
    def __init__(self, data):
        print(data)
        self.description = data.get("description", "")
        self.taken = data.get("taken", False)
