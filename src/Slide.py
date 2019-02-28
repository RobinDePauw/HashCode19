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


    def score(self,other_slide):
        score1 = len(self.get_tags().intersection(other_slide.get_tags()))
        score2 = len(self.get_tags().difference(other_slide.get_tags()))
        score3 = len(self.get_tags().difference(other_slide.get_tags()))
        return min([score1,score2,score3])
