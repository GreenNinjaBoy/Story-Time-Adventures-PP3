import time
import sys
from pages import Page


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story_data = file.readlines()
    return princess_story_data


princess_story_file_path = 'princess_story.txt'


princess_story = load_princess_story(princess_story_file_path)


def print_slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
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


def tick(current_page, princess_story_data, space_adventure_data):
    message_1 = current_page.message
    message_2 = current_page.message_2

    if isinstance(message_1, list):
        for line in message_1:
            print_slow(line)
            time.sleep(0.1)  # Add a slightly longer delay between lines for clarity
    else:
        print_slow(message_1)
    
    if isinstance(message_2, list):
        for line in message_2:
            print_slow(line)  # Add a slightly longer delay between lines for clarity
    elif message_2:
        print_slow(message_2)  # Print message_2 slowly

    if current_page.choices is None:
        print_slow("Thanks for playing!")
        sys.exit()

    if current_page.choices == ['end_game']:
        end_game_message = ''.join(princess_story_data[110:121])
        print_slow(end_game_message)
        print_slow("Thanks for playing!")
        sys.exit()
    
    if current_page.choices == ["end_game_2"]:
        end_game_message_2 = ''.join(space_adventure_data[34:56])
        print_slow(end_game_message_2)
        print_slow("Thanks for Playing")
        sys.exit()

    if current_page.choices == ['y', 'n']:
        player_choice = get_yes_or_no_choice()
    else:
        player_choice = get_choice(current_page.choices)

    next_page = current_page.choices_mapping[player_choice]
    tick(next_page, princess_story_data, space_adventure_data)