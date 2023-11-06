import time
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from pages import Page
# from princess_story import  pa_page_1, pa_page_2, pa_page_3, pa_page_4, pa_page_5, pa_page_6, pa_page_7, pa_page_8, pa_page_9


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
    while True:
        print('')
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


def tick(current_page, story_title):
    """
    Display the story messages and handle user interactions recursively.
    Args:
        current_page (Page): The current page of the story.
        story_title (str): The title of the current story.
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

    player_choice = get_choice(current_page.choices)
    next_page = current_page.choices_mapping[player_choice]
    print()  # Add a line break after the user's input
    tick(next_page, story_title)


class Storybook:
    """
    Initialize the Storybook object with a list of pages.
    Args:
        pages (list): List of Page objects representing the story pages.
        user_name (str): The user's name.
    """

    def __init__(self, pages, user_name):
        self.pages = pages
        self.user_name = user_name


f = Figlet(font='slant')
p = Figlet(font="puffy")

user_name = None


def intro_to_game():
    """
    Display the introduction message for the game.
    """
    print(colored(f.renderText('Story Time Adventures'), color="green"))
    cprint("----------- Made By Jamie Connell 2023 -----------", 'yellow')
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where the choices you make help tell the story!")
    print_slow("You can get a grown-up to help you on your adventure!")
    global user_name
    user_name = get_name("Now brave adventurer, what is your name?: ")
    print_slow(f'Welcome {user_name}, we have two great adventure stories for you to read:')
    return user_name


def get_name(prompt):
    """
    Prompts the user to enter their name and returns it.
    Args:
        prompt (str): The prompt message to display to the user.
    Returns:
        str: The user's name.
    """
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print("Sorry, only letters A-Z and a-z are allowed.")


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
    message='page 4',
    choices=["1. Do you want to have a candy feast?", "2. Or do you want to visit the Candy Planet inhabitants?"],
    choices_mapping={1: sa_page_8, 2: sa_page_10}
)

sa_page_3 = Page(
    message="or would you prefer to investigate"
)

sa_page_2 = Page(
    message='page 3',
    choices=["1. Do you want to land on the Candy Planet?", "2. Do you want to chase the sparkling comets?"],
    choices_mapping={1: sa_page_4, 2: sa_page_6}
)

sa_page_1 = Page(
    message='page 1',
    choices=["1. Would you like to explore the glittering Stardust Galaxy?", "2. Or would you prefer to investigate the mysterious Nebula Nebula?"],
    choices_mapping={1: sa_page_2, 2: sa_page_3}
)


def main():
    """
    Main function to start the game.
    """
    intro_to_game()

    # Get the user's choice of story and story title
    choice = get_choice(["1. The Brave Princess", "2. The Cosmic Space Adventure"])
    story_title = "The Brave Princess" if choice == 1 else "The Cosmic Space Adventure"
    if story_title == "1":
        print(colored(p.renderText(story_title), color="magenta"))
    else:
        print(colored(p.renderText(story_title), color="blue"))

    # Import the pages for the selected story
    if choice == 1:
        from princess_story import pa_page_1, pa_page_2, pa_page_3, pa_page_4, pa_page_5, pa_page_6, pa_page_7, pa_page_8, pa_page_9
        pages = [pa_page_1, pa_page_2, pa_page_3, pa_page_4, pa_page_5, pa_page_6, pa_page_7, pa_page_8, pa_page_9]
    elif choice == 2:
        print('Space Story')

    # Start the selected story
    story = Storybook(pages, user_name)
    tick(story.pages[0], story_title)


if __name__ == '__main__':
    main()