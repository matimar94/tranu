import tranu.shared.window
#import tranu.pysdl2.sdl2 as sdl2
from . import sdl2
import ctypes


class TGameWindow(tranu.shared.window.SharedWindow):

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

    def draw(self):
        pass

    def __init__(self, width, height):
        super().__init__(width, height)

        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        window = sdl2.SDL_CreateWindow(b"Hello World",
                                  sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
                                  592, 460, sdl2.SDL_WINDOW_SHOWN)
        windowsurface = sdl2.SDL_GetWindowSurface(window)

        #image = sdl2.SDL_LoadBMP(b"exampleimage.bmp")
        #sdl2.SDL_BlitSurface(image, None, windowsurface, None)

        #sdl2.SDL_UpdateWindowSurface(window)
        #sdl2.SDL_FreeSurface(image)

        running = True
        event = sdl2.SDL_Event()

        while running:
            while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break

            self.update(1.0/60)
            self.draw()

        sdl2.SDL_DestroyWindow(window)
        sdl2.SDL_Quit()
