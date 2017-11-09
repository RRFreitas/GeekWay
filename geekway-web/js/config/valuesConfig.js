angular.module("app").value("config", {

	baseUrl: function() {

		var _protocol = "http://"
		var _externalDNS = "localhost";
		var _externalIP = "0.0.0.0";
		var _internalIP = "0.0.0.0";
		var _port = "5000";
		var _context = "/api";

		var url = location.href;

		if (url.indexOf(_externalDNS) >= 0 || url.indexOf(_externalIP) >= 0)
			return _protocol + _externalDNS + ":" + _port + _context;
		else
			return _protocol + _internalIP + ":" + _port + _context;
	}

})