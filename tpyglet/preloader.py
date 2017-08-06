import tranu.shared.preloader
import tranu.tpyglet.image
import tranu.tpyglet.sound


class TPreloader(tranu.shared.preloader.SharedPreloader):

    def _load_image(self, path):
        img = tranu.tpyglet.image.TImage()
        img.load(path)

        return img

    def load(self, func):
        super().load(func)

        self.preload_ready()

    def _load_sound(self, path):
        snd = tranu.tpyglet.sound.TSound()
        snd.load(path)

        return snd

    def __init__(self):
        super().__init__()