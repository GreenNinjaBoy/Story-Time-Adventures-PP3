from termcolor import colored, cprint
from pyfiglet import Figlet
from pages import Page  # Import the Page class from pages.py
from game_logic import print_slow, tick
from princess_story import pa_page_1, pa_page_1_2, pa_page_2, pa_page_3, pa_page_4, pa_page_5, pa_page_7, pa_page_9, pa_page_10, pa_page_11
from space_adventure import sa_page_1 

class Storybook:
    def __init__(self, pages):
        self.pages = pages


# Load adventure data from a text file
def load_adventure_data(file_path):
    with open(file_path, 'r') as file:
        adventure_data = file.readlines()
    return adventure_data


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story_data = file.readlines()
    return princess_story_data


# Path to the princess story text file
princess_story_file_path = 'princess_story.txt'


# Load princess story data into the princess_story list
princess_story = load_princess_story(princess_story_file_path)

def load_space_adventure(file_path):
    with open(file_path, 'r') as file:
        space_adventure_data = file.readlines()
    return space_adventure_data


space_adventure_file_path = 'space_adventure.txt'
space_adventure = load_space_adventure(space_adventure_file_path)

# This page will promt the user to pick an adventure, 
# if the user picks 1 then princess_adventure.py will begin
# If the user picks '2' thes space_adventure.py will begin

page_1 = Page(
    message="Select an Adventure:",
    message_2=None,
    choices=["1: The Brave Princess and the Enchanted Forest", "2: The Cosmic Space Adventure"],
    choices_mapping={1: pa_page_1, 2: sa_page_1}
)

story = Storybook([page_1,
                   pa_page_1,
                   pa_page_1_2,
                   pa_page_2,
                   pa_page_3,
                   pa_page_4,
                   pa_page_5,
                   pa_page_7,
                   pa_page_10]) 


def main():
    intro_to_game()
    princess_story_data = load_princess_story('princess_story.txt')
    space_adventure_data = load_space_adventure('space_adventure.txt')
    tick(story.pages[0], princess_story_data, space_adventure_data)


def intro_to_game():
    f = Figlet(font='slant')
    print(colored(f.renderText('Story Time Adventure'), color="green"))
    cprint("-----------Made By Jamie Connell 2023 -----------", 'yellow')
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where the choices you make help tell the story!")
    print_slow("You can get a grown-up to help you on your adventure!")
    print_slow("Now we have two great adventure stories for you to read:")
    
if __name__ == '__main__':
    main()