from Slide import Slide
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

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

    def process_set(self):
        n_tags = map(lambda x: x.n_tags, self.vertical_photos)
        return n_tags

    def plot_dist(self):
        sns.distplot(self.process_set());

