import os
from room_functions import room_functions
version = 0.1


def main():
    print("version:"+version)
    main_menu()

def main_menu():
    print("Hello, welcome to the main menu. What would you like to do?")
    print("1. Adventures")
    print("2. Look for Updates")
    print("3. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        adventures()
    elif choice == '2':
        update()
    elif choice == '3':
        exit_program()
    else:
        print("Invalid input. Please enter a valid number.")
        main_menu()

def adventures():
    print("Adventures:")
    dir_path = "./adventures"
    adventures = [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

    for i, adventure in enumerate(adventures, start=1):
        print(f"{i}. {adventure}")

    selection = input("Start by selecting the number: ")

    try:
        selected_index = int(selection) - 1
        selected_adventure = adventures[selected_index]
        adventure_path = os.path.join(dir_path, selected_adventure)
        adventure_path = adventure_path.replace('\\', '/')
        room_functions.game(adventure_path)
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number.")
        adventures()

def update():
    print("Updated")
    main_menu()

def exit_program():
    print("Exiting the program. Goodbye!")
    # Add any cleanup code if necessary
    exit()

if __name__ == "__main__":
    main()
