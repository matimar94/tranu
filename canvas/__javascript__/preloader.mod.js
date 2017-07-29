	__nest__ (
		__all__,
		'tranu.canvas.preloader', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var tranu = {};
					__nest__ (tranu, 'shared.preloader', __init__ (__world__.tranu.shared.preloader));
					__nest__ (tranu, 'canvas.image', __init__ (__world__.tranu.canvas.image));
					var TPreloader = __class__ ('TPreloader', [tranu.shared.preloader.SharedPreloader], {
						get _increase_preload () {return __get__ (this, function (self) {
							self._loaded++;
							if (self._loaded >= self._total) {
								self.preload_ready ();
							}
						});},
						get _load_image () {return __get__ (this, function (self, path) {
							var img = tranu.canvas.image.TImage ();
							img.load (path, self._increase_preload ());
							return img;
						});},
						get __init__ () {return __get__ (this, function (self) {
							__super__ (TPreloader, '__init__') (self);
						});}
					});
					__pragma__ ('<use>' +
						'tranu.canvas.image' +
						'tranu.shared.preloader' +
					'</use>')
					__pragma__ ('<all>')
						__all__.TPreloader = TPreloader;
					__pragma__ ('</all>')
				}
			}
		}
	);
