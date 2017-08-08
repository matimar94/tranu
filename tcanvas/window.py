import tranu.shared.window


class TWindow(tranu.shared.window.SharedWindow):

    def _draw(self):
        self._context.save()
        self._context.fillStyle="black"
        self._context.fillRect(0, 0, self.width, self.height)
        #self._context.clearRect(0, 0, self.width, self.height)
        self._context.restore()
        self.draw()

    def draw_rect(self, x, y, w, h):
        self._context.rect(x, y, w, h)
        self._context.stroke()

    def draw_circle(self, x, y, r):
        self._context.beginPath()
        self._context.arc(x, y, r, 0, 2 * Math.PI)
        self._context.stroke()

    #def create_preloader(self):
        #return tranu.preloader.TPreloader()

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

    def _key_pressed(self, ev):
        if self.get_key_state(ev.code) == False:
            self.key_pressed(ev.code)

    def _key_released(self, ev):
        self.key_released(ev.code)

    def _mouse_pressed(self, ev):
        #btn = (tranu.mousecodes.LEFT, tranu.mousecodes.MIDDLE, tranu.mousecodes.RIGHT)[ev.button]
        x, y = self._fix_mouse(ev)

        self.mouse_pressed(ev.button, x, y)

    def _mouse_released(self, ev):
        #btn = (tranu.mousecodes.LEFT, tranu.mousecodes.MIDDLE, tranu.mousecodes.RIGHT)[ev.button]
        x, y = self._fix_mouse(ev)

        self.mouse_released(ev.button, x, y)


    @property
    def context(self):
        return self._context

    def _fix_mouse(self, evt):
        rect = self._wind.getBoundingClientRect()

        return evt.clientX - rect.left, evt.clientY - rect.top

    def _loop(self):
        self.update(1.0/60)
        self._draw()

    def start(self):
        window.addEventListener('keydown', self._key_pressed, False)
        window.addEventListener('keyup', self._key_released, False)

        self._wind.addEventListener('mousedown', self._mouse_pressed, False)
        self._wind.addEventListener('mouseup', self._mouse_released, False)

        self._wind.addEventListener("mousemove", lambda ev: self.set_mouse_pos(*self._fix_mouse(ev)))

        self._interval = setInterval(self._loop, 1000.0 / 60)

    def __init__(self, width, height):
        super().__init__(width, height)

        #self._wind = __new__(PIXI.Application(800, 600))
        self._wind =  self._create_canvas(width, height) #__new__(PIXI.Applicatio)
        self._context = self._wind.getContext("2d")

        self._context.imageSmoothingEnabled = False
