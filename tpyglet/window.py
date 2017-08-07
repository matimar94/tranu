import tranu.shared.window
import pyglet


class TWindow(tranu.shared.window.SharedWindow):

    def _draw(self):
        self._wind.clear()
        self.draw()

    def draw_rect(self, x, y, w, h):
        pass

    def draw_circle(self, x, y, r):
        pass

    def _key_pressed(self, code, modif):
        if self.get_key_state(code):
            self.key_pressed(code)

    def _key_released(self, code, modif):
        self.key_released(code)

    def _mouse_pressed(self, x, y, button, modif):
        # btn = (tranu.mousecodes.LEFT, tranu.mousecodes.MIDDLE, tranu.mousecodes.RIGHT)[ev.button]

        self.mouse_pressed(button, x, y)

    def _mouse_released(self, x, y, button, modif):
        # btn = (tranu.mousecodes.LEFT, tranu.mousecodes.MIDDLE, tranu.mousecodes.RIGHT)[ev.button]
        # x, y = self._fix_mouse(ev)

        self.mouse_released(button, x, y)

    def start(self):
        self._wind.on_key_press = self._key_pressed
        self._wind.on_key_release = self._key_released

        self._wind.on_mouse_press = self._mouse_pressed
        self._wind.on_mouse_release = self._mouse_released

        self._wind.on_draw = self._draw

        pyglet.clock.schedule_interval(self.update, 1.0 / 60)

    def run(self):
        pyglet.app.run()

    def __init__(self, width, height):
        super().__init__(width, height)

        self._wind = pyglet.window.Window(width, height)
        #self._wind.on_draw = self.draw
