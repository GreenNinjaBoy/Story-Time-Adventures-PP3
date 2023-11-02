from pages import Page

"""
Load princess story data from a text file and return it as a list of strings.
Args: file_path (str): Path to the text file containing princess story data.
Returns: list: List of strings containing princess story data.
"""

def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story_data = file.read().splitlines()
    return princess_story_data


princess_story_file_path = 'princess_story.txt'
princess_story = load_princess_story(princess_story_file_path)

# each pa_page below will extract assigned message from princess.txt
# each pa_page will display choices to the user to select.
# depending on the users answer they will be redirect to the corrisponding pa_page

pa_page_9 = Page(
    message=princess_story[78:83],
    choices=['end_game']
)

pa_page_8 = Page(
    message=princess_story[71:75],
    choices=['end_game']
)

pa_page_7 = Page(
    message=princess_story[62:68],
    message_2=None,
    choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
    choices_mapping={1: pa_page_8, 2: pa_page_9}
)

pa_page_6 = Page(
    message=princess_story[49:58],
    message_2=None,
    choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
    choices_mapping={1: pa_page_8, 2: pa_page_9}
)

pa_page_5 = Page(
    message=princess_story[36:46],
    message_2=None,
    choices=['1. Ride on a magic lily pad:', '2. Climb on the back of Willow, the river nymph:'],
    choices_mapping={1: pa_page_6, 2: pa_page_7}
)

pa_page_4 = Page(
    message=princess_story[26:33],
    message_2=None,
    choices=['1. Ride on a magic lily pad:', '2.Climb on the back of Willow, the river nymph:'],
    choices_mapping={1: pa_page_6, 2: pa_page_7}
)

pa_page_3 = Page(
    message=princess_story[19:22],
    message_2=None,
    choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
    choices_mapping={1: pa_page_4, 2: pa_page_5}
)

pa_page_2 = Page(
    message=princess_story[11:16],
    message_2=None,
    choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
    choices_mapping={1: pa_page_4, 2: pa_page_5}
)


pa_page_1 = Page(
    message=princess_story[0:6],
    message_2=None,
    choices=["1. Chase after the bird immediately.", 
             "2. Ask her loyal royal pet, a talking rabbit named Clover, for advice."],
    choices_mapping={1: pa_page_2, 2: pa_page_3}
)
