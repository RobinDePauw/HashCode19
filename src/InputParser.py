from Photo import Photo

class InputParser:

    class Photo:
        def __init__(self,id,orientation,n_tags,tags):
            self.id = id
            self.orientation = orientation
            self.n_tags = n_tags
            self.tags = tags

    def parse(self,filename):
        inputfile = open(filename, 'r')
        firstline = inputfile.readline()
        n_photos = int(firstline)

        photo_set = set()

        for id in range(n_photos):
            photoline = inputfile.readline()
            param = photoline[:-1].split(' ')
            orientation, n_tags, tags = str(param[0]), int(param[1]), set(param[2:])
            print(orientation)
            print(n_tags)
            print(tags)
            photo = Photo(id,orientation,n_tags,tags)
            photo_set.add(photo)

        return n_photos, photo_set
