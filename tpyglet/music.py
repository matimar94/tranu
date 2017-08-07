import tranu.tpyglet.sound
import pyglet


class TMusic(tranu.tpyglet.sound.TSound):

    def load(self, path, onloadfunc=None):
        self._impl = pyglet.media.load(path, streaming=True)

        if onloadfunc is not None:
            onloadfunc()

        return self._impl
