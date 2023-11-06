from pages import Page
from run import user_name

pa_page_9 = Page(
    message='page 9',
    choices=['end_game']
)

pa_page_8 = Page(
    message='page8',
    choices=['end_game']
)

pa_page_7 = Page(
    message='page 7',
    message_2=None,
    choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
    choices_mapping={1: pa_page_8, 2: pa_page_9}
)

pa_page_6 = Page(
    message='page 6',
    message_2=None,
    choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
    choices_mapping={1: pa_page_8, 2: pa_page_9}
)

pa_page_5 = Page(
    message='page 5',
    message_2=None,
    choices=['1. Ride on a magic lily pad:', '2. Climb on the back of Willow, the river nymph:'],
    choices_mapping={1: pa_page_6, 2: pa_page_7}
)

pa_page_4 = Page(
    message='page 4',
    message_2=None,
    choices=['1. Ride on a magic lily pad:', '2.Climb on the back of Willow, the river nymph:'],
    choices_mapping={1: pa_page_6, 2: pa_page_7}
)

pa_page_3 = Page(
    message='page 3',
    message_2=None,
    choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
    choices_mapping={1: pa_page_4, 2: pa_page_5}
)

pa_page_2 = Page(
    message='Princess Lily decided to chase after the bird immediately.' 
    'She ran as fast as she could, her golden dress billowing in the wind.'
    'Deep into the enchanted forest,' 
    'she found herself at a magical clearing filled with talking animals.' 
    'Who should Princess Lily seek help from?',
    message_2=None,
    choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
    choices_mapping={1: pa_page_4, 2: pa_page_5}
)


pa_page_1 = Page(
    message=f"Once upon a time, in a faraway kingdom,there lived a kind and brave princess named {user_name}."
    f'Princess {user_name} had a magical crown that granted her the power to make the kingdom flourish.' 
    'One sunny day, while playing in the royal garden,' 
    'a mischievous bird swooped down and snatched her crown,' 
    'flying away into the enchanted forest'
    f'What will princess {user_name} do?',
    message_2=None,
    choices=["Chase after the bird immediately.", "Ask her loyal royal pet, a talking rabbit named Clover, for advice."],
    choices_mapping={1: pa_page_2, 2: pa_page_3}
)