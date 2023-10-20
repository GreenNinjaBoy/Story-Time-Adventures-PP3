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
    print_slow(colored('Welcome to Story Time Adventures', color="red"))
    print_slow("Where your choices help tell the story")
    print_slow("You can get a grown-up to help you on your adventure")


def get_story_tellers_name():
    print_slow("Now!")
    story_tellers_name = input("What shall we call our story teller? ")
    print_slow(f"Hello, {story_tellers_name}! Your adventure begins now!")
    return story_tellers_name


def save_story_adventure(file_path, player_name, adventure_text):
    with open(file_path, 'w') as file:
        adventure_text = adventure_text.replace("{player_name}", player_name)
        file.write(adventure_text)


def print_story_adventure(adventure_text, player_name):
    print_slow(adventure_text)
    adventure_text = adventure_text.replace(player_name, "{player_name}")
    return adventure_text


def choosing_a_story(player_name, adventure_text):
    print_slow("It's time to pick a story")
    print_slow(f"1. {player_name} saves their magical unicorn friend")
    print_slow(f"2. {player_name}'s big park adventure")
    print_slow(f"Now, {player_name} please choose")
    choice = input()

    if choice == "1":
        save_story_adventure('story_adventure_1.txt', player_name, adventure_text)
        print_story_adventure(adventure_text, player_name)
    elif choice == "2":
        print_slow(f"{player_name}'s big park adventure")
    else:
        print_slow("I am sorry, I didn't understand. Please choose either '1' or '2'")
        choosing_a_story(player_name, adventure_text)


def main():
    intro_to_game()
    player_name = get_story_tellers_name()
    adventure_text = open('story_adventure_1.txt', 'r').read()
    adventure_text = choosing_a_story(player_name, adventure_text)
    save_adventure_text('story_adventure_1.txt', adventure_text)
    adventure_text = print_story_adventure(adventure_text, player_name)
    save_adventure_text('story_adventure_1.txt', adventure_text)

if __name__ == "__main__":
    main()