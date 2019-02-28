from Slide import Slide


class SlideShow:
    def __init__(self):
        self.slide_list = []

    def add_slide(self, photo):
        self.slide_list.append(Slide([photo]))

    def add_doubleslide(self, photo1, photo2):
        assert (photo1.orientation == "V")
        assert (photo2.orientation == "V")
        self.slide_list.append(Slide([photo1, photo2]))

    def get_output(self):
        output = ""
        output += str(len(self.slide_list)) + "\n"
        for slide in self.slide_list:
            output += slide.output() + "\n"

        return output

    def optimize(self):
        # todo: implement
        pass

    def score_transition(self,slide1,slide2):
        score1 = len(slide1.get_tags().intersection(slide2.get_tags()))
        score2 = len(slide1.get_tags().difference(slide2.get_tags()))
        score3 = len(slide2.get_tags().difference(slide1.get_tags()))
        return min([score1,score2,score3])

    def percentage_score(self,slide1,slide2):
        score = self.score_transition(slide1,slide2)
        perc_score = score / (len(slide1.get_tags)/2.0)
        return perc_score
