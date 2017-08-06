import tranu.shared.font
import pyglet


class TFont(tranu.shared.font.SharedFont):

    def __init__(self, size):
        super().__init__(size)

        self._family = "Arial"
        self._label = None

    def load(self, path, sysfont=True):
        self._label = pyglet.text.Label(font_name=path, font_size=self._size)

    def draw(self, window, text, x, y):
        self._label.text = text
        self._label.x = x
        self._label.y = window.height - y

        self._label.draw()
