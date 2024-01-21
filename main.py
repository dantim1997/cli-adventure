from os import listdir
from os.path import isfile, join
import json
from room import room

def main():
    print("Hello World!")
    main_menu()

def main_menu():
    print("Hello, welcome in the main menu, what you like to do?")
    print("1. adventures")
    print("2. look for updates")
    print("3. exit")
    x = int(input())
    if 1 == x:
        adventures()
    elif 2 == x:
        update()
    elif 3 == x:
        exit()
    else: 
        "wrong number"

def adventures():
    print("adventures:")
    dir_path = "./adventures"
    files = listdir(dir_path)
    adventures = []
    counter = 0
    for file in files:
        counter = counter+1
        print(str(counter) +". "+file)
        adventures.append(file)

    print("start by selecting the number")
    number = input()
    room.game("adventures/"+adventures[int(number)-1]+"/")

def update():
    print("updated")
    main_menu()

if __name__ == "__main__":
    main()