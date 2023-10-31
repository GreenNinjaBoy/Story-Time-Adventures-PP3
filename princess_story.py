import images
from termcolor import colored, cprint

princess_story_data = {
    1: {
        'prompt_before_image':
        "Once upon a time, in a kingdom far, far away,"
        "there lived a brave and kind princess named Lily.",

        'image_path': 'princess',
        
        'prompt_after_image':
        "One sunny morning,"
        "Princess Lily woke up to find her beloved cat, Whiskers, missing! "
        "Determined to find her furry friend,"
        "she embarked on a magical adventure through the Enchanted Forest. "
        "She came across three different paths:"
        "a sparkling river on the left, a mysterious cave in the middle, "
        "and a colorful meadow on the right."
        "Which path will Princess Lily choose?\n",
        'choices': {
            1: {
                'text': 'Explore the sparkling river',
                'destination': 2
            },
            2: {
                'text': 'Enter the mysterious cave',
                'destination': 3
            },
            3: {
                'text': 'Walk through the colorful meadow',
                'destination': 4
            }
        }
    },
    2: {
        'prompt': "Princess Lily followed the sparkling river."
                  "As she walked along the riverbank,"
                  "she noticed a friendly frog "
                  "sitting on a lily pad. The frog croaked,"
                  "'Greetings, Princess Lily!'"
                  "To continue your journey, you'll need"
                  "to solve my riddle."
                  "'What has a golden crown but cannot wear it?'" 
                  "What will Princess Lily answer?\n",
        'choices': {
            1: {
                'text': 'A pineapple',
                'destination': 5
            },
            2: {
                'text': 'A sunflower',
                'destination': 6
            },
            3: {
                'text': 'A pumpkin',
                'destination': 7
            }
        }
    },
    3: {
        'prompt': 
        "Choosing the mysterious cave, Princess Lily ventured inside." 
        "The cave was dark and damp, but Lily's bravery "
        "guided her forward. Deep within the cave," 
        "she encountered a group of glowing mushrooms. Each mushroom emitted "
        "a different color: red, blue, and green." 
        "Which colored mushroom will Princess Lily touch?\n",
        'choices': {
            1: {
                'text': 'Red mushroom',
                'destination': 8
            },
            2: {
                'text': 'Blue mushroom',
                'destination': 9
            },
            3: {
                'text': 'Green mushroom',
                'destination': 10
            }
        }
    },
    4: {
        'prompt': 
        "Princess Lily chose the colorful meadow,"
        "where she found a wise old owl perched on a tree branch."
        "The owl happily shared a piece of advice with Lily:"
        "'In the Enchanted Forest, some creatures are friendly, while'"
        "others can be tricky. Choose your path wisely."
        "Feeling grateful, Princess Lily continued her journey deeper "
        "into the forest. As she walked, she heard a rustling noise behind her." 
        "What will she do?\n",
        'choices': {
            1: {
                'text': 'Turn around and investigate',
                'destination': 11
            },
            2: {
                'text': 'Ignore the noise and keep walking',
                'destination': 12
            },
            3: {
                'text': 'Climb a tree to get a better view',
                'destination': 13
            }
        }
    },
    5: {
        'prompt': "Princess Lily turned around to investigate the noise."
                  "To her surprise, she found a mischievous squirrel "
                  "playing with Whiskers. Relieved and amused,"
                  "Lily picked up Whiskers and continued her journey," 
                  "now with a cheerful companion by her side.\n",
        'choices': {
            1: {
                'text': 'Play with the squirrel',
                'destination': 14
            },
            2: {
                'text': 'Continue the journey',
                'destination': 15
            }
        }
    },
    6: {
        'prompt': "Deciding to ignore the noise, Princess Lily kept walking. It turned out to be a playful breeze rustling "
                  "the leaves. Lily and Whiskers continued their adventure, undisturbed by the forest's natural sounds.\n",
        'choices': {
            1: {
                'text': 'Sing a song to the forest',
                'destination': 16
            },
            2: {
                'text': 'Search for hidden treasures',
                'destination': 17
            }
        }
    },
    7: {
        'prompt': "Princess Lily climbed a tree to get a better view of her surroundings. From the treetop, she spotted Whiskers "
                  "playfully chasing fireflies. Lily called her cat, and Whiskers happily joined her. Together, they descended "
                  "from the tree and resumed their magical journey.\n",
        'choices': {
            1: {
                'text': 'Follow the fireflies',
                'destination': 18
            },
            2: {
                'text': 'Explore the nearby cave',
                'destination': 19
            }
        }
    },
    8: {
        'prompt': "Princess Lily touched the red mushroom. Instantly, she gained the ability to understand the language of animals. "
                  "With this newfound skill, she communicated with the forest creatures, seeking information about Whiskers' "
                  "whereabouts. Guided by her animal friends, Lily successfully reunited with her cat and continued her adventure.\n",
        'choices': {
            1: {
                'text': 'Visit the wise old owl',
                'destination': 20
            },
            2: {
                'text': 'Explore the Enchanted Waterfall',
                'destination': 21
            }
        }
    },
    9: {
        'prompt': "Princess Lily touched the blue mushroom. Surprisingly, it granted her the power to control the elements. "
                  "She used her newfound abilities to create a safe path through the forest, overcoming obstacles and challenges. "
                  "With determination and elemental mastery, Lily found Whiskers and together they ventured back home.\n",
        'choices': {
            1: {
                'text': 'Help the animals in need',
                'destination': 22
            },
            2: {
                'text': 'Return to the Enchanted Meadow',
                'destination': 23
            }
        }
    },
    10: {
        'prompt': "Princess Lily touched the green mushroom. The forest came to life with vibrant colors and enchanting melodies. "
                   "Inspired by the beauty surrounding her, Lily played a tune on her flute, which attracted Whiskers back to her. "
                   "Their journey became a harmonious melody, and they returned home with music in their hearts.\n",
        'choices': {
            1: {
                'text': 'Perform at the Enchanted Festival',
                'destination': 24
            },
            2: {
                'text': 'Explore the Starlit Grove',
                'destination': 25
            }
        }
    },
    11: {
        'prompt': "Princess Lily turned around to investigate the noise. She discovered a friendly forest spirit, who had been "
                  "trying to catch her attention. The spirit offered guidance, helping Lily navigate the Enchanted Forest and "
                  "eventually reunite with Whiskers. Grateful for the spirit's assistance, Lily continued her adventure with a newfound friend.\n",
        'choices': {}
    },
    12: {
        'prompt': "Deciding to ignore the noise, Princess Lily kept walking. Unbeknownst to her, the noise was a clever trap set "
                  "by mischievous fairies. Lily and Whiskers found themselves in a magical clearing, but the fairies quickly "
                  "revealed their playful intentions. After a fun day of games and laughter, the fairies helped Lily and Whiskers "
                  "find their way back home.\n",
        'choices': {}
    },
    13: {
        'prompt': "Princess Lily climbed a tree to get a better view of her surroundings. From above, she spotted a hidden "
                  "path leading to the heart of the Enchanted Forest. Descending from the tree, Lily and Whiskers followed the "
                  "path and discovered a magical portal. With curiosity and courage, they entered the portal, embarking on a "
                  "new adventure in a distant realm.\n",
        'choices': {}
    },
    14: {
        'prompt': "Princess Lily played with the friendly squirrel, creating a bond of friendship. Together, they explored the "
                  "Enchanted Forest, finding joy in each other's company. Whiskers, the playful cat, joined the fun, making their "
                  "journey a delightful adventure. With newfound friends, Lily, Whiskers, and the squirrel returned home, their "
                  "hearts full of happiness.\n",
        'choices': {}
    },
    15: {
        'prompt': "Princess Lily continued her journey, embracing the mysteries of the Enchanted Forest. Along the way, she "
                  "discovered hidden wonders, met magical creatures, and learned valuable lessons. With Whiskers by her side, "
                  "Lily's adventurous spirit led her to new horizons, making their story an endless tale of exploration and discovery.\n",
        'choices': {}
    },
    16: {
        'prompt': "Lily sang a sweet melody to the forest, filling the air with enchanting music. The animals of the forest "
                  "gathered around, captivated by her song. Whiskers, enchanted by the music, joined in with playful leaps. The "
                  "forest echoed with their harmonious tunes, creating a magical moment. Inspired by their music, other creatures "
                  "joined, forming a magical orchestra. Together, they created a symphony that resonated through the Enchanted Forest.\n",
        'choices': {}
    },
    17: {
        'prompt': "Princess Lily embarked on a quest to find hidden treasures in the Enchanted Forest. With Whiskers by her side, "
                  "they discovered ancient artifacts, sparkling gems, and mystical artifacts. Their exploration was filled with "
                  "excitement and wonder. Lily's bravery and curiosity were rewarded with precious treasures, and she shared her "
                  "findings with the kingdom, becoming a legendary explorer.\n",
        'choices': {}
    },
    18: {
        'prompt': "Following the mesmerizing fireflies, Princess Lily entered a magical grove. The trees glowed with ethereal "
                  "light, and the air was filled with enchantment. Whiskers, too, was mesmerized by the glow. Lily and her cat "
                  "explored the Starlit Grove, discovering its secrets and beauty. Their bond grew stronger as they admired the "
                  "stellar wonders, making memories that would last a lifetime.\n",
        'choices': {}
    },
    19: {
        'prompt': "In the mysterious cave, Princess Lily found ancient inscriptions that revealed the history of the Enchanted "
                  "Forest. With Whiskers at her side, she deciphered the secrets, gaining wisdom and knowledge. Their exploration "
                  "uncovered the forest's origins, deepening their understanding of the magical realm. Lily and Whiskers emerged "
                  "from the cave enlightened, ready to protect the Enchanted Forest and its magical inhabitants.\n",
        'choices': {}
    },
    20: {
        'prompt': "Guided by the wise old owl, Princess Lily learned ancient spells and forest magic. With newfound wisdom, she "
                  "became the protector of the Enchanted Forest, ensuring harmony between its inhabitants. Whiskers, too, gained "
                  "mystical powers, becoming a guardian alongside Lily. Together, they safeguarded the forest, their bond strengthening "
                  "as they embraced their magical destinies.\n",
        'choices': {}
    },
    21: {
        'prompt': "Princess Lily and Whiskers explored the Enchanted Waterfall, where they discovered a hidden realm behind "
                  "the cascading waters. In this magical realm, they encountered ancient spirits and celestial beings. Immersed "
                  "in the waterfall's magic, Lily and Whiskers became protectors of the mystical waters, ensuring its purity and "
                  "serenity. Their tale spread far and wide, inspiring others to cherish and preserve the wonders of nature.\n",
        'choices': {}
    },
    22: {
        'prompt': "Using her elemental mastery, Princess Lily aided animals in need throughout the Enchanted Forest. With each "
                  "act of kindness, her bond with Whiskers deepened. Together, they became heroes to the forest creatures, their "
                  "compassion and bravery shining bright. Lily and Whiskers continued their adventures, their legacy forever etched "
                  "in the hearts of the Enchanted Forest's inhabitants.\n",
        'choices': {}
    },
    23: {
        'prompt': "Returning to the Enchanted Meadow, Princess Lily and Whiskers found peace and tranquility among the blooming "
                  "flowers and gentle breezes. They spent their days exploring the meadow, nurturing its beauty, and sharing their "
                  "love with the natural world. Lily's heart swelled with gratitude, knowing she had found her true home, and she "
                  "and Whiskers lived harmoniously in the heart of the Enchanted Forest.\n",
        'choices': {}
    },
    24: {
        'prompt': "Princess Lily performed at the Enchanted Festival, captivating the audience with her musical talents. Whiskers "
                  "joined the performance, adding charm to the show. The kingdom celebrated their magical bond, and Lily became "
                  "the kingdom's beloved musician. Together, they brought joy and harmony to the hearts of all, their melodies echoing "
                  "throughout the kingdom for generations.\n",
        'choices': {}
    },
    25: {
        'prompt': "Exploring the Starlit Grove, Princess Lily and Whiskers encountered celestial beings and discovered the "
                  "secrets of the night sky. Lily became an astronomer, studying the stars and sharing her knowledge with the "
                  "kingdom. Whiskers, too, became a legend, his silhouette immortalized in the constellations. Together, they "
                  "inspired generations to gaze at the stars, fostering a love for the cosmos that connected the kingdom to the universe.\n",
        'choices': {}
    }
}