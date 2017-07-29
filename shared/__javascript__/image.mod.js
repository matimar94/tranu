	__nest__ (
		__all__,
		'tranu.shared.image', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var SharedImage = __class__ ('SharedImage', [object], {
						get draw () {return __get__ (this, function (self, window, x, y) {
							var __except0__ = NotImplementedError ('Define draw for image');
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get draw_src () {return __get__ (this, function (self, window, sx, sy, sw, sh, tx, ty, tw, th) {
							var __except0__ = NotImplementedError ('Define draw_src for image');
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get width () {return __get__ (this, function (self) {
							var __except0__ = NotImplementedError ('Define width property for image');
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get height () {return __get__ (this, function (self) {
							var __except0__ = NotImplementedError ('Define height property for image');
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get load () {return __get__ (this, function (self, path) {
							var __except0__ = NotImplementedError ('Image loader not defined for target backend');
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get __init__ () {return __get__ (this, function (self) {
							self._impl = null;
						});}
					});
					__pragma__ ('<all>')
						__all__.SharedImage = SharedImage;
					__pragma__ ('</all>')
				}
			}
		}
	);
