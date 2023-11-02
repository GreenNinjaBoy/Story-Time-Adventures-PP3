from termcolor import colored, cprint
from pyfiglet import Figlet
from pages import Page  # Import the Page class from pages.py
from game_logic import print_slow, tick
from princess_story import pa_page_1, pa_page_2, pa_page_3, pa_page_4, pa_page_5, pa_page_6, pa_page_7, pa_page_8, pa_page_9
from space_adventure import sa_page_1 

"""
Initialize the Storybook object with a list of pages.
Args: pages (list): List of Page objects representing the story pages.
"""

class Storybook:
    def __init__(self, pages):
        self.pages = pages

"""
Load adventure data from a text file and return it as a list of strings.
Args: file_path (str): Path to the text file containing adventure data.
Returns: list: List of strings containing adventure data.
"""


def load_adventure_data(file_path):
   
    with open(file_path, 'r') as file:
        adventure_data = file.readlines()
    return adventure_data

"""
Load princess story data from a text file and return it as a list of strings.
Args: file_path (str): Path to the text file containing princess story data.
Returns: list: List of strings containing princess story data.
"""

def load_princess_story(file_path):
    
    with open(file_path, 'r') as file:
        princess_story_data = file.read().splitlines()
    return princess_story_data

 """
Load space adventure data from a text file and return it as a list of strings.
Args:file_path (str): Path to the text file containing space adventure data.
Returns:list: List of strings containing space adventure data.
"""

def load_space_adventure(file_path):
   
    with open(file_path, 'r') as file:
        space_adventure_data = file.readlines()
    return space_adventure_data

"""
Display the introduction message for the game.
"""
def intro_to_game():
    # Display the introduction message for the game.
    f = Figlet(font='slant')
    print(colored(f.renderText('Story Time Adventure'), color="green"))
    cprint("-----------Made By Jamie Connell 2023 -----------", 'yellow')
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where the choices you make help tell the story!")
    print_slow("You can get a grown-up to help you on your adventure!")
    print_slow("Now we have two great adventure stories for you to read:")

"""
  Main function to start the game.
"""
def main():
  
    intro_to_game()
    princess_story_data = load_princess_story('princess_story.txt')
    space_adventure_data = load_space_adventure('space_adventure.txt')
    tick(story.pages[0], princess_story_data, space_adventure_data)


if __name__ == '__main__':
    main()