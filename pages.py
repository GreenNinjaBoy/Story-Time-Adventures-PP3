class Page:
    """
    Represents a page in the story.
    """

    def __init__(
        self, message, choices, choices_mapping=None
    ):
        self.message = message
        self.choices = choices
        self.choices_mapping = choices_mapping or None

