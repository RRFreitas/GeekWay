angular.module("app").factory("userService", function($cookies) {

    var _storeUser = function (user) {
        $cookies.putObject("user", user);
    };

    var _removeUser = function (user) {
        $cookies.remove("user");
    };

    var _getUser = function () {
        return $cookies.getObject("user");
    };

    return {
            removeUser: _removeUser,
    		getUser: _getUser,
            storeUser: _storeUser
    };
});