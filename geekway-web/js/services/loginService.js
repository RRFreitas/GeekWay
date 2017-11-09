angular.module("app").factory("loginService", function ($http, config) {

    var _path = config.baseUrl() + "/user";

    var _fazerLogin = function (user) {
        return $http.post(_path + "/login", user);
    };

    var _fazerLogout = function () {
        return $http.post(_path + "/logout");
    };

    return {
        fazerLogin: _fazerLogin,
        fazerLogout: _fazerLogout
    };
});