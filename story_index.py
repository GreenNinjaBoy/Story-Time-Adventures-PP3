from pages import Page


def create_pages(user_name):
    pa_page_9 = Page(
        message=f"Princess {user_name} decided to find a way to distract the bird. Remembering the squirrels' advice, she sang a beautiful melody, capturing the bird's attention. While the bird was enchanted by the melody, Princess {user_name} gently took her crown back.",
        choices=None,
    )

    pa_page_8 = Page(
        message=f"Princess {user_name} approached the bird and kindly asked for her crown back. Surprised by {user_name}'s kindness, the bird handed the crown over, realizing the error of its ways. Grateful for Princess {user_name}'s forgiveness, the bird promised never to be mischievous again.",
        choices=None,
    )

    pa_page_7 = Page(
        message=f"Princess {user_name} climbed onto the back of Willow, the river nymph. With a swift and graceful glide, they crossed the enchanted river together. On the other side, they found themselves in a magical grove where the mischievous bird had built a nest. What should Princess {user_name} do next?",
        message_2=None,
        choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
        choices_mapping={1: pa_page_8, 2: pa_page_9}
    )

    pa_page_6 = Page(
        message=f"Princess {user_name} discovered a magic lily pad by the riverbank. With a determined heart, she hopped onto the lily pad, which carried her swiftly across the enchanted river. On the other side, she followed the clues provided by the singing squirrels, leading her straight to the mischievous bird's nest. What should Princess {user_name} do next?",
        message_2=None,
        choices=['1. Approach the bird and kindly ask for her crown back', '2. Find a way to distract the bird while she takes the crown back.'],
        choices_mapping={1: pa_page_8, 2: pa_page_9}
    )

    pa_page_5 = Page(
        message=f"Princess {user_name} approached the friendly group of singing squirrels. The squirrels, impressed by her politeness, shared their knowledge of the enchanted forest. They told her about the mischievous bird's favorite hiding spots and the secrets of the magical creatures living in the forest.",
        message_2=f"With the squirrels' guidance, Princess {user_name} set out to find her crown. As princess {user_name} continued her journey, She came to a river",
        choices=['1. Ride on a magic lily pad:', '2. Climb on the back of Willow, the river nymph:'],
        choices_mapping={1: pa_page_6, 2: pa_page_7}
    )

    pa_page_4 = Page(
        message=f'Princess {user_name} approached the wise old owl. The owl, with its vast knowledge of the forest,  advised her to follow the sparkling trail of stardust left behind by the mischievous bird. With renewed hope, {user_name} followed the trail. The trail lead {user_name} to a river. How should Princess {user_name} cross the river?',
        message_2=None,
        choices=['1. Ride on a magic lily pad:', '2.Climb on the back of Willow, the river nymph:'],
        choices_mapping={1: pa_page_6, 2: pa_page_7}
    )

    pa_page_3 = Page(
        message=f'Princess {user_name} decided to ask her loyal royal pet, Clover, for advice.Clover, with his sharp senses, suggested seeking help from the forest animals who were known to be wise.',
        message_2=None,
        choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
        choices_mapping={1: pa_page_4, 2: pa_page_5}
    )

    pa_page_2 = Page(
        message=f'Princess {user_name} decided to chase after the bird immediately.'
                f'She ran as fast as she could, her golden dress billowing in the wind.'
                f'Deep into the enchanted forest,' 
                f'she found herself at a magical clearing filled with talking animals.'
                f'Who should Princess {user_name} seek help from?',
        message_2=None,
        choices=["1. A wise old owl perched on a tree:", "2. A friendly group of singing squirrels"],
        choices_mapping={1: pa_page_4, 2: pa_page_5}
    )

    pa_page_1 = Page(
        message=f"Once upon a time, in a faraway kingdom, there lived a kind and brave princess named {user_name}."
                f'Princess {user_name} had a magical crown that granted her the power to make the kingdom flourish.'
                f'One sunny day, while playing in the royal garden,' 
                f'a mischievous bird swooped down and snatched her crown,' 
                f'flying away into the enchanted forest'
                f'What will Princess {user_name} do?',
        message_2=None,
        choices=["Chase after the bird immediately.", "Ask her loyal royal pet, a talking rabbit named Clover, for advice."],
        choices_mapping={1: pa_page_2, 2: pa_page_3}
    )

    return pa_page_1, pa_page_2, pa_page_3, pa_page_4, pa_page_5, pa_page_6, pa_page_7, pa_page_8, pa_page_9


def create_pages_2(user_name):
    sa_page_10 = Page(
        message="this is visit planet inhabitants story"
    )

    sa_page_8 = Page(
        message="this is candy feast story"#
    )

    sa_page_6 = Page(
        message="this is sparkling comets story"
    )

    sa_page_4 = Page(
        message='page 4',
        choices=["1. Do you want to have a candy feast?", "2. Or do you want to visit the Candy Planet inhabitants?"],
        choices_mapping={1: sa_page_8, 2: sa_page_10}
    )

    sa_page_3 = Page(
        message="or would you prefer to investigate"
    )

    sa_page_2 = Page(
        message='page 3',
        choices=["1. Do you want to land on the Candy Planet?", "2. Do you want to chase the sparkling comets?"],
        choices_mapping={1: sa_page_4, 2: sa_page_6}
    )

    sa_page_1 = Page(
        message=f'Once upon a time, in a spaceship traveling through the cosmos, there lived two intrepid space explorers named {user_name} and Cosmo.',
        choices=["1. Would you like to explore the glittering Stardust Galaxy?", "2. Or would you prefer to investigate the mysterious Nebula Nebula?"],
        choices_mapping={1: sa_page_2, 2: sa_page_3}
    )

    return sa_page_1, sa_page_2, sa_page_3, sa_page_4, sa_page_6,sa_page_8