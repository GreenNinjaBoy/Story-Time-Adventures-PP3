import time
import sys


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story_data = file.read().splitlines()
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
    message = current_page.message
    message_2 = current_page.message_2

    player_choice = get_choice(current_page.choices)

    next_page = current_page.choices_mapping[player_choice]
    tick(next_page, princess_story_data, space_adventure_data)