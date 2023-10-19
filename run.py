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

print_slow("Testing Print speed")
print("Normal Speed")