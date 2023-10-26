import time
from termcolor import colored, cprint
from pyfiglet import Figlet


class Storybook:
    def __init__(self, pages):
        self.pages = pages


class Page:
    def __init__(self, message, choices=None, choices_mapping=None):
        self.message = message
        self.choices = choices
        self.choices_mapping = choices_mapping


def print_slow(text, delay=0.05):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()


def get_choice(choices):
    for choice in choices:
        print(choice)
    print("Please select a choice")

    try:
        choice = int(input())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_choice(choices)
    return choice


def get_yes_or_no_choice():
    print("Please enter 'y' for Yes or 'n' for No")
    while True:
        choice = input().lower()
        if choice == 'y' or choice == 'n':
            return choice
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def tick(current_page):
    print_slow(current_page.message)
  
    if current_page.choices is None:
        print_slow("Thanks for playing!")
        import sys; sys.exit()

    if current_page.choices == ['y', 'n']:
        player_choice = get_yes_or_no_choice()
    else:
        player_choice = get_choice(current_page.choices)
    
    next_page = current_page.choices_mapping[player_choice]
    tick(next_page)


def main():
    intro_to_game()
    player_name = get_story_tellers_name()
    adventures = load_adventure_stories('story_adventure_1.txt')
    princess_story = load_princess_story('princess_story.txt')

    page_6 = Page(
        message=princess_story[18], 
        choices=None)

    page_5 = Page(
        message=princess_story[12:18],
        choices=["y", "n"],
        choices_mapping={"y": page_6, "n": page_6}
    )

    page_4 = Page(
        message=princess_story[18],
        choices=None,
        choices_mapping={None}
    )

    page_3 = Page(
        message=princess_story[9:11],
        choices=["1. Trust Squeaky and Follow His Advice:", "2. Ignore Squeaky and Continue on Your Own:"],
        choices_mapping={1: page_5, 2: page_6}
    )

    page_2 = Page(
        message=princess_story[0:7],
        choices=["1. Follow the Forrest Trail:", "2. Investigate the Abandoned Castle:", "3. Seek the Guidance of the Wise Sage: "],
        choices_mapping={1: page_3, 2: page_4}
        )

    page_1 = Page(
        message=adventures[0:4],
        choices=["1: Princess Adventure", "2: Space Adventure"],
        choices_mapping={1: page_2, 2: page_6}
    )

    story = Storybook([page_1, page_2, page_3, page_4, page_5, page_6])  # Add more pages as needed
    tick(story.pages[0])


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


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story = file.readlines()
    return princess_story


if __name__ == "__main__":
    main()