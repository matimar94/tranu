import tranu.shared.preloader
import tranu.tcanvas.image
import tranu.tcanvas.sound
import  tranu.tcanvas.font

class TPreloader(tranu.shared.preloader.SharedPreloader):

    def _increase_preload(self):
        self._loaded += 1

        if self._loaded >= self._total:
            self.preload_ready()

    def _load_image(self, path):
        img = tranu.tcanvas.image.TImage()
        img.load(path, self._increase_preload)

        return img

    def _load_sound(self, path):
        snd = tranu.tcanvas.sound.TSound()
        snd.load(path, self._increase_preload)

        return snd

    def _load_font(self, path, size, sysfont=True):
        fon = tranu.tcanvas.font.TFont(size)
        fon.load(path, sysfont)
        self._increase_preload()

        return fon

    def __init__(self):
        super().__init__()