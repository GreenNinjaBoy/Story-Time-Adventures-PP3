import time


def print_slow(text, line_length=80, letter_delay=0.05, word_delay=0.5):
    """
    Print a text slowly with a typewriter effect, breaking it into multiple
    lines if it exceeds a certain length.
    Args:
        text (str): The text to be printed slowly.
        line_length (int): Maximum number of characters
        in a line before breaking.
        letter_delay (float): Delay between printing individual letters.
        word_delay (float): Delay between printing words.
    """
    current_line_length = 0
    for word in text.split():
        if current_line_length + len(word) + 1 <= line_length:
            for letter in word:
                print(letter, end="", flush=True)
                time.sleep(letter_delay)
            print(" ", end="", flush=True)
            current_line_length += len(word) + 1
        else:
            print("\n", end="", flush=True)
            time.sleep(word_delay)
            current_line_length = 0
            for letter in word:
                print(letter, end="", flush=True)
                time.sleep(letter_delay)
            print(" ", end="", flush=True)
            current_line_length += len(word) + 1
    print()