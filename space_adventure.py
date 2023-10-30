from pages import Page

def load_space_adventure(file_path):
    with open(file_path, 'r') as file:
        space_adventure_data = file.readlines()
    return space_adventure_data


space_adventure_file_path = 'space_adventure.txt'
space_adventure = load_space_adventure(space_adventure_file_path)


sa_page_10 = Page(
    message="this is visit planet inhabitants story"
)
sa_page_8 = Page(
    message=space_adventure[21:31],
    choices=["end_game_2"]
)

sa_page_6 = Page(
    message="this is sparkling comets story"
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