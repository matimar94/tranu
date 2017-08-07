import tranu.shared.font
import tranu.tpyglet.colors
import pyglet


class TFont(tranu.shared.font.SharedFont):

    def __init__(self, size):
        super().__init__(size)

        self._family = "Arial"
        self._label = None

    def load(self, path, sysfont=True):
        self._label = pyglet.text.Label(font_name=path, font_size=self._size)

    def draw(self, window, text, x, y, color=tranu.tpyglet.colors.RED):
        self._label.text = text
        self._label.x = x
        self._label.y = window.height - y
        self._label.color = (*color, 255) if len(color)==3 else color

        self._label.draw()
