	__nest__ (
		__all__,
		'tranu.shared.preloader', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var tranu = {};
					__nest__ (tranu, 'image', __init__ (__world__.tranu.image));
					var SharedPreloader = __class__ ('SharedPreloader', [object], {
						IMAGE: 0,
						SOUND: 1,
						get preload_ready () {return __get__ (this, function (self) {
							if (self._loadfunc) {
								self._loadfunc ();
							}
						});},
						get _load_image () {return __get__ (this, function (self, path) {
							var img = tranu.image.Image ();
							img.load (path);
							return img;
						});},
						get load () {return __get__ (this, function (self, func) {
							self._total = sum (list (map (len, self._resources)));
							self._loaded = 0;
							self._loadfunc = func;
							var __iterable0__ = self._images.py_items ();
							for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
								var img = __iterable0__ [__index0__];
								self._images [img [0]] = self._load_image (img [1]);
							}
						});},
						get add_image () {return __get__ (this, function (self, py_name, image_path) {
							self._images [py_name] = image_path;
						});},
						get get_image () {return __get__ (this, function (self, py_name) {
							return self._images [py_name];
						});},
						get __init__ () {return __get__ (this, function (self) {
							self._images = dict ({});
							self._types = list (['image', 'sound']);
							self._resources = tuple ([self._images]);
						});}
					});
					__pragma__ ('<use>' +
						'tranu.image' +
					'</use>')
					__pragma__ ('<all>')
						__all__.SharedPreloader = SharedPreloader;
					__pragma__ ('</all>')
				}
			}
		}
	);
