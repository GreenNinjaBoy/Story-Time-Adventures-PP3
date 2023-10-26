import time
import sys
from pages import Page


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


def tick(current_page):
    if isinstance(current_page.message, list):
        for line in current_page.message:
            print_slow(line)
    else:
        print_slow(current_page.message)
  
    if current_page.choices is None:
        print_slow("Thanks for playing!")
        sys.exit()

    if current_page.choices == ['y', 'n']:
        player_choice = get_yes_or_no_choice()
    else:
        player_choice = get_choice(current_page.choices)

    next_page = current_page.choices_mapping[player_choice]
    tick(next_page)