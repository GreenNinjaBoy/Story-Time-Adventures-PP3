from pages import Page

def load_space_adventure(file_path):
    with open(file_path, 'r') as file:
        space_adventure_data = file.readlines()
    return space_adventure_data


space_adventure_file_path = 'space_adventure.txt'
space_adventure = load_space_adventure(space_adventure_file_path)

sa_page_20 = Page(
    message=space_adventure[75:91],
    choices=["end_game_2"]
)

sa_page_18 = Page(
    message=space_adventure[58:74],
    choices=["end_game_2"]
)
sa_page_16 = Page(
    message=space_adventure[48:57],
    choices=["1. Do you want to confront the candy-stealing alien and ask why it took the candies?", "2. Do you want to follow the footprints further into the cave?"],
    choices_mapping={1: sa_page_18, 2: sa_page_20}
)

sa_page_14 = Page(
    message=space_adventure[38:47],
    choices=["end_game_2"]
)

sa_page_13 = Page(
    message="This is to see where the comet comes form story"
)
sa_page_12 = Page(
    message=space_adventure[96:106],
    choices=["end_game_2"]
)

sa_page_10 = Page(
    message=space_adventure[33:36],
    choices=["1. Do you want to build a candy trap to catch the alien?", "2. Do you want to search for clues around the Candy Planet?"],
    choices_mapping={1: sa_page_14, 2: sa_page_16}
)
sa_page_8 = Page(
    message=space_adventure[21:31],
    choices=["end_game_2"]
)

sa_page_6 = Page(
    message=space_adventure[92:95],
    choices=["1. Do you want to catch a comet and make a wish?", "2. Do want to see where the comets come from?"],
    choices_mapping={1: sa_page_12, 2: sa_page_13}
)

sa_page_4 = Page(
    message=space_adventure[16:20],
    choices=["1. Do you want to have a candy feast?:", "2. Or do you want to visit the Candy Planet inhabitants?:"],
    choices_mapping={1: sa_page_8, 2: sa_page_10}
)

sa_page_3 = Page(
    message="this is Nebula story"
)

sa_page_2 = Page(
    message=space_adventure[11:15],
    choices=["1. Do you want to land on the Candy Planet?:", "2. Do you want to chase the sparkling comets?:"],
    choices_mapping={1: sa_page_4, 2: sa_page_6}
)

sa_page_1 = Page(
    message=space_adventure[0:9],
    choices=["1. Would you like to explore the glittering Stardust Galaxy:", "2. or would you prefer to investigate the mysterious Nebula Nebula:"],
    choices_mapping={1: sa_page_2, 2: sa_page_3}
)