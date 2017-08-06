import tranu.config


if tranu.config.get_tranu_backend() in tranu.config.TRANU_WEB:
    from org.transcrypt.stubs.browser import __pragma__
    from tranu.tcanvas.image import TImage
elif tranu.config.tranu_backend in tranu.config.TRANU_NATIVE:
    # This horrible desktop-web-pragma trick has to disappear soon
    try:
        __pragma__ ('skip')
    except:
        pass

    if tranu.config.get_tranu_backend() == tranu.config.TRANU_PYSDL2_BACKEND:
        from tranu.tpysdl2.image import TImage
    elif tranu.config.get_tranu_backend() == tranu.config.TRANU_PYGLET_BACKEND:
        from tranu.tpyglet.image import TImage
    try:
        __pragma__ ('noskip')
    except:
        pass
else:
    print("ERROR: DESIRED RENDERING BACKEND NOT FOUND")