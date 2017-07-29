import tranu.shared.preloader

class SharedWindow():

    def key_pressed(self, key):
        self._keys[key] = True

    def key_released(self, key):
        self._keys[key] = False

    def mouse_pressed(self, button):
        self._mouse[button] = True

    def mouse_released(self, button):
        self._mouse[button] = False

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

        self.preload( self._preloader )