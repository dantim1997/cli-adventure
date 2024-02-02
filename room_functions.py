import json
import color
import room_map

class room_functions:
    currentroom = room_map.Room
    player = []
    json_file = ""

    def do_action():
        print("what you want to do?")
        room_functions.get_action(input())

    def get_action(actions):
        action = actions.split()
        if(action[0] == "help"):
            print("you can do the following:")
            print("look at")
            print("walk to")
            print("take")
            print("inventory")
        #look
        elif(action[0] == "look"):
            if(len(action) == 1 ):
                print("you see the following items:")
                for item in room_functions.currentroom.items:
                    if(room_functions.currentroom.get_item_info(item).taken == False):
                        print(item)

            elif(action[1] == "at"):
                try:
                    if(room_functions.currentroom.get_item_info(item).taken == False):
                        print(room_functions.currentroom.get_item_info(action[2]).description)
                except:
                    print(action[2]+" can not be found")
        
        # inventory
        elif(action[0] == "inventory"):
            if(len(action) == 1 ):
                print("you have the following items:")
                for item in room_functions.player["items"]:
                    print(item)
        
        #take
        elif(action[0] == "take"):
            if(len(action) == 1 ):
                print("what you like to take?")
                for item in room_functions.currentroom.items:
                    if(room_functions.currentroom.get_item_info(item).taken == False):
                        print(item)
            elif(len(action) == 2):
                try:
                    for item in room_functions.currentroom.items:
                        print(item)
                        if(action[1] == item):
                            room_functions.player["items"][action[1]] = item
                            print(room_functions.currentroom.set_item_taken(item, True).taken)
                except ZeroDivisionError as e:
                    print(action[1]+" can not be found")
                    print(f"Error: {e}")
        # use
        elif(action[0] == "use"):       
            if(len(action) == 1 ):
                print("you can use the following items:")
                for item in room_functions.player["items"]:
                    print(item)
            elif(len(action[1]) == 2):
                print("What do you want to use "+action[1]+"on?")
            elif(action[2] == "on"):
                #TODO
                print("not yet done")
        # walk
        elif(action[0] == "walk"):
            if(len(action) == 1 ):
                print("you can walk the following ways:")
                for item in room_functions.currentroom.routes:
                    print(item)

            elif(action[1] == "to"):
                try:
                    to_room =room_functions.currentroom.get_route(action[2]).location
                    if(room_functions.currentroom.get_route(action[2]).is_locked):
                        print("this way is locked")
                    else:
                        print("walked to " + action[2])
                        room_functions.load_game(to_room)
                except:
                    print(action[2]+" can not be found")
            else:
                print("walk to where?")
        else:
            print()
            print("That action is not available, try help")

        print()
        room_functions.do_action()

    def load_game(location):
        f = open(room_functions.json_file + "/room.json")
        data = json.load(f)
        # Closing file
        f.close()
        map = room_map.RoomMap(data)
        
        for room in map.rooms:
            if room.roomID == location:
                room_functions.currentroom = room
        print(room_functions.currentroom.description)
    
    def load_player():
        f = open(room_functions.json_file+ "/player.json")
        data = json.load(f)
        # Closing file
        f.close()
        room_functions.player = data

    def game(json_location):
        print("start")
        print(json_location)
        room_functions.json_file = json_location
        room_functions.load_game(1)
        room_functions.load_player()
        room_functions.do_action()