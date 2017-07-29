import tranu.image

class SharedPreloader():
    IMAGE = 0
    SOUND = 1


    def preload_ready(self):
        if self._loadfunc:
            self._loadfunc()

    def _load_image(self, path):
        img = tranu.image.Image()
        img.load(path)

        return img

    def load(self, func):
        self._total = sum(list(map(len, self._resources)))
        self._loaded = 0

        self._loadfunc = func

        for img in self._images.items():
            #img.onload = self._increase_preload
            self._images[img[0]] = self._load_image(img[1])

    def add_image(self, name, image_path):
        self._images[name] = image_path

    def get_image(self, name):
        return self._images[name]

    def __init__(self):
        self._images = {}
        self._types = [ "image", "sound" ]

        self._resources = (self._images,)
