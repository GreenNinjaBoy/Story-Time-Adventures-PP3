import time
from princess_story import princess_story_data
from termcolor import colored  # Import colored function for colorful output
import images


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


def display_image(images, image_path):
    ascii_art = images.get(image_path)
    if ascii_art:
        print(ascii_art)
    else:
        print(f"Image '{image_path}' not found.")


def start_interactive_story(story_data):
    current_page = 1

    while current_page:
        page = story_data.get(current_page)
        if page:
            print_slow(page.get('prompt_before_image', ''))
            image_path = page.get('image_path')
            if image_path:
                # Pass the images dictionary and image_path
                display_image(images.images, image_path)
            print_slow(page.get('prompt_after_image', ''))
            print_slow(page.get('prompt', ''))
            if page['choices']:
                print("Choices:")
                for choice, data in page['choices'].items():
                    print_slow(f"{choice}. {data['text']}")
                user_choice = get_choice(page['choices'])
                current_page = page['choices'][user_choice]['destination']
            else:
                if 'conclusion' in page:
                    print_slow(page['conclusion'])
                else:
                    print_slow("The End.")
                current_page = 0
        else:
            print_slow(
                "Invalid page configuration. The story cannot continue.")
            current_page = 0
