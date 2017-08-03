import tranu.shared.preloader

class SharedWindow():

    def draw_rect(self, x, y, w, h):
        raise NotImplementedError("TARGET BACKEND DOESN'T IMPLEMENT RECTS")

    def draw_circle(self, x, y, r):
        raise NotImplementedError("TARGET BACKEND DOESN'T IMPLEMENT CIRCLES")

    def get_key_state(self, key):
        return self._keys.get(key, False)

    def key_pressed(self, key):
        self._keys[key] = True

    def key_released(self, key):
        self._keys[key] = False

    def mouse_pressed(self, button, x, y):
        self._mouse[button] = True
        self._mouse_x, self._mouse_y = x, y

    def mouse_released(self, button, x, y):
        self._mouse[button] = False
        self._mouse_x, self._mouse_y = x, y

    def mouse_pos(self):
        return self._mouse_x, self._mouse_y

    def set_mouse_pos(self, x, y):
        self._mouse_x = x
        self._mouse_y = y

    def update(self, dt):
        raise NotImplementedError("TARGET BACKEND DOESN'T IMPLEMENT UPDATE")

    def draw(self):
        raise NotImplementedError("TARGET BACKEND DOESN'T IMPLEMENT DRAW")

    def _loop(self):
        self.update(0.016)
        self.draw()

    def start(self):
        raise NotImplementedError("TARGET BACKEND DOESN'T IMPLEMENT START")

    def preload(self, preloader):
        pass

    def create_preloader(self):
        raise NotImplementedError("PRELOADER NOT IMPLEMENTED FOR TARGET BACKEND")

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self._keys = {}
        self._mouse = [ False for x in range(3) ]
        self._preloader = self.create_preloader()

        self._mouse_x = 0
        self._mouse_y = 0

        self.preload( self._preloader )