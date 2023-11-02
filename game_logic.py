import time
import sys

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
Args: file_path (str): Path to the text file containing space adventure data.
Returns: list: List of strings containing space adventure data.
"""
def load_space_adventure(file_path):

    with open(file_path, 'r') as file:
        space_adventure_data = file.read().splitlines()
    return space_adventure_data


"""
Print a text slowly, one character at a time, to create a typewriter effect.
Args:
text (str): The text to be printed slowly.
"""
def print_slow(text):
    
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


"""
Get user input for choices and validate it.
Args: choices (list): List of choices for the user.
Returns: int: User's choice as an integer.
"""
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


"""
Get user input for Yes/No choices and validate it.
Returns: str: 'y' for Yes, 'n' for No.
"""
def get_yes_or_no_choice():
    
    print("Please enter 'y' for Yes or 'n' for No")
    while True:
        choice = input().lower()
        if choice == 'y' or choice == 'n':
            return choice
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


"""
Display the story messages and handle user interactions recursively.
Args:current_page (Page): The current page of the story.
     princess_story_data (list): List of strings containing princess story data.
     space_adventure_data (list): List of strings containing space adventure data.
"""
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
        end_game_message = ''.join(princess_story_data[87:98])
        print_slow(end_game_message)
        print_slow("Thanks for playing!")
        sys.exit()

    if current_page.choices == ['y', 'n']:
        player_choice = get_yes_or_no_choice()
    else:
        player_choice = get_choice(current_page.choices)

    next_page = current_page.choices_mapping[player_choice]
    tick(next_page, princess_story_data, space_adventure_data
