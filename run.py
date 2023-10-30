import time
from termcolor import colored, cprint
from pyfiglet import Figlet
from game_logic import start_interactive_story
from princess_story import princess_story_data


def print_slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


def main():
    f = Figlet(font='slant')
    print(colored(f.renderText('Story Time Adventure'), color="green"))
    cprint("-----------Made By Jamie Connell 2023 -----------", 'yellow')
    print("Welcome to Story Time Adventure!")
    print_slow("Where your choices help tell the story")
    print_slow("You can get a grown-up to help you on your adventure")
    
    while True:
        print("Please Choose a Story:")
        print("1: The Brave Princess and the Enchanted Forest")
        print("2: The Cosmic Quest: A Space Adventure")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_interactive_story(princess_story_data)
            break
        elif choice == '2':
            # Code to start the space adventure (not provided in the previous messages)
            print("Space Adventure is not implemented yet.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()