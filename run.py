from princess_story import princess_story_data
from space_adventure import space_adventure_data
from game_logic import start_interactive_story, print_slow
from termcolor import colored, cprint
from pyfiglet import Figlet
import images


def main():
    f = Figlet(font='slant')
    print(colored(f.renderText('Story Time Adventure'), color="green"))
    cprint("-----------Made By Jamie Connell 2023 -----------", 'yellow')
    print_slow("Welcome to Story Time Adventure!")
    print_slow("Where your choices help tell the story")
    print_slow("You can get a grown-up to help you on your adventure")
    print_slow("Please choose a story:")
    print("1: The Brave Princess and the Enchanted Forest")
    print("2: The Cosmic Space Adventure")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        start_interactive_story(princess_story_data)
    elif choice == 2:
        start_interactive_story(space_adventure_data)
    else:
        print_slow("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
    