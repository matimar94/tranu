import tranu.shared.sound

class TSound(tranu.shared.sound.SharedSound):

    def play(self, volume=1.0):
        self._impl.volume(volume)
        self._impl.play()

    def pause(self):
        return NotImplementedError("Define pause for Sound")

    def stop(self):
        return NotImplementedError("Define stop for Sound")

    @property
    def duration(self):
        return self._impl.duration()

    def load(self, path, onloadfunc=None):
        if onloadfunc is not None:
            self._impl = __new__(Howl({"src":[path], "onload":onloadfunc}))
        else:
            self._impl = __new__(Howl({"src":[path]}))
        #self._impl.src = path

        #if onloadfunc:
            #self._impl.onload = onloadfunc

        return self._impl


    def __init__(self):
        super().__init__()
