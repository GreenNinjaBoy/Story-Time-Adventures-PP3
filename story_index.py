from pyfiglet import Figlet
from termcolor import colored

from pages import Page
from utils import print_slow

p = Figlet(font="puffy")


def end_game_1(user_name):
    print_slow(f"Princess {user_name} returned to the kingdom")
    print_slow("her crown safely back on her head. The kingdom rejoiced,")
    print_slow("The king and queen praised her cleverness and bravery.")
    print_slow(f"Princess {user_name} shared the lessons she learned with the kingdom,")
    print_slow("teaching everyone the importance of kindness and resourcefulness.")
    print_slow(
        "And so, the tale of the Enchanted Princess and the Lost Crown spread far and wide,"
    )
    print_slow(
        "inspiring children to be resourceful and creative in the face of challenges."
    )
    print(colored(p.renderText("The End"), color="magenta"))


def create_pages(user_name):
    pa_page_9 = Page(
        message=f"Princess {user_name} decided to find a way to distract the bird. Remembering the squirrels' advice, she sang a beautiful melody, capturing the bird's attention. While the bird was enchanted by the melody, Princess {user_name} gently took her crown back.",
        choices=["end_game_1"],
        choices_mapping=None
    )

    pa_page_8 = Page(
        message=f"Princess {user_name} approached the bird and kindly asked for her crown back. Surprised by {user_name}'s kindness, the bird handed the crown over, realizing the error of its ways. Grateful for Princess {user_name}'s forgiveness, the bird promised never to be mischievous again.",
        choices=["end_game_1"],
        choices_mapping=None
    )

    pa_page_7 = Page(
        message=f"Princess {user_name} climbed onto the back of Willow, the river nymph. With a swift and graceful glide, they crossed the enchanted river together. On the other side, they found themselves in a magical grove where the mischievous bird had built a nest. What should Princess {user_name} do next?",
        choices=[
            "Approach the bird and kindly ask for her crown back",
            "Find a way to distract the bird while she takes the crown back.",
        ],
        choices_mapping={1: pa_page_8, 2: pa_page_9},
    )

    pa_page_6 = Page(
        message=f"Princess {user_name} discovered a magic lily pad by the riverbank. With a determined heart, she hopped onto the lily pad, which carried her swiftly across the enchanted river. On the other side, she followed the clues provided by the singing squirrels, leading her straight to the mischievous bird's nest. What should Princess {user_name} do next?",
        choices=[
            "Approach the bird and kindly ask for her crown back",
            "Find a way to distract the bird while she takes the crown back.",
        ],
        choices_mapping={1: pa_page_8, 2: pa_page_9},
    )

    pa_page_5 = Page(
        message=f"Princess {user_name} approached the friendly group of singing squirrels. The squirrels, impressed by her politeness, shared their knowledge of the enchanted forest. They told her about the mischievous bird's favorite hiding spots and the secrets of the magical creatures living in the forest."
        f"With the squirrels' guidance, Princess {user_name} set out to find her crown. As princess {user_name} continued her journey, She came to a river",
        choices=[
            "Ride on a magic lily pad:",
            "Climb on the back of Willow, the river nymph:",
        ],
        choices_mapping={1: pa_page_6, 2: pa_page_7},
    )

    pa_page_4 = Page(
        message=f"Princess {user_name} approached the wise old owl. The owl, with its vast knowledge of the forest,  advised her to follow the sparkling trail of stardust left behind by the mischievous bird. With renewed hope, {user_name} followed the trail. The trail lead {user_name} to a river. How should Princess {user_name} cross the river?",
        choices=[
            "Ride on a magic lily pad:",
            "Climb on the back of Willow, the river nymph:",
        ],
        choices_mapping={1: pa_page_6, 2: pa_page_7},
    )

    pa_page_3 = Page(
        message=(
            f"Princess {user_name} decided to ask her loyal royal pet, Clover, for advice.Clover, with his sharp ",
            "senses, suggested seeking help from the forest animals who were known to be wise.",
        ),
        choices=[
            "A wise old owl perched on a tree:",
            "A friendly group of singing squirrels",
        ],
        choices_mapping={1: pa_page_4, 2: pa_page_5},
    )

    pa_page_2 = Page(
        message=f"Princess {user_name} decided to chase after the bird immediately."
        f"She ran as fast as she could, her golden dress billowing in the wind."
        f"Deep into the enchanted forest,"
        f"she found herself at a magical clearing filled with talking animals."
        f"Who should Princess {user_name} seek help from?",
        choices=[
            "A wise old owl perched on a tree:",
            "A friendly group of singing squirrels",
        ],
        choices_mapping={1: pa_page_4, 2: pa_page_5},
    )

    pa_page_1 = Page(
        message=f"Once upon a time, in a faraway kingdom, there lived a kind and brave princess named {user_name}."
        f" Princess {user_name} had a magical crown that granted her the power to make the kingdom flourish."
        f" One sunny day, while playing in the royal garden,"
        f" a mischievous bird swooped down and snatched her crown,"
        f" flying away into the enchanted forest"
        f" What will Princess {user_name} do?",
        choices=[
            "Chase after the bird immediately.",
            "Ask her loyal royal pet, a talking rabbit named Clover, for advice.",
        ],  
    )
    pa_page_1.choices_mapping={1: pa_page_2, 2: pa_page_3},

    return (
        pa_page_1,
        pa_page_2,
        pa_page_3,
        pa_page_4,
        pa_page_5,
        pa_page_6,
        pa_page_7,
        pa_page_8,
        pa_page_9,
    )


