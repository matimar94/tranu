import tranu.shared.sound
import pyglet
import os

pyglet.lib.load_library( os.path.join(os.path.dirname(__file__), "avbin") ) # 'tranu/tpyglet/avbin')
pyglet.have_avbin = True

class TSound(tranu.shared.sound.SharedSound):

    def play(self, volume=1.0):
        snd = self._impl.play()
        snd.volume = volume

    @property
    def duration(self):
        return self._impl.duration

    def load(self, path, onloadfunc=None):
        self._impl = pyglet.media.load(path, streaming=False)

        if onloadfunc is not None:
            onloadfunc()

        return self._impl

    def __init__(self):
        super().__init__()
