from SlideShow import SlideShow
from InputParser import InputParser
from VerticalCombinator import VerticalCombinator

def process_file(filename):
    parser = InputParser()
    return parser.parse("../input/" + filename + ".in")


def makeSlides(slideshow, photos):
    pass


def write_output(slideshow, filename):
    out = slideshow.get_output()
    outputfile = open("../output/" + filename + ".out", 'w')
    outputfile.write(out)

if __name__ == "__main__":

    files = ["a", "b", "c", "d", "e"]
    #files = ["a"]

    for f in files:
        print("starting file: "+f)
        photos = process_file(f)[1]
        verts = set(filter(lambda x: x.orientation == "V",photos))
        combinator = VerticalCombinator(verts)
        combinator.plot_dist()
