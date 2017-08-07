import tranu.image
import tranu.sound
import tranu.font

class SharedPreloader():
    IMAGE = 0
    SOUND = 1

    def preload_ready(self):
        if self._loadfunc:
            self._loadfunc()

    def _load_image(self, path):
        img = tranu.image.TImage()
        img.load(path)

        return img

    def _load_sound(self, path):
        snd = tranu.sound.TSound()
        snd.load(path)

        return snd

    def _load_font(self, path, size, sysfont=True):
        fon = tranu.font.TFont(size)
        fon.load(path, sysfont)

        return fon

    def load(self, func):
        self._total = sum(list(map(len, self._resources)))
        self._loaded = 0

        self._loadfunc = func

        for img in self._images.items():
            #img.onload = self._increase_preload
            self._images[img[0]] = self._load_image(img[1])

        for snd in self._sounds.items():
            self._sounds[snd[0]] = self._load_sound(snd[1])

        for fon in self._fonts.items():
            self._fonts[fon[0]] = self._load_font(fon[1][0], fon[1][1], fon[1][2])


    def add_image(self, name, image_path):
        self._images[name] = image_path

    def add_sound(self, name, sound_path):
        self._sounds[name] = sound_path

    def add_font(self, name, font_path, font_size, sysfont=True):
        self._fonts[name] = (font_path, font_size, sysfont)

    def get_image(self, name):
        return self._images[name]

    def get_sound(self, name):
        return self._sounds[name]

    def get_font(self, name):
        return self._fonts[name]

    def __init__(self):
        self._images = {}
        self._sounds = {}
        self._fonts = {}
        self._types = [ "image", "sound" ]

        self._resources = (self._images, self._sounds, self._fonts)
