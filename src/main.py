
from SlideShow import SlideShow
from InputParser import InputParser

def process_file(filename):
    parser = InputParser()
    return parser.parse("../input/" + filename + ".in")


def makeSlides(slideshow, photos):
    vertical_buffer = None

    for i in range(len(photos)):
        cur_photo = photos.pop()
        if(cur_photo.orientation == "H"):
            slideshow.add_slide(cur_photo)
        else:
            if vertical_buffer is None:
                vertical_buffer = cur_photo
            else:
                slideshow.add_doubleslide(vertical_buffer, cur_photo)
                vertical_buffer = None
  
    return slideshow


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
        slideshow = SlideShow()
        slideshow = makeSlides(slideshow, photos)
        slideshow.optimize()
        write_output(slideshow, f)
