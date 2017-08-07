import tranu.shared.font
import tranu.tcanvas.colors

class TFont(tranu.shared.font.SharedFont):

    def __init__(self, size):
        super().__init__(size)

        self._family = "Arial"

    def load(self, path, sysfont=True):
        if path.endswith(".ttf"):
            self._family = path[:-4]
        elif sysfont:
            self._family = path
        else:
            raise NameError("Wrong font name given")

    def draw(self, window, text, x, y, color=tranu.tcanvas.colors.RED):
        #old_font = window._context.font
        window._context.save()
        window._context.font = "{}px {}".format( self._size, self._family )
        window._context.fillStyle=color
        window._context.fillText(text, x, y)
        #window._context.font = old_font
        window._context.restore()
