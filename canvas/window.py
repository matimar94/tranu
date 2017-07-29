import tranu.shared.window
import tranu.canvas.preloader

class TWindow(tranu.shared.window.SharedWindow):

    def update(self, dt):
        pass

    def create_preloader(self):
        return tranu.canvas.preloader.TPreloader()

    def _create_canvas(self, w, h):
        canvas = document.createElement('canvas')
        canvas.id = "CANVAS"
        canvas.width = w
        canvas.height = h
        canvas.style.zIndex = 8
        canvas.style.position = "absolute"
        canvas.style.border = "1px solid"

        document.body.appendChild(canvas)

        return canvas

    @property
    def context(self):
        return self._context

    def start(self):
        self._interval = setInterval(self._loop, 1000.0 / 60)

    def __init__(self, width, height):
        super().__init__(width, height)

        #self._wind = __new__(PIXI.Application(800, 600))
        self._wind =  self._create_canvas(width, height) #__new__(PIXI.Applicatio)
        self._context = self._wind.getContext("2d")
