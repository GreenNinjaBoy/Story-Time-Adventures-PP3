import time


def print_slow(str):
    """
    Creating a function that when called,
    will print text slower to the terminal.
    """
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


def intro_to_game():
    """
    Creating a function which gives the user
    a brief introduction 
    """
    print_slow("Welcome to Story Time Adventures")
    print_slow("Where you choices help tell the story")
    print_slow("You can get a grown up to help you on your adventure")


def get_story_tellers_name():
    """
    Creating a function that will ask the user
    to enter their name
    """
    print_slow("Now!")
    story_tellers_name = input("What shall we call our story teller? ")
    print_slow(f"Hello, {story_tellers_name}! your adventure begins now!")
    return name
    

def choosing_a_story(player_name):
    """
    The user will now be prompted to choose 
    their adventure
    """
    print_slow(f"Now, {player_name}")


def main():
    intro_to_game()
    get_story_tellers_name()


main()


if __name__ == "__main__":
    player_name = get_story_tellers_name
    choosing_a_story()
