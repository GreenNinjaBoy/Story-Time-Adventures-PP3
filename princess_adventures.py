from pages import Page


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story_data = file.readlines()
    return princess_story_data


princess_story_file_path = 'princess_story.txt'
princess_story = load_princess_story(princess_story_file_path)

page_9 = Page(
    message=princess_story[55],
    choices=['end_game_2']

)
page_8 = Page(
    message=princess_story[35:37],
    choices=['end_game'],
)
page_7 = Page(
    message=princess_story[36:43],
    choices=None,
    choices_mapping=None
)
page_6 = Page(
    message=princess_story[27:33],
    choices=["y", "n"],
    choices_mapping={"y": page_8, "n": page_7}
)

page_5 = Page(
    message=princess_story[19:24],
    choices=["y", "n"],
    choices_mapping={"y": page_6, "n": page_6}
)

page_4 = Page(
    message=princess_story[40:51],
    choices=['y', 'n'],
    choices_mapping={'y': page_9, 'n': page_9}
)

page_3 = Page(
    message=princess_story[14:16],
    choices=["1. Trust Squeaky and Follow His Advice:", "2. Ignore Squeaky and Continue on Your Own:"],
    choices_mapping={1: page_5, 2: page_4}
)

page_2 = Page(
    message=princess_story[0:11],
    choices=["1. Follow the Forrest Trail:", "2. Investigate the Abandoned Castle:", "3. Seek the Guidance of the Wise Sage: "],
    choices_mapping={1: page_3, 2: page_4}
)