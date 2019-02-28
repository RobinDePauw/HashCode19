class Photo:
    def __init__(self, id, orientation, n_tags, tags):
        self.id = id
        self.orientation = orientation
        self.n_tags = n_tags
        self.tags = tags

    def __str__(self):
        return "< photo:" +str(self.id) + ">"