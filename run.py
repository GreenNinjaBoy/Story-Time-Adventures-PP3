import time
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from pages import Page


def load_princess_story(file_path):
    """
    Load princess story data from a text file and return it as a list of strings.
    Args:
        file_path (str): Path to the text file containing princess story data.
    Returns:
        list: List of strings containing princess story data.
    """    
    with open(file_path, 'r') as file:
        princess_story_data = file.read().splitlines()
    return princess_story_data


def load_adventure_data(file_path):
    """
    Load adventure data from a text file and return it as a list of strings.
    Args:
        file_path (str): Path to the text file containing adventure data.
    Returns:
        list: List of strings containing adventure data.
    """    
    with open(file_path, 'r') as file:
        adventure_data = file.readlines()
    return adventure_data


def load_space_adventure(file_path):
    """
    Load space adventure data from a text file and return it as a list of strings.
    Args:
        file_path (str): Path to the text file containing space adventure data.
    Returns:
        list: List of strings containing space adventure data.
    """    
    with open(file_path, 'r') as file:
        space_adventure_data = file.readlines()
    return space_adventure_data      


def print_slow(text):
    """
    Print a text slowly, one character at a time, to create a typewriter effect.
    Args:
        text (str): The text to be printed slowly.
    """
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


def get_choice(choices):
    """
    Get user input for choices and validate it.
    Args: 
        choices (list): List of choices for the user.
    Returns: 
        int: User's choice as an integer.
    """
    print("Available choices:")
    for idx, choice in enumerate(choices, start=1):
        print(f"{idx}. {choice}")
    print("Please select a choice (1 or 2)")
    try:
        choice = int(input())
        if choice in [1, 2]:
            return choice
        else:
            print("Invalid input. Please enter 1 or 2.")
            return get_choice(choices)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_choice(choices)


def get_yes_or_no_choice():
    """
    Get user input for Yes/No choices and validate it.
    Returns:
        str: 'y' for Yes, 'n' for No.
    """
    print("Please enter 'y' for Yes or 'n' for No")
    while True:
        choice = input().lower()
        if choice == 'y' or choice == 'n':
            return choice
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def tick(current_page, princess_story_data, space_adventure_data):
    """
    Display the story messages and handle user interactions recursively.
    Args:
        current_page (Page): The current page of the story.
        princess_story_data (list): List of strings containing princess story data.
        space_adventure_data (list): List of strings containing space adventure data.
    """
    message_1 = current_page.message
    message_2 = current_page.message_2

    if isinstance(message_1, list):
        for line in message_1:
            print_slow(line)
            time.sleep(0.1) 
    else:
        print_slow(message_1)

    if isinstance(message_2, list):
        for line in message_2:
            print_slow(line) 
    elif message_2:
        print_slow(message_2)  

    if current_page.choices is None:
        print_slow("Thanks for playing!")
        sys.exit()

    if current_page.choices == ['end_game']:
        end_game_message = ''.join(princess_story_data[87:98])
        print_slow(end_game_message)
        print_slow("Thanks for playing!")
        sys.exit()

    if current_page.choices == ['y', 'n']:
        player_choice = get_yes_or_no_choice()
    else:
        print("")  # Add a newline character before printing choices
        player_choice = get_choice(current_page.choices)

    next_page = current_page.choices_mapping[player_choice]
    print()  # Add a line break after the user's input
    tick(next_page, princess_story_data, space_adventure_data)

def main():
    """
    Main function to start the game.
    """
    intro_to_game()
    princess_story_data = load_princess_story('princess_story.txt')
    space_adventure_data = load_space_adventure('space_adventure.txt')
    tick(story.pages[0], princess_story_data, space_adventure_data)
    print()  # Add a line break after the story finishes
    print()  # Add a line break before next part of story starts

class Storybook:
    """
    Initialize the Storybook object with a list of pages.
    Args: 
        pages (list): List of Page objects representing the story pages.
    """
    def __init__(self, pages):
        self.pages = pages


