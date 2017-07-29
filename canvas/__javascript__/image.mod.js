	__nest__ (
		__all__,
		'tranu.canvas.image', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var tranu = {};
					__nest__ (tranu, 'shared.image', __init__ (__world__.tranu.shared.image));
					var TImage = __class__ ('TImage', [tranu.shared.image.SharedImage], {
						get draw () {return __get__ (this, function (self, window, x, y) {
							window._context.drawImage (self._impl, x, y);
						});},
						get draw_src () {return __get__ (this, function (self, window, sx, sy, sw, sh, tx, ty, tw, th) {
							window.context.drawImage (self._impl, sx, sy, sw, sh, tx, ty, tw, th);
						});},
						get width () {return __get__ (this, function (self) {
							return self._impl.width;
						});},
						get height () {return __get__ (this, function (self) {
							return self._impl.height;
						});},
						get load () {return __get__ (this, function (self, path, onloadfunc) {
							if (typeof onloadfunc == 'undefined' || (onloadfunc != null && onloadfunc .hasOwnProperty ("__kwargtrans__"))) {;
								var onloadfunc = null;
							};
							self._impl = new Image ();
							self._impl.src = path;
							if (onloadfunc) {
								self._impl.onload = onloadfunc;
							}
							return self._impl;
						});},
						get __init__ () {return __get__ (this, function (self) {
							__super__ (TImage, '__init__') (self);
							self._impl = null;
						});}
					});
					__pragma__ ('<use>' +
						'tranu.shared.image' +
					'</use>')
					__pragma__ ('<all>')
						__all__.TImage = TImage;
					__pragma__ ('</all>')
				}
			}
		}
	);
