import random

from Slide import Slide
import matplotlib.pyplot as plt

class VerticalCombinator:
    def __init__(self,vertical_photos):
        self.vertical_photos = vertical_photos


    def random(self):
        result_set = set()
        buffer = None
        set_copy = self.vertical_photos.copy()
        for photo in set_copy:
            if buffer == None:
                buffer = photo
            else:
                slide = Slide([buffer,photo])
                result_set.add(slide)
                buffer = None
        return result_set

    def order_big_with_small(self):
        result_set = set()
        photo_list = list(self.vertical_photos)
        photo_list.sort(key=lambda x: x.n_tags)
        for i in range(int(len(photo_list)/2.0-1)):
            result_set.add(Slide([photo_list[i],photo_list[-i-1]]))
        return result_set

    def max_union_tags_random(self,sample_n):

        def get_best_fit(candidate,second_candidates):
            list_cand = list(second_candidates)
            list_cand.sort(key=lambda x: len(candidate.get_tags().union(x.get_tags())),reverse=True)
            return list_cand[0]

        result_set= set()
        photos = self.vertical_photos.copy()
        for index in range(int(len(photos)/2.0)):
            candidate = photos.pop()
            second_candidates = random.sample(photos,min([sample_n,len(photos)]))
            best_fit = get_best_fit(candidate,second_candidates)
            photos.remove(best_fit)
            slide = Slide([candidate,best_fit])
            result_set.add(slide)

        return result_set



    def process_set(self,set):
        n_tags = list(map(lambda x: len(x.get_tags()), set))
        return n_tags

    def plot_dist(self,set):
        plt.hist(self.process_set(set))
        plt.show()

