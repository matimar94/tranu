	__nest__ (
		__all__,
		'tranu.canvas.window', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var tranu = {};
					__nest__ (tranu, 'shared.window', __init__ (__world__.tranu.shared.window));
					__nest__ (tranu, 'canvas.preloader', __init__ (__world__.tranu.canvas.preloader));
					var TWindow = __class__ ('TWindow', [tranu.shared.window.SharedWindow], {
						get py_update () {return __get__ (this, function (self, dt) {
							// pass;
						});},
						get create_preloader () {return __get__ (this, function (self) {
							return tranu.canvas.preloader.TPreloader ();
						});},
						get _create_canvas () {return __get__ (this, function (self, w, h) {
							var canvas = document.createElement ('canvas');
							canvas.id = 'CANVAS';
							canvas.width = w;
							canvas.height = h;
							canvas.style.zIndex = 8;
							canvas.style.position = 'absolute';
							canvas.style.border = '1px solid';
							document.body.appendChild (canvas);
							return canvas;
						});},
						get context () {return __get__ (this, function (self) {
							return self._context;
						});},
						get start () {return __get__ (this, function (self) {
							self._interval = setInterval (self._loop, 1000.0 / 60);
						});},
						get __init__ () {return __get__ (this, function (self, width, height) {
							__super__ (TWindow, '__init__') (self, width, height);
							self._wind = self._create_canvas (width, height);
							self._context = self._wind.getContext ('2d');
						});}
					});
					__pragma__ ('<use>' +
						'tranu.canvas.preloader' +
						'tranu.shared.window' +
					'</use>')
					__pragma__ ('<all>')
						__all__.TWindow = TWindow;
					__pragma__ ('</all>')
				}
			}
		}
	);
