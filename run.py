from termcolor import colored, cprint
from pyfiglet import Figlet
from pages import Page  # Import the Page class from pages.py
from game_logic import print_slow, get_choice, get_yes_or_no_choice, tick


class Storybook:
    def __init__(self, pages):
        self.pages = pages


# Load adventure data from a text file
def load_adventure_data(file_path):
    with open(file_path, 'r') as file:
        adventure_data = file.readlines()
    return adventure_data


# Path to the adventures text file
adventures_file_path = 'story_adventure_1.txt'

# Load adventure data into the adventures list
adventures = load_adventure_data(adventures_file_path)


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story_data = file.readlines()
    return princess_story_data


# Path to the princess story text file
princess_story_file_path = 'princess_story.txt'


# Load princess story data into the princess_story list
princess_story = load_princess_story(princess_story_file_path)

page_6 = Page(
    message=princess_story[22:37],
    choices=None,
    choices_mapping=None
)

page_5 = Page(
    message=princess_story[17:20],
    choices=["y", "n"],
    choices_mapping={"y": page_6, "n": page_6}
)

page_4 = Page(
    message=princess_story[18],
    choices=None,
    choices_mapping={None}
)

page_3 = Page(
    message=princess_story[11:13],
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

story = Storybook([page_1, page_2, page_3, page_4, page_5, page_6]) 


def main():
    intro_to_game()
    tick(story.pages[0])


def intro_to_game():
    f = Figlet(font='slant')
    print(colored(f.renderText('Story Time Adventure'), color="green"))
    cprint("-----------Made By Jamie Connell 2023 -----------", 'yellow')
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where your choices help tell the story")
    print_slow("You can get a grown-up to help you on your adventure")


if __name__ == "__main__":
    main()