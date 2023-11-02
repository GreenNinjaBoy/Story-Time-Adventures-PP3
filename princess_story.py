from pages import Page


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story_data = file.read().splitlines()
    return princess_story_data


princess_story_file_path = 'princess_story.txt'
princess_story = load_princess_story(princess_story_file_path)

pa_page_14 = Page(
    message='This is page 14'
)
pa_page_12 = Page(
    message=princess_story[36:38],
    choices=['end_game']
)
pa_page_11 = Page(
    message=princess_story[47:53],
    message_2=None,
    choices=['end_game']
)

pa_page_10 = Page(
    message=princess_story[26:31],
    message_2=None,
    choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
    choices_mapping={1: pa_page_12, 2: pa_page_14}
)

pa_page_9 = Page(
    message=princess_story[92:101],
    message_2=None,
    choices=['end_game']
)

pa_page_8 = Page(
    message='option2'
)


pa_page_7 = Page(
    message=princess_story[56:64],
    message_2=princess_story[73:79],
    choices=['y', 'n'],
    choices_mapping={'y': pa_page_9, 'n': pa_page_11}
)

pa_page_6 = Page(
    message='option 1'
)
pa_page_5 = Page(
    message=princess_story[38:44],
    message_2=None,
    choices=["y", "n"],
    choices_mapping={"y": pa_page_11, "n": pa_page_9}
)


pa_page_4 = Page(
    message=princess_story[17:23],
    message_2=None,
    choices=['1. Ride on a magic lily pad:', '2.Climb on the back of Willow, the river nymph:'],
    choices_mapping={1: pa_page_8, 2: pa_page_10}
)

# 3 new options are presented to the user if 'a mysterious' cave is chosen
pa_page_3 = Page(
    message=princess_story[13:18],
    message_2=None,
    choices=["1. Red:", "2. Blue:", "Green"],
    choices_mapping={1: pa_page_5, 2: pa_page_7, 3: pa_page_9}
)


pa_page_2 = Page(
    message=princess_story[9:14],
    message_2=None,
    choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
    choices_mapping={1: pa_page_4, 2: pa_page_6}
)

# story begins and the first two options are presented to thew user
pa_page_1 = Page(
    message=princess_story[0:6],
    message_2=None,
    choices=["1. Chase after the bird immediately.", "2.Ask her loyal royal pet, a talking rabbit named Clover, for advice."],
    choices_mapping={1: pa_page_2, 2: pa_page_3} 
)
