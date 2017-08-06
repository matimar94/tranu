import tranu.shared.sound
import pyglet
import os

pyglet.lib.load_library( os.path.join(os.path.dirname(__file__), "avbin") ) # 'tranu/tpyglet/avbin')
pyglet.have_avbin = True

class TSound(tranu.shared.sound.SharedSound):

    def play(self):
        self._impl.play()

    @property
    def duration(self):
        return NotImplementedError("Define duration for Sound")

    def load(self, path, onloadfunc=None):
        self._impl = pyglet.media.load(path, streaming=False)

        if onloadfunc is not None:
            onloadfunc()

        return self._impl


    def __init__(self):
        super().__init__()
