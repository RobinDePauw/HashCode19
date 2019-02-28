from Slide import Slide
from SlideShow import SlideShow
from InputParser import InputParser
from SlideShuffler import SlideShuffler
import sys
from VerticalCombinator import VerticalCombinator


def process_file(filename):
    parser = InputParser()
    return parser.parse("../input/" + filename + ".in")


def makeSlides(slideshow, photos):
    verts = set(filter(lambda x: x.orientation == "V", photos))
    horts = set(filter(lambda x: x.orientation == "H", photos))
    combinator = VerticalCombinator(verts)
    vert_slides = combinator.order_big_with_small()
    hort_slides = set(map(lambda x:Slide([x]),horts))
    all_slides = hort_slides | vert_slides
    slideshow = SlideShow()
    slideshow.set_slide_list(list(all_slides))
    return slideshow


def write_output(slideshow, filename):
    out = slideshow.get_output()
    outputfile = open("../output/" + filename + ".out", 'w')
    outputfile.write(out)

if __name__ == "__main__":
    files = sys.argv[1:]

    for f in files:
        print("starting file: "+f)
        photos = process_file(f)[1]
        slideshow = SlideShow()
        slideshow = makeSlides(slideshow, photos)
        ss = SlideShuffler(slideshow)
        slideshow = ss.shuffle()
        write_output(slideshow, f)
