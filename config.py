
#__all__ = ["set_tranu_backend", "get_tranu_backend"]

TRANU_PYSDL2_BACKEND = 0
TRANU_CANVAS_BACKEND = 1

TRANU_DEFAULT_BACKEND = TRANU_PYSDL2_BACKEND

tranu_backend = TRANU_DEFAULT_BACKEND

TRANU_WEB = (TRANU_CANVAS_BACKEND,)
TRANU_NATIVE = (TRANU_PYSDL2_BACKEND,)

TRANU_BACKEND_MAPPER = { "CANVAS":TRANU_CANVAS_BACKEND, "PYSDL2":TRANU_PYSDL2_BACKEND }

def set_tranu_backend(option):
    global tranu_backend

    if option not in TRANU_WEB and option not in TRANU_NATIVE:
        print("Warning: Wrong rendering backend selected, switching to DEFAULT")
        tranu_backend = TRANU_DEFAULT_BACKEND
    else:
        tranu_backend = option


def get_tranu_backend():
    return tranu_backend

def is_backend_web():
    return tranu_backend in TRANU_WEB

def is_backend_native():
    return tranu_backend in TRANU_NATIVE