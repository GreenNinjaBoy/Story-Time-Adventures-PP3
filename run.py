import time
from termcolor import colored, cprint
from pyfiglet import Figlet


def print_slow(str):
    """
    Creating a function that when called,
    will print text slower to the terminal.
    """
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


def intro_to_game():
    """
    Creating a function which gives the user
    a brief introduction 
    """
    f = Figlet(font='slant')
    print(colored(f.renderText('Story Time Adventure'), color="green"))
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where you choices help tell the story")
    print_slow("You can get a grown up to help you on your adventure")


def get_story_tellers_name():
    print_slow("Now!")
    story_tellers_name = input("What shall we call our story teller? ")
    print_slow(f"Hello, {story_tellers_name}! Your adventure begins now!")
    return story_tellers_name


def choosing_a_story(player_name):
    print_slow("Its time to pick a story")
    print_slow(f"1. {player_name} saves their magical unicorn friend")
    print_slow(f"2. {player_name}'s big park adventure")
    print_slow(f"Now, {player_name} please choose")
    choice = input()
    if choice == "1":
        print_slow(f"{player_name} saves their magical unicorn friend")
    elif choice == "2":
        print_slow(f"{player_name}'s big park adventure")
    else:
        print_slow("I am sorry I didn't understand please choose either '1' or '2'")
        choosing_a_story(player_name)

def main():
    intro_to_game()
    player_name = get_story_tellers_name()
    choosing_a_story(player_name)


if __name__ == "__main__":
    main()

