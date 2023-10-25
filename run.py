import time
from termcolor import colored, cprint
from pyfiglet import Figlet


def print_slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


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


def choose_path(player_name, adventures):
    print_slow(f"Hello {player_name}! Once upon a time you find yourself in a magic forest ")
    print_slow("Before you there are two paths 'left' and 'right'.")
    print_slow("The left path will take you on an adventure to save a princess.")
    print_slow("The right path will take you an a space adventure.")
    print_slow("which path would you like to take?")
    choice = input().lower()
    if choice == "left":
        print_slow(adventures[0])
        from my_images import squirel_img
        princess_adventure(player_name)
    elif choice == "right":
        print_slow(adventures[1])
        from my_images import portal_img
    else:
        print_slow("I am sorry I didn't understand")
        print_slow("please enter either 'left' or 'right'")
        choose_path(player_name, adventures)


def main():
    intro_to_game()
    player_name = get_story_tellers_name()
    adventures = load_adventure_stories('story_adventure_1.txt')
    choose_path(player_name, adventures)

def princess_adventure(player_name):
    print_slow("Once upon a time, in a faraway kingdom, there lived a beautiful princess named Isabella.")
    print_slow("One fateful night, an evil sorcerer named Malachar cast a dark spell upon the kingdom.")
    print_slow("causing Princess Isabella to disappear without a trace.")
    print_slow("The entire kingdom fell into despair.")
    print_slow(f"and it was believed that only a brave and noble soul called {player_name} could rescue the princess")
    print_slow("and break the curse.")


if __name__ == "__main__":
    main()