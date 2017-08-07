
class SharedFont():

    def __init__(self, size):
        #self._family = "Arial"
        self._size = 16

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def load(self, path, sysfont=True):
        raise NotImplementedError

    def draw(self, window, text, x, y, color):
        raise NotImplementedError

