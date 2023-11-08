# imports
import sys

from pyfiglet import Figlet
from termcolor import colored, cprint

from story_index import create_pages, create_pages_2, end_game_1, end_game_2
from utils import print_slow

# global vars
GREEN = "green"
MAGENTA = "magenta"
BLUE = "blue"
RED = "red"
YELLOW = "yellow"

f = Figlet(font="slant")
p = Figlet(font="puffy")


# classes and funcs
def get_choice(choices):
    """
    Get user input for choices and validate it.
    Args:
        choices (list): List of choices for the user.
    Returns:
        int: User's choice as an integer.
    """
    while True:
        print("")
        for idx, choice in enumerate(choices, start=1):
            print(f"{idx}. {choice}")
        print("Please select a choice (1 or 2)")
        try:
            choice = int(input())
            if choice in [1, 2]:
                return choice
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def tick(current_page, story_title, user_name):
    """
    Display the story messages and handle user interactions recursively.
    Args:
        current_page (Page): The current page of the story.
        story_title (str): The title of the current story.
    """
    message_1 = current_page.message

    print_slow(message_1)
    # TODO merge message_1 and message_2#
    
    if current_page.choices == ["end_game_1"]:
        end_game_1(user_name)
        sys.exit()
    elif current_page.choices == ["end_game_2"]:
        end_game_2(user_name)
        sys.exit()

    player_choice = get_choice(current_page.choices)
    next_page = current_page.choices_mapping[player_choice]
    print()  # Add a line break after the user's input
    tick(next_page, story_title, user_name)


def get_name(prompt):
    """
    Prompts the user to enter their name and assigns
    it to the global variable user_name.
    Args:
        prompt (str): The prompt message to display to the user.
    """
    while True:
        name = input(prompt)
        if name.isalpha():
            return name  # Assign the input value to the global user_name variable
        else:
            print("Sorry, only letters A-Z and a-z are allowed.")


def intro_to_game():
    """
    Display the introduction message for the game.
    """
    print(colored(f.renderText("Story Time Adventures"), color=GREEN))
    cprint("----------- Made By Jamie Connell 2023 -----------", YELLOW)
    print_slow(colored("Welcome to Story Time Adventures", color=RED))
    print_slow("Where the choices you make help tell the story!")
    print_slow("You can get a grown-up to help you on your adventure!")
    user_name = get_name("Now brave adventurer, what is your name? \n")
    print_slow(f"Welcome {user_name}, we have two great adventure stories for you:")
    return user_name


def main():
    """
    Main function to start the game.
    """
    user_name = intro_to_game()

    # Get the user's choice of story and story title
    choice = get_choice(["The Brave Princess", "The Cosmic Space Adventure"])

    # set up the user's story
    if choice == 1:
        story_title = "The Brave Princess"
        print(colored(p.renderText(story_title), color=MAGENTA))
        pages = create_pages(user_name)
    elif choice == 2:
        story_title = "The Cosmic Space Adventure"
        print(colored(p.renderText(story_title), color=BLUE))
        pages = create_pages_2(user_name)
    else:
        raise ValueError("Didn't recognise that choice!")

    # Start the selected story
    tick(pages[0], story_title, user_name)


if __name__ == "__main__":
    main()