class GotoError(Exception):
    def __init__(self):
        self.message = 'maximum goto depth exceeded'
        super().__init__(self.message)
