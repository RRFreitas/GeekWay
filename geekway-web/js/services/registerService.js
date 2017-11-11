angular.module("app").factory("registerService", function($http, config) {
   var _path = config.baseUrl();
    
    var _fazerRegistro = function(user) {
        return $http.post(_path + "/register", user);
    };
    
    return {
        fazerRegistro: _fazerRegistro
    };
});