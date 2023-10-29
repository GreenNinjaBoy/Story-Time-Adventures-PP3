from pages import Page


def load_princess_story(file_path):
    with open(file_path, 'r') as file:
        princess_story_data = file.readlines()
    return princess_story_data


princess_story_file_path = 'princess_story.txt'
princess_story = load_princess_story(princess_story_file_path)

pa_page_11 = Page(
    message=princess_story[47:53],
    message_2=None,
    choices=['end_game']
)
pa_page_10 = Page(
    message=princess_story[94:108],
    choices=['end_game']
)
pa_page_9 = Page(
    message=princess_story[90],
    message_2=princess_story[98:108],
    choices=['end_game']

)
page_8 = Page(
    message=princess_story[35:37],
    message_2=None,
    choices=['end_game'],
)
pa_page_7 = Page(
    message=princess_story[56:64],
    message_2=princess_story[73:79],
    choices=['y', 'n'],
    choices_mapping={'y': pa_page_9, 'n': pa_page_10}
)

# If user choses '1' from pa_page_3 this code will run
# two new options are presented to the user.
pa_page_5 = Page(
    message=princess_story[39:44],
    choices=["y", "n"],
    choices_mapping={"y": pa_page_11, "n": pa_page_9}
)

# If user choses '2' from pa_page_1_2 / pa_page_2 this code will run
# two new options are presented to the user.
pa_page_4 = Page(
    message=princess_story[75:87],
    choices=['y', 'n'],
    choices_mapping={'y': pa_page_9, 'n': pa_page_10}
)

# If user choses '1' from pa_page_1_2 / pa_page_2 this code will run
# two new options are presented to the user.
pa_page_3 = Page(
    message=princess_story[31:36],
    choices=["y", "n"],
    choices_mapping={"y": pa_page_5, "n": pa_page_7}
)

# If user choses '1' from pa_page_1 this code will run
# two new options are presented to the user.
pa_page_2 = Page(
    message=princess_story[16:18],
    choices=["1. Trust Squeaky and Follow His Advice:", "2. Ignore Squeaky and Continue on Your Own:"],
    choices_mapping={1: pa_page_3, 2: pa_page_4}
)

# If user choses '2' from pa_page_1 this code will run
# two new options are presented to the user.
pa_page_1_2 = Page(
    message=princess_story[21:27],
    choices=["1. Trust Squeaky and Follow His Advice:", "2. Ignore Squeaky and Continue on Your Own:"],
    choices_mapping={1: pa_page_3, 2: pa_page_4}
)

# story begins and the first two options are presented to thew user
pa_page_1 = Page(
    message=princess_story[0:13],
    choices=["1. Follow the Forrest Trail:", "2. Find another path"],
    choices_mapping={1: pa_page_2, 2: pa_page_1_2}
)