def intro_to_game():
    """
    Display the introduction message for the game.
    """
    f = Figlet(font='slant')
    print(colored(f.renderText('Story Time Adventure'), color="green"))
    cprint("-----------Made By Jamie Connell 2023 -----------", 'yellow')
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where the choices you make help tell the story!")
    print_slow("You can get a grown-up to help you on your adventure!")
    print_slow("Now we have two great adventure stories for you to read:")


class Page:
    """
    Represents a page in the story.
    """
    def __init__(self, message, message_2=None, choices=None, choices_mapping=None):
        self.message = message
        self.message_2 = message_2
        self.choices = choices
        self.choices_mapping = choices_mapping


princess_story = load_princess_story('princess_story.txt')
space_adventure = load_space_adventure('space_adventure.txt')


sa_page_10 = Page(
    message="this is visit planet inhabitants story"
)

sa_page_8 = Page(
    message="this is candy feast story"
)

sa_page_6 = Page(
    message="this is sparkling comets story"
)

sa_page_4 = Page(
    message=space_adventure[16:20],
    choices=["1. Do you want to have a candy feast?:", "2. Or do you want to visit the Candy Planet inhabitants?:"],
    choices_mapping={1: sa_page_8, 2: sa_page_10}
)

sa_page_3 = Page(
    message="or would you prefer to investigate"
)

sa_page_2 = Page(
    message=space_adventure[11:15],
    choices=["1. Do you want to land on the Candy Planet?:", "2. Do you want to chase the sparkling comets?:"],
    choices_mapping={1: sa_page_4, 2: sa_page_6}
)

sa_page_1 = Page(
    message=space_adventure[0:9],
    choices=["1. Would you like to explore the glittering Stardust Galaxy:", "2. or would you prefer to investigate the mysterious Nebula Nebula:"],
    choices_mapping={1: sa_page_2, 2: sa_page_3}
)


pa_page_9 = Page(
    message=princess_story[78:83],
    choices=['end_game']
)

pa_page_8 = Page(
    message=princess_story[71:75],
    choices=['end_game']
)

pa_page_7 = Page(
    message=princess_story[62:68],
    message_2=None,
    choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
    choices_mapping={1: pa_page_8, 2: pa_page_9}
)

pa_page_6 = Page(
    message=princess_story[49:58],
    message_2=None,
    choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
    choices_mapping={1: pa_page_8, 2: pa_page_9}
)

pa_page_5 = Page(
    message=princess_story[36:46],
    message_2=None,
    choices=['1. Ride on a magic lily pad:', '2. Climb on the back of Willow, the river nymph:'],
    choices_mapping={1: pa_page_6, 2: pa_page_7}
)

pa_page_4 = Page(
    message=princess_story[26:33],
    message_2=None,
    choices=['1. Ride on a magic lily pad:', '2.Climb on the back of Willow, the river nymph:'],
    choices_mapping={1: pa_page_6, 2: pa_page_7}
)

pa_page_3 = Page(
    message=princess_story[19:22],
    message_2=None,
    choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
    choices_mapping={1: pa_page_4, 2: pa_page_5}
)

pa_page_2 = Page(
    message=princess_story[11:16],
    message_2=None,
    choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
    choices_mapping={1: pa_page_4, 2: pa_page_5}
)


pa_page_1 = Page(
    message=princess_story[0:6],
    message_2=None,
    choices=["1. Chase after the bird immediately.", 
             "2. Ask her loyal royal pet, a talking rabbit named Clover, for advice."],
    choices_mapping={1: pa_page_2, 2: pa_page_3}
)


page_1 = Page(
    message="Select an Adventure:",
    message_2=None,
    choices=["1: The Brave Princess", "2: The Cosmic Space Adventure"],
    choices_mapping={1: pa_page_1, 2: sa_page_1}
)


story = Storybook([page_1,
                   pa_page_1,
                   pa_page_2,
                   pa_page_3,
                   pa_page_4,
                   pa_page_5,
                   pa_page_6,
                   pa_page_7,
                   pa_page_8,
                   pa_page_9])


def main():
    """
    Main function to start the game.
    """
    intro_to_game()
    princess_story_data = load_princess_story('princess_story.txt')
    space_adventure_data = load_space_adventure('space_adventure.txt')
    tick(story.pages[0], princess_story_data, space_adventure_data)


if __name__ == '__main__':
    main()