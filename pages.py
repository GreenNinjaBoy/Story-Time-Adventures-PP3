class Page:
    """
    Represents a page in the story.
    """

    def __init__(self, message, message_2=None, choices=None, choices_mapping=None):
        self.message = message
        self.message_2 = message_2
        self.choices = choices
        self.choices_mapping = choices_mapping
