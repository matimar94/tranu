
class SharedImage():

    def draw(self, window, x, y):
        raise NotImplementedError("Define draw for image")

    def draw_src(self, window, sx, sy, sw, sh, tx, ty, tw, th):
        raise NotImplementedError("Define draw_src for image")

    def draw_ex(self, window, x, y, scale_x=1, scale_y=1, rotation=0, origin_x=0.5, origin_y=0.5, texture_rect=None):
        raise NotImplementedError("Define draw_ex for image")

    @property
    def width(self):
        raise NotImplementedError("Define width property for image")

    @property
    def height(self):
        raise NotImplementedError("Define height property for image")

    def load(self, path):
        raise NotImplementedError("Image loader not defined for target backend")

    def __init__(self):
        self._impl = None
