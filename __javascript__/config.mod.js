	__nest__ (
		__all__,
		'tranu.config', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var TRANU_PYSDL2_BACKEND = 0;
					var TRANU_CANVAS_BACKEND = 1;
					var TRANU_DEFAULT_BACKEND = TRANU_PYSDL2_BACKEND;
					var tranu_backend = TRANU_DEFAULT_BACKEND;
					var TRANU_WEB = tuple ([TRANU_CANVAS_BACKEND]);
					var TRANU_NATIVE = tuple ([TRANU_PYSDL2_BACKEND]);
					var TRANU_BACKEND_MAPPER = dict ({'CANVAS': TRANU_CANVAS_BACKEND, 'PYSDL2': TRANU_PYSDL2_BACKEND});
					var set_tranu_backend = function (option) {
						if (!__in__ (option, TRANU_WEB) && !__in__ (option, TRANU_NATIVE)) {
							print ('Warning: Wrong rendering backend selected, switching to DEFAULT');
							tranu_backend = TRANU_DEFAULT_BACKEND;
						}
						else {
							tranu_backend = option;
						}
					};
					var get_tranu_backend = function () {
						return tranu_backend;
					};
					var is_backend_web = function () {
						return __in__ (tranu_backend, TRANU_WEB);
					};
					var is_backend_native = function () {
						return __in__ (tranu_backend, TRANU_NATIVE);
					};
					__pragma__ ('<all>')
						__all__.TRANU_BACKEND_MAPPER = TRANU_BACKEND_MAPPER;
						__all__.TRANU_CANVAS_BACKEND = TRANU_CANVAS_BACKEND;
						__all__.TRANU_DEFAULT_BACKEND = TRANU_DEFAULT_BACKEND;
						__all__.TRANU_NATIVE = TRANU_NATIVE;
						__all__.TRANU_PYSDL2_BACKEND = TRANU_PYSDL2_BACKEND;
						__all__.TRANU_WEB = TRANU_WEB;
						__all__.get_tranu_backend = get_tranu_backend;
						__all__.is_backend_native = is_backend_native;
						__all__.is_backend_web = is_backend_web;
						__all__.set_tranu_backend = set_tranu_backend;
						__all__.tranu_backend = tranu_backend;
					__pragma__ ('</all>')
				}
			}
		}
	);
