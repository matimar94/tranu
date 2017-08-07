import tranu.shared.image

_DEGTORAD = 3.1416/180

class TImage(tranu.shared.image.SharedImage):

    def draw(self, window, x, y):
        window._context.drawImage(self._impl, x, y)

    def draw_src(self, window, sx, sy, sw, sh, tx, ty, tw, th):
        window._context.drawImage(self._impl, sx, sy, sw, sh, tx, ty, tw, th)

    def draw_ex(self, window, x, y, scale_x=1, scale_y=1, rotation=0, origin_x=0.5, origin_y=0.5, texture_rect=None):
        if texture_rect:
            sx, sy, sw, sh = texture_rect
        else:
            sx, sy, sw, sh = 0, 0, self._impl.width, self._impl.height

        window._context.save()
        window._context.translate(x, y)
        window._context.rotate(rotation * _DEGTORAD)
        window._context.drawImage(self._impl, sx, sy, sw, sh, -(sw*scale_x *origin_x), -(sh*scale_y *origin_y), sw*scale_x, sh*scale_y)
        window._context.restore()

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
        #self._impl = None