def end_game_2(user_name):
    print_slow(f"{user_name}'s cosmic space adventure became legendary,")
    print_slow("inspiring generations of explorers to venture into the unknown.")
    print_slow("They became a hero, not just for Earth but for the entire galaxy,")
    print_slow("proving that courage, kindness, and quick thinking")
    print_slow("could overcome any challenge in the vast cosmic expanse.")
    print_slow(
        f"And so, the tale of {user_name}'s Cosmic Space Adventure echoed through the universe,"
    )
    print_slow("reminding everyone that the stars were not just distant lights,")
    print_slow("but potential destinations for the brave and curious")
    print(colored(p.renderText("The End"), color="blue"))


def create_pages_2(user_name):
    sa_page_11 = Page(
        message=f"Inspired by the scholar's wisdom, {user_name} harnessed the crystal's energy to communicate with other intelligent life forms across the galaxy. This newfound ability opened up opportunities for peaceful diplomacy and understanding between different civilizations.",
        choices=["end_game_2"],
    )

    sa_page_10 = Page(
        message=f"{user_name} used the alien crystal to fix the spaceship's engine, making it faster than ever before. With the newfound speed, {user_name} zoomed back to Earth, landing safely and sharing the incredible cosmic adventure with the world.",
        choices=["end_game_2"],
    )

    sa_page_9 = Page(
        message=f"Curious about the space station, {user_name} decided to teleport there first. Upon arrival, they met lots of different space explorers. Among them was a wise alien scholar who had a unique crystal that could power up {user_name} spaceship. How should {user_name} use the alien crystal?",
        choices=[
            "Use the crystal to fix the spaceship's engine for faster travel.",
            "Harness the crystal's energy to talk to more aliens.",
        ],
        choices_mapping={1: sa_page_10, 2: sa_page_11},
    )

    sa_page_8 = Page(
        message=f"{user_name} decided to teleport to the lush, alien jungle planet. There, they encountered a friendly tribe of alien beings who offered to help {user_name}. The tribe had a unique crystal that could power up {user_name} spaceship. How should {user_name} use the alien crystal?",
        choices=[
            "Use the crystal to fix the spaceship's engine for faster travel.",
            "Harness the crystal's energy to talk to more aliens.",
        ],
        choices_mapping={1: sa_page_10, 2: sa_page_11},
    )

    sa_page_7 = Page(
        message=f"Undeterred by the cosmic storm, {user_name} hopped into a high-speed space pod. With lightning reflexes, they made it through the storm, reaching the teleportation device just in time. Where should {user_name} teleport to first?",
        choices=[
            "A lush, alien jungle planet. ",
            "A bustling space station filled with intergalactic travelers.",
        ],
        choices_mapping={1: sa_page_8, 2: sa_page_9},
    )

    sa_page_6 = Page(
        message=f"Feeling adventurous,{user_name} decided to navigate through the treacherous asteroid field. It was a challenging journey, but with precise calculations and careful maneuvering, they made it through unscathed and reached the teleportation device. Where should {user_name} teleport to first?",
        choices=[
            "A lush, alien jungle planet. ",
            "A bustling space station filled with intergalactic travelers.",
        ],
        choices_mapping={1: sa_page_8, 2: sa_page_9},
    )

    sa_page_5 = Page(
        message=f"{user_name} chose to find an alternate route through the outpost. With the help of the map, they navigated through hidden corridors and secret passages, successfully guiding the alien creatures to safety. Grateful for the rescue, the aliens shared valuable information about the outpost, including the location of a cosmic teleportation device. How should {user_name} reach the cosmic teleportation device?",
        choices=[
            "Journey through the dangerous asteroid field",
            "Brave the cosmic storm in a high-speed space pod",
        ],
        choices_mapping={1: sa_page_6, 2: sa_page_7},
    )

    sa_page_4 = Page(
        message=f"Using their space ray, {user_name} created a safe passage, allowing the alien creatures to escape. Grateful for the rescue, the aliens shared valuable information about the outpost, including the location of a cosmic teleportation device. How should {user_name} reach the cosmic teleportation device?",
        choices=[
            "Journey through the dangerous asteroid field",
            "Brave the cosmic storm in a high-speed space pod",
        ],
        choices_mapping={1: sa_page_6, 2: sa_page_7},
    )

    sa_page_3 = Page(
        message=f"Intrigued by the alien artifacts, {user_name} decided to examine them closely. {user_name} found a group of friendly aliens who were trapped and a map which have a way out on it How should {user_name} assist the alien creatures?",
        choices=[
            "Use a space ray to create a safe passage",
            "Find an alternate route through the outpost.",
        ],
        choices_mapping={1: sa_page_4, 2: sa_page_5},
    )

    sa_page_2 = Page(
        message=f"Feeling brave, {user_name} decided to venture deeper into the outpost. Among the strange, echoing sounds, {user_name} found a group of friendly aliens who were trapped. They asked for help to escape from a collapsing tunnel How should {user_name} assist the alien creatures?",
        choices=[
            "Use a space ray to create a safe passage",
            "Find an alternate route through the outpost.",
        ],
        choices_mapping={1: sa_page_4, 2: sa_page_5},
    )

    sa_page_1 = Page(
        message=f"In a galaxy far, far away, there lived a curious young astronaut named {user_name}. One day, while exploring a distant planet, {user_name}'s spaceship crashed, leaving them stranded on an unknown cosmic outpost. {user_name} needed to think of a way to get back home. How should {user_name} explore the outpost?",
        choices=[
            "Go deeper into the outpost to investigate mysterious sounds?",
            "Examine the nearby alien artifacts for clues.",
        ],
        choices_mapping={1: sa_page_2, 2: sa_page_3},
    )

    return (
        sa_page_1,
        sa_page_2,
        sa_page_3,
        sa_page_4,
        sa_page_6,
        sa_page_7,
        sa_page_8,
        sa_page_9,
        sa_page_10,
        sa_page_11,
    )