angular.module("app").factory("userService", function($cookies) {

    var _storeToken = function (token) {
        $cookies.putObject("token", token);
    };

    var _removeToken = function (token) {
        $cookies.remove("token");
    };

    var _getToken = function () {
        return $cookies.getObject("token");
    };
    
    var _storeUser = function(user) {
        
    };

    return {
            removeToken: _removeToken,
    		getToken: _getToken,
            storeToken: _storeToken
    };
});