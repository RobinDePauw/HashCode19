from Photo import Photo
class Slide:

    def __init__(self,photos):
        self.photos = photos

    def output(self):
        if len(self.photos) == 1:
            return str(self.photos[0].id)
        elif len(self.photos) == 2:
            return str(self.photos[0].id) + " " + str(self.photos[1].id)