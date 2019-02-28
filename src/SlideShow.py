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
        print(self.slide_list)
        for slide in self.slide_list:
            output += slide.output() + "\n"

        return output
