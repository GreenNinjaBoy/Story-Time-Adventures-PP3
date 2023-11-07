import time
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from pages import Page
from story_index import create_pages, create_pages_2, end_game_2, end_game_1


def print_slow(text, line_length=80, letter_delay=0.05, word_delay=0.5):
    """
    Print a text slowly with a typewriter effect, breaking it into multiple lines if it exceeds a certain length.
    Args:
        text (str): The text to be printed slowly.
        line_length (int): Maximum number of characters in a line before breaking.
        letter_delay (float): Delay between printing individual letters.
        word_delay (float): Delay between printing words.
    """
    current_line_length = 0
    for word in text.split():
        if current_line_length + len(word) + 1 <= line_length:
            for letter in word:
                print(letter, end='', flush=True)
                time.sleep(letter_delay)
            print(' ', end='', flush=True)
            current_line_length += len(word) + 1
        else:
            print('\n', end='', flush=True)
            time.sleep(word_delay)
            current_line_length = 0
            for letter in word:
                print(letter, end='', flush=True)
                time.sleep(letter_delay)
            print(' ', end='', flush=True)
            current_line_length += len(word) + 1
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

    if current_page.choices == ['end_game_1']:
        end_game_1(user_name)
        sys.exit()
    elif current_page.choices == ["end_game_2"]:
        end_game_2(user_name)
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
    get_name("Now brave adventurer, what is your name? \n")
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
