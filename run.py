import time
from termcolor import colored, cprint
from pyfiglet import Figlet


def print_slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


def intro_to_game():
    f = Figlet(font='slant')
    print(colored(f.renderText('Story Time Adventure'), color="green"))
    cprint("-----------Made By Jamie Connell 2023 -----------", 'yellow')
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where your choices help tell the story")
    print_slow("You can get a grown-up to help you on your adventure")


def get_story_tellers_name():
    print_slow("Now!")
    story_tellers_name = input("What shall we call our story teller? ")
    return story_tellers_name


def load_adventure_stories(file_path):
    with open(file_path, 'r') as file:
        adventures = file.readlines()
        return adventures


def choose_path(player_name, adventures, princess_story):
    print_slow(f"Hello {player_name}! You wake up in a magic forest ")
    print_slow("Before you there are two paths 'left' and 'right'.")
    print_slow("The left path will take you on an adventure to save a princess.")
    print_slow("The right path will take you on a space adventure.")
    print_slow("Which path would you like to take?")
    choice = input().lower()
    if choice == "left":
        print_slow(adventures[0])
        princess_adventure(princess_story)
    elif choice == "right":
        print_slow(adventures[1])
        # Handle space adventure logic here
    else:
        print_slow("I am sorry I didn't understand")
        print_slow("Please enter either 'left' or 'right'")
        choose_path(player_name, adventures, princess_story)


def main():
    intro_to_game()
    player_name = get_story_tellers_name()
    adventures = load_adventure_stories('story_adventure_1.txt')
    princess_story = load_princess_story('princess_story.txt')
    choose_path(player_name, adventures, princess_story)


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story = file.readlines()
        return princess_story


def princess_adventure(princess_story):
    for i in range(9):
        print_slow(princess_story[i])

    print_slow("1. Follow the Forest Trail:")
    print_slow("2. Investigate the Abandoned Castle:")
    print_slow("3. Seek the Guidance of the Wise Sage:")
    print_slow("please choose a path")
    try:
        choice = int(input())
        if choice == 1:
            print_slow(princess_story[9])
        elif choice == 2:
            print_slow(princess_story[10])
        elif choice == 3:
            print_slow(princess_story[12])
        else:
            print_slow("I am sorry, please choose 1, 2, or 3")
            princess_adventure(princess_story)  # Recursively call the function to prompt the user again
    except ValueError:
        print_slow("Invalid input. Please enter a number.")
        princess_adventure(princess_story)


if __name__ == "__main__":
    main()