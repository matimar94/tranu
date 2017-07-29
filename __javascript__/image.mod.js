	__nest__ (
		__all__,
		'tranu.image', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var tranu = {};
					__nest__ (tranu, 'config', __init__ (__world__.tranu.config));
					if (__in__ (tranu.config.get_tranu_backend (), tranu.config.TRANU_WEB)) {
						var TImage = __init__ (__world__.tranu.canvas.image).TImage;
					}
					else if (__in__ (tranu.config.tranu_backend, tranu.config.TRANU_NATIVE)) {
						try {
						}
						catch (__except0__) {
						}
					}
					else {
					}
					__pragma__ ('<use>' +
						'tranu.canvas.image' +
						'tranu.config' +
					'</use>')
					__pragma__ ('<all>')
						__all__.TImage = TImage;
					__pragma__ ('</all>')
				}
			}
		}
	);
