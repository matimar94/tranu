	__nest__ (
		__all__,
		'tranu.shared.window', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var tranu = {};
					__nest__ (tranu, 'shared.preloader', __init__ (__world__.tranu.shared.preloader));
					var SharedWindow = __class__ ('SharedWindow', [object], {
						get key_pressed () {return __get__ (this, function (self, key) {
							self._keys [key] = true;
						});},
						get key_released () {return __get__ (this, function (self, key) {
							self._keys [key] = false;
						});},
						get mouse_pressed () {return __get__ (this, function (self, button) {
							self._mouse [button] = true;
						});},
						get mouse_released () {return __get__ (this, function (self, button) {
							self._mouse [button] = false;
						});},
						get py_update () {return __get__ (this, function (self, dt) {
							var __except0__ = NotImplementedError ("TARGET BACKEND DOESN'T IMPLEMENT UPDATE");
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get draw () {return __get__ (this, function (self) {
							var __except0__ = NotImplementedError ("TARGET BACKEND DOESN'T IMPLEMENT DRAW");
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get _loop () {return __get__ (this, function (self) {
							self.py_update (0.016);
							self.draw ();
						});},
						get start () {return __get__ (this, function (self) {
							var __except0__ = NotImplementedError ("TARGET BACKEND DOESN'T IMPLEMENT START");
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get preload () {return __get__ (this, function (self, preloader) {
							// pass;
						});},
						get create_preloader () {return __get__ (this, function (self) {
							var __except0__ = NotImplementedError ('PRELOADER NOT IMPLEMENTED FOR TARGET BACKEND');
							__except0__.__cause__ = null;
							throw __except0__;
						});},
						get __init__ () {return __get__ (this, function (self, width, height) {
							self.width = width;
							self.height = height;
							self._keys = dict ({});
							self._mouse = function () {
								var __accu0__ = [];
								for (var x = 0; x < 3; x++) {
									__accu0__.append (false);
								}
								return __accu0__;
							} ();
							self._preloader = self.create_preloader ();
							self.preload (self._preloader);
						});}
					});
					__pragma__ ('<use>' +
						'tranu.shared.preloader' +
					'</use>')
					__pragma__ ('<all>')
						__all__.SharedWindow = SharedWindow;
					__pragma__ ('</all>')
				}
			}
		}
	);
