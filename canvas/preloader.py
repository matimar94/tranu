import tranu.shared.preloader
import tranu.canvas.image
import tranu.canvas.sound

class TPreloader(tranu.shared.preloader.SharedPreloader):

    def _increase_preload(self):
        self._loaded += 1

        if self._loaded >= self._total:
            self.preload_ready()

    def _load_image(self, path):
        img = tranu.canvas.image.TImage()
        img.load(path, self._increase_preload)

        return img

    def _load_sound(self, path):
        snd = tranu.canvas.sound.TSound()
        snd.load(path, self._increase_preload)

        return snd

    def __init__(self):
        super().__init__()