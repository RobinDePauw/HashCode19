import random
import time
import tqdm as tqdm

from Slide import Slide
from SlideShow import SlideShow
from InputParser import InputParser
from VerticalCombinator import VerticalCombinator
import itertools
import matplotlib.pyplot as plt
    

def process_file(filename):
    parser = InputParser()
    return parser.parse("../input/" + filename + ".in")


def makeSlides(slideshow, photos):
    pass


def write_output(slideshow, filename):
    out = slideshow.get_output()
    outputfile = open("../output/" + filename + ".out", 'w')
    outputfile.write(out)

def find_common(tags,photos):
    set_copy = photos.copy()
    for i in range(len(set_copy)):
        candidate = set_copy.pop()
        if len(tags.intersection(candidate.get_tags())) > 0:
            return candidate

    return None



if __name__ == "__main__":

    files = ["a", "b", "c", "d", "e"]
    files = ["b"]

    for f in files:
        print("starting file: "+f)
        photos = process_file(f)[1]
        list_result = []
        selected = photos.pop()
        list_result.append(Slide([selected]))
        for i in range(len(photos)):
            print(i)
            next = find_common(selected.get_tags(),photos)
            if next is not None:
                list_result.append(Slide([next]))
                selected = next
                photos.remove(next)
            else:
                next = photos.pop()
                list_result.append(Slide([next]))
                selected = next
        slideshow = SlideShow()
        slideshow.set_slide_list(list_result)
        write_output(slideshow, f)


