import time
from princess_story import princess_story_data
from termcolor import colored  # Import colored function for colorful output


def print_slow(text,):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


def get_choice(choices):
    while True:
        try:
            user_input = int(input("Please enter your choice: "))
            if user_input in choices:
                return user_input
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def start_interactive_story(story_data):
    current_page = 1

    while current_page:
        page = story_data.get(current_page)
        if page:
            print_slow(page['prompt'])  # Print prompt slowly

            if page['choices']:
                print("Choices:")
                for choice, data in page['choices'].items():
                    print_slow(f"{choice}. {data['text']}")  # Print choices slowly
                user_choice = get_choice(page['choices'])
                current_page = page['choices'][user_choice]['destination']
        else:
            print_slow("The End.")  # Print "The End" slowly
            current_page = 0