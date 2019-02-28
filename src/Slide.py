from Photo import Photo
class Slide:

    def __init__(self,photos):
        self.photos = photos

    def get_tags(self):
        if len(self.photos) == 1:
            return self.photos[0].tags
        elif len(self.photos) == 2:
            return self.photos[0].tags | self.photos[1].tags

    def output(self):
        if len(self.photos) == 1:
            return str(self.photos[0].id)
        elif len(self.photos) == 2:
            return str(self.photos[0].id) + " " + str(self.photos[1].id)

    def get_tags(self):
        tags = self.photos[0].tags
        if len(self.photos) == 2:
            tags.add(self.photos[1].tags)
        return tags