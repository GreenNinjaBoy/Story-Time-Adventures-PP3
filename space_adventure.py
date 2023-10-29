from pages import Page

def load_space_adventure(file_path):
    with open(file_path, 'r') as file:
        space_adventure_data = file.readlines()
    return space_adventure_data


space_adventure_file_path = 'space_adventure.txt'
space_adventure = load_space_adventure(space_adventure_file_path)

sa_page_3 = Page(
    message="this is Nebula story"
)

sa_page_2 = Page(
    message="this is stardust story"
)

sa_page_1 = Page(
    message=space_adventure[0:9],
    choices={"1. Would you like to explore the glittering Stardust Galaxy:", "2. or would you prefer to investigate the mysterious Nebula Nebula:"},
    choices_mapping={1: sa_page_2, 2: sa_page_3}
)