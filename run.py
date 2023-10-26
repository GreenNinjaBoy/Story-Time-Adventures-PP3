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


def choose_path(player_name, adventures, princess_story):
    print_slow(adventures[0:4])
    while True:
        choice = input("Which path would you like to take? ").lower()
        if choice == "left":
            print_slow(adventures[5])
            princess_adventure(princess_story)
            break
        elif choice == "right":
            print_slow(adventures[6])
            # Handle space adventure logic here
            break
        else:
            print_slow("I am sorry I didn't understand")
            print_slow("Please enter either 'left' or 'right'")


def main():
    intro_to_game()
    player_name = get_story_tellers_name()
    adventures = load_adventure_stories('story_adventure_1.txt')
    princess_story = load_princess_story('princess_story.txt')
    choose_path(player_name, adventures, princess_story)


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story = file.readlines()
    return princess_story


def princess_adventure(princess_story):
    print_slow('\n'.join(princess_story[:9]))

    paths = [
        "Follow the Forest Trail",
        "Investigate the Abandoned Castle",
        "Seek the Guidance of the Wise Sage"
    ]

    print_slow("\n".join(f"{i + 1}. {path}" for i, path in enumerate(paths)))
    print_slow("Please choose a path")

    while True:
        try:
            choice = int(input())
            if 1 <= choice <= 3:
                break
            else:
                print_slow("I am sorry, please choose 1, 2, or 3")
        except ValueError:
            print_slow("Invalid input. Please enter a number.")

    if choice == 1:
        print_slow(princess_story[9])
        princess_adventure_2(princess_story)
    elif choice == 2:
        print_slow(princess_story[14])
    elif choice == 3:
        print_slow(princess_story[15])


def princess_adventure_2(princess_story):
    print_slow(princess_story[10])

    options = [
        "Trust Squeaky and Follow His Advice",
        "Ignore Squeaky and Continue on Your Own"
    ]

    print_slow("\n".join(f"{i + 1}. {option}" for i, option in enumerate(options)))
    print_slow("What would you like to do?")

    while True:
        try:
            choice = int(input())
            if choice == 1:
                print_slow(princess_story[11])
            elif choice == 2:
                print_slow(princess_story[12])
            else:
                print_slow("I am sorry, please choose 1 or 2")
        except ValueError:
            print_slow("Invalid input. Please enter a number.")
        else:
            break


if __name__ == "__main__":
    main()
