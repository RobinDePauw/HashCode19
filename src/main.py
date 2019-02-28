
from SlideShow import SlideShow
    return parser.parse("../input/" + filename + ".in")
def makeSlides(slideshow, photos):
    cur_photo = get_next_photo(photos, {})

    slideshow.add_slide(cur_photo)
    for i in range(len(photos)):
        print("Adding photo")
        cur_photo = get_next_photo(photos, cur_photo.tags)
        slideshow.add_slide(cur_photo)
    
    return slideshow

def get_next_photo(photoset, tagset):
    return photoset.pop()


def write_output(slideshow, filename):
    out = slideshow.get_output()
    outputfile = open("../output/" + filename + ".out", 'w')
    outputfile.write(out)
