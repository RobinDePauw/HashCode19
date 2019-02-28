from InputParser import InputParser
from SlideShow import SlideShow


def process_file(filename):
    parser = InputParser()
    return parser.parse("../input/" + filename + ".in")

def makeSlides(slideshow, photos):
    cur_photo = get_next_photo(photos, {})

    slideshow.add_slide(cur_photo)
    for i in range(len(photos)):
        print("Adding photo")
        cur_photo = get_next_photo(photos, cur_photo.tags)
        slideshow.add_slide(cur_photo)

def get_next_photo(photoset, tagset):
    return photoset.pop()


   # output = None
  #  outputfile = open("../output/" + filename + ".out", 'w')
   # outputfile.write(output)

if __name__ == "__main__":

    files = ["a", "b", "c", "d", "e"]

    for file in files:
        print("starting file: "+file)
        photos = process_file(file)[1]
        slideshow = SlideShow()
        makeSlides(slideshow, photos)
