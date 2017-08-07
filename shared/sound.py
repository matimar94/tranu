
class SharedSound():

    def play(self, volume=1.0):
        return NotImplementedError("Define play for Sound")

    def pause(self):
        return NotImplementedError("Define pause for Sound")

    def stop(self):
        return NotImplementedError("Define stop for Sound")

    @property
    def duration(self):
        return NotImplementedError("Define duration for Sound")

    def load(self, path, onloadfunc=None):
        return NotImplementedError("Sound loader not defined for target backend")

    def __init__(self):
        self._impl = None
