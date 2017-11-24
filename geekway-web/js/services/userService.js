angular.module("app").factory("userService", function($cookies, $http, config) {

    var _path = config.baseUrl() + "";
    
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
        $cookies.putObject("user", user);
    };
    
    var _removeUser = function (user) {
        $cookies.remove("user");
    };

    var _getUser = function () {
        return $cookies.getObject("user");
    };
    
    var _requestUser = function(id) {
          return $http.get(_path + "/users/" + id);
    };

    return {
            removeToken: _removeToken,
    		getToken: _getToken,
            storeToken: _storeToken,
            removeUser: _removeUser,
    		getUser: _getUser,
            storeUser: _storeUser,
            requestUser: _requestUser
    };
});