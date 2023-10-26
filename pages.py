class Page:
    def __init__(self, message, choices=None, choices_mapping=None):
        self.message = message
        self.choices = choices
        self.choices_mapping = choices_mapping