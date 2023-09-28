class Task():
    # Public properties:
    #   title: string representing a job to do
    # complete: a boolean representing whether it is complete

    def __init__(self, title):
        self.title = title
        self.complete = False

    def mark_complete(self):
        self.complete = True