import tranu.shared.image
import pyglet

class TImage(tranu.shared.image.SharedImage):

    def draw(self, window, x, y):
        self._impl.blit(x, window.height - self.height - y)

    def draw_ex(self, window, x, y, scale_x=1, scale_y=1, rotation=0, origin_x=0.5, origin_y=0.5, texture_rect=None ):
        if texture_rect:
            sx, sy, sw, sh = texture_rect
        else:
            sx, sy, sw, sh = 0, 0, self._impl.width, self._impl.height

        tw, th = sw * scale_x, sh * scale_y

        sy = self.height - sh - sy

        #pox = self._impl.anchor_x
        #poy = self._impl.anchor_y

        #self._impl.anchor_x = origin_x
        #self._impl.anchor_y = origin_y
        reg = self._impl.get_region(sx, sy, sw, sh)
        reg.anchor_x = origin_x * sw
        reg.anchor_y = -origin_y * sh
        self._sprite._set_texture( reg ) # We update position (expensive) next line.
        self._sprite.update(x, window.height - y - th, 0, scale_x=tw/sw, scale_y=th/sh)
        self._sprite.draw()
        #self._impl.anchor_x = pox
        #self._impl.anchor_y = poy

    def draw_src(self, window, sx, sy, sw, sh, tx, ty, tw, th):
        #tex = self._impl.tex_coords

        sy = self.height - sh - sy

        #self._impl.tex_coords = (sx, sy, 0.,
                              #sx+sw, sy, 0.,
                              #sx+sw, sy+sh, 0.,
                              #sx, sy+sh, 0.)
        #self._impl.blit(tx, window.height - ty - th, width=tw, height=th)

        #self._sprite.image = self._impl.get_region(sx, sy, sw, sh)
        self._sprite._set_texture( self._impl.get_region(sx, sy, sw, sh) ) # We update position (expensive) next line.
        self._sprite.update(tx, window.height - ty - th, 0, scale_x=tw/sw, scale_y=th/sh)
        self._sprite.draw()

        #self._impl.tex_coords = tex

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

        self._sprite = pyglet.sprite.Sprite(self._impl)

        return self._impl


    def __init__(self):
        super().__init__()

        self._sprite : pyglet.sprite.Sprite = None
        #self._impl = None
