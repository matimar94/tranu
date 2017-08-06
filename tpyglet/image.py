import tranu.shared.image
import pyglet

class TImage(tranu.shared.image.SharedImage):

    def draw(self, window, x, y):
        self._impl.blit(x, window.height - self.height - y)

    def draw_src(self, window, sx, sy, sw, sh, tx, ty, tw, th):
        tex = self._impl.tex_coords

        sy = self.height - sh - sy

        self._impl.tex_coords = (sx, sy, 0.,
                              sx+sw, sy, 0.,
                              sx+sw, sy+sh, 0.,
                              sx, sy+sh, 0.)

        self._impl.blit(tx, window.height - ty - th, width=tw, height=th)

        self._impl.tex_coords = tex

    @property
    def width(self):
        return self._impl.width

    @property
    def height(self):
        return self._impl.height

    def load(self, path, onloadfunc=None):
        self._impl = pyglet.image.load(path).get_texture(True)

        pyglet.gl.glTexParameteri(self._impl.target, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)

        pyglet.gl.glTexParameteri(self._impl.target, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)

        if onloadfunc is not None:
            onloadfunc()

        return self._impl


    def __init__(self):
        super().__init__()
        #self._impl = None
