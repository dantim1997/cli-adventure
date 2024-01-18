import json
import color

class room:
    currentroom = []
    player = []
    json_file = ""

    def do_action():
        print("what you want to do?")
        room.get_action(input())

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
                for item in room.currentroom["items"]:
                    print(item)

            elif(action[1] == "at"):
                try:
                    print(room.currentroom["items"][action[2]]["description"])
                except:
                    print(action[2]+" can not be found")
        
        # inventory
        elif(action[0] == "inventory"):
            if(len(action) == 1 ):
                print("you have the following items:")
                for item in room.player["items"]:
                    print(item)
        
        #take
        elif(action[0] == "take"):
            if(len(action) == 1 ):
                print("what you like to take?")
                for item in room.currentroom["items"]:
                    print(item)
            elif(len(action) == 2):
                try:
                    for item in room.currentroom["items"]:
                        print(item)
                        if(action[1] == item):
                           room.player["items"][action[1]] = item
                    print(room.currentroom["items"][action[2]]["description"])
                except:
                    print(action[1]+" can not be found")
        # use
                    
        # walk
        elif(action[0] == "walk"):
            if(len(action) == 1 ):
                print("you can walk the following ways:")
                for item in room.currentroom["routes"]:
                    print(item)

            elif(action[1] == "to"):
                try:
                    print(room.currentroom["routes"][action[2]])
                    to_room =room.currentroom["routes"][action[2]["location"]]
                    print(to_room)
                    if(room.currentroom["routes"][action[2]["is_locked"]] == True):
                        room.load_game(to_room)
                    else:
                        print("this way is locked")
                except:
                    print(action[2]+" can not be found")

        print()
        room.do_action()

    def load_game(location):
        f = open(room.json_file + "room.json")
        data = json.load(f)
        # Closing file
        f.close()
        for i in data['rooms']:
            if i["roomID"] == location:
                room.currentroom = i
        print(room.currentroom["description"])
    
    def load_player():
        f = open(room.json_file+ "player.json")
        data = json.load(f)
        # Closing file
        f.close()
        room.player = data

    def game(json_location):
        print("start")
        room.json_file = json_location
        room.load_game(1)
        room.load_player()
        room.do_action()