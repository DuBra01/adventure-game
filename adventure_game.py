# This script is a text-based adventure game where the player searches for a legendary treasure.

# Task 1: simple print to confirm setup works
print("Game is starting...")

player_name = ""


def play_again():
    print("\nGame ended.")
    print("If you want to play again, type 'yes'")
    print("If you want to exit, type 'exit'")

    while True:
        choice = input("> ").lower().strip()

        if choice == "yes":
            print(f"\nHi {player_name}, you like adventure!")
            print("Good you're back — have luck this time!\n")
            start_game()
            break
        elif choice == "exit":
            print("\nThanks for playing. Goodbye!")
            print("To start the game again, run:")
            print("python3 adventure_game.py\n")
            break
        else:
            print("Please type 'yes' to play again or 'exit' to quit.")


def forest_path():
    print("\nYou enter a dark, creepy forest...")
    print("The trees are tall and block the sunlight.")
    print("Strange noises echo around you, and the air feels cold.")

    print("\nWhat do you do first?")
    print("1. Cross a river")
    print("2. Climb a tree")
    print("3. Climb a hill")
    print("4. Fight with snakes")
    print("5. Fight with bears")

    choice = input("> ").lower().strip()

    if choice == "1" or choice == "cross a river":
        print("\nYou try to cross the river.")
        print("The current is strong, but you manage to reach the other side.")
        print("You are tired, but you find an old map on the ground.")
        print("The map points toward a cave.")
        cave_path()

    elif choice == "2" or choice == "climb a tree":
        print("\nYou climb a tree and look around.")
        print("From the top, you spot smoke rising near a cave entrance.")
        print("You carefully climb down and head toward the cave.")
        cave_path()

    elif choice == "3" or choice == "climb a hill":
        print("\nYou climb a hill and see the land stretching before you.")
        print("In the distance, you notice a hidden cave glowing faintly.")
        print("You follow the trail down to the cave.")
        cave_path()

    elif choice == "4" or choice == "fight with snakes":
        print("\nYou attack the snakes, but there are too many.")
        print("You are overwhelmed. Game over.")
        play_again()

    elif choice == "5" or choice == "fight with bears":
        print("\nYou challenge a bear.")
        print("That was a terrible idea. Game over.")
        play_again()

    else:
        print("\nInvalid choice. You get lost in the forest. Game over.")
        play_again()


def cave_path():
    print("\nThe cave is cold, dark, and silent...")
    print("Water drips from the walls, and the air feels heavy.")

    print("\nWhat do you do?")
    print("1. Light a torch")
    print("2. Proceed in the dark")

    choice = input("> ").lower().strip()

    if choice == "1" or choice == "light a torch":
        print("\nYou light a torch.")
        print("The flame reveals ancient symbols on the walls and a narrow stone path.")

        print("\nYou move deeper into the cave and find two final options:")
        print("1. Open the treasure chamber")
        print("2. Touch a strange glowing stone")

        final_choice = input("> ").lower().strip()

        if final_choice == "1" or final_choice == "open the treasure chamber":
            print("\nYou open the chamber and discover the legendary treasure. You win!")
            play_again()
        elif final_choice == "2" or final_choice == "touch a strange glowing stone":
            print("\nThe stone triggers a trap. The cave collapses. Game over.")
            play_again()
        else:
            print("\nInvalid choice. You slip in the cave and the adventure ends.")
            play_again()

    elif choice == "2" or choice == "proceed in the dark":
        print("\nYou walk forward in complete darkness.")
        print("You fall into a hidden pit. Game over.")
        play_again()

    else:
        print("\nInvalid choice. You get lost in the cave. Game over.")
        play_again()


def start_game():
    global player_name

    print("\nWelcome to the Adventure Game!")
    print("You are an explorer on a quest to find a legendary treasure hidden in an ancient land.")
    print("Your journey will be filled with challenges and decisions that will shape your destiny.")

    if player_name == "":
        player_name = input("\nWhat is your name, explorer? ").strip()
        print(f"\nHello, {player_name}!")
        print("Your quest begins now.")
    else:
        print(f"\nWelcome back, {player_name}!")
        print("Have fun in your next adventure!")

    print("\nAre you ready to begin your adventure? (yes/no)")
    ready = input("> ").lower().strip()

    if ready in ["yes", "y"]:
        pass
    elif ready in ["no", "n"]:
        print("Maybe next time! Goodbye.")
        return
    else:
        print("Invalid input. Please answer with yes/y or no/n.")
        start_game()
        return

    print("\nYou stand before two possible paths:")
    print("1. Enter the dark forest")
    print("2. Enter the mysterious cave")
    print("What do you choose? (forest/cave)")

    choice = input("> ").lower().strip()

    if choice == "1" or choice == "forest":
        print(f"\n{player_name}, you step into the dark forest...")
        forest_path()
    elif choice == "2" or choice == "cave":
        print(f"\n{player_name}, you enter the mysterious cave...")
        cave_path()
    else:
        print("\nInvalid choice. Please restart the game.")
        play_again()


# Start the game
start_game()