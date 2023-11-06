import time
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from pages import Page
from story_index import create_pages, create_pages_2


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
        print_slow(f"Princess {user_name} returned to the kingdom"),
        print_slow("her crown safely back on her head. The kingdom rejoiced,"),
        print_slow("The king and queen praised her cleverness and bravery."),
        print_slow(f"Princess {user_name} shared the lessons she learned with the kingdom,"),
        print_slow("teaching everyone the importance of kindness and resourcefulness."),
        print_slow("And so, the tale of the Enchanted Princess and the Lost Crown spread far and wide,"),
        print_slow("inspiring children to be resourceful and creative in the face of challenges."),
        print(colored(p.renderText("The End"), color="magenta"))
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

user_name = None  # Declare user_name as a global variable


def get_name(prompt):
    """
    Prompts the user to enter their name and assigns it to the global variable user_name.
    Args:
        prompt (str): The prompt message to display to the user.
    """
    global user_name  # Declare user_name as a global variable
    while True:
        name = input(prompt)
        if name.isalpha():
            user_name = name  # Assign the input value to the global user_name variable
            break
        else:
            print("Sorry, only letters A-Z and a-z are allowed.")


def intro_to_game():
    """
    Display the introduction message for the game.
    """
    print(colored(f.renderText('Story Time Adventures'), color="green"))
    cprint("----------- Made By Jamie Connell 2023 -----------", 'yellow')
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where the choices you make help tell the story!")
    print_slow("You can get a grown-up to help you on your adventure!")
    get_name("Now brave adventurer, what is your name?")
    print_slow(f'Welcome {user_name}, we have two great adventure stories for you to read:')


def main():
    """
    Main function to start the game.
    """
    intro_to_game()

    # Get the user's choice of story and story title
    choice = get_choice(["The Brave Princess", "The Cosmic Space Adventure"])
    story_title = "The Brave Princess" if choice == 1 else "The Cosmic Space Adventure"
    if story_title == "1":
        print(colored(p.renderText(story_title), color="magenta"))
    else:
        print(colored(p.renderText(story_title), color="blue"))

    # Import the pages for the selected story
    if choice == 1:
        pages = create_pages(user_name)
    elif choice == 2:
        pages = create_pages_2(user_name)

    # Start the selected story
    story = Storybook(pages, user_name)
    tick(story.pages[0], story_title)


if __name__ == '__main__':
    main()
