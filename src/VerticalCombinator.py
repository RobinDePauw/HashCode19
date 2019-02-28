import random

from Slide import Slide
import matplotlib.pyplot as plt

class VerticalCombinator:
    def __init__(self,vertical_photos):
        self.vertical_photos = vertical_photos


    def random(self):
        result_set = set()
        buffer = None
        for photo in self.vertical_photos:
            if buffer == None:
                buffer = photo
            else:
                slide = Slide([buffer,photo])
                buffer = None
        return result_set

    def order_big_with_small(self):
        result_set = set()
        photo_list = list(self.vertical_photos)
        ordered_list = photo_list.sort(key=lambda x: x.n_tags)
        for i in range(len(ordered_list))/2-1:
            result_set.add(Slide([ordered_list[i],ordered_list[-i-1]]))

    def max_union_tags_random(self,sample_n):

        def get_best_fit(candidate,second_candidates):
            list = list(second_candidates)
            list = list.order(key=lambda x: len(candidate.get_tags().union(x.get_tags())),reverse=True)
            return

        result_set= set()
        photos = self.vertical_photos.copy()
        for index in range(len(photos)):
            candidate = photos.pop()
            second_candidates = random.sample(photos,sample_n)
            best_fit = get_best_fit(candidate,second_candidates)
            photos.remove(best_fit)
            slide = Slide([candidate,best_fit])
            result_set.add(slide)

        return result_set



    def process_set(self):
        n_tags = list(map(lambda x: x.n_tags, self.vertical_photos))
        return n_tags

    def plot_dist(self):
        plt.hist(self.process_set())
        plt.show()

