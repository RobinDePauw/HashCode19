from Slide import Slide

class SlideShuffler:
    def __init__(self, slideshow):
        self.slideshow = slideshow

    def shuffle(self):
        
        slides  = self.slideshow.slide_list
        slides = sorted(slides,key=lambda x: x.get_tags_amt())
        print("slides sorted")
        new_slides = []
        while len(slides) != 0:
            subset_size = min(200,len(slides))
            subset = slides[:subset_size]
            slides = slides[subset_size:]

            optimized = self.shuffle_list(subset)
            new_slides.extend(optimized)

        self.slideshow.slide_list = new_slides


        return self.slideshow


    def shuffle_list(self, slidelist):
        slides_copy= slidelist
        cur_slide = slidelist[0]
        slides_copy.remove(cur_slide)
        shuffled = [cur_slide]
        for i in range(len(slides_copy)):
            cur_slide = cur_slide.pick_best_match(slides_copy)
            shuffled.append(cur_slide)
            slides_copy.remove(cur_slide)
        return shuffled

    