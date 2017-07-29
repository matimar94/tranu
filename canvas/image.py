import tranu.shared.image

class TImage(tranu.shared.image.SharedImage):

    def draw(self, window, x, y):
        window._context.drawImage(self._impl, x, y)

    def draw_src(self, window, sx, sy, sw, sh, tx, ty, tw, th):
        window.context.drawImage(self._impl, sx, sy, sw, sh, tx, ty, tw, th)

    @property
    def width(self):
        return self._impl.width

    @property
    def height(self):
        return self._impl.height

    def load(self, path, onloadfunc=None):
        self._impl = __new__(Image())
        self._impl.src = path

        if onloadfunc:
            self._impl.onload = onloadfunc

        return self._impl

    def __init__(self):
        super().__init__()
        self._impl = None
