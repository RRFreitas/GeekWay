angular.module("app").controller("loginCtrl", function ($scope, loginService, userService, $state) {

    $scope.user = {};
    
    verificarLogin = function() {
        token = userService.getToken();
        
        if(token != null  && userService.getUser() != null) {
            $state.go("home");
        }
    };

    $scope.fazerLogin = function (user) {
        loginService.fazerLogin(user).then(function (data, status) {
                userService.storeToken(data["data"]);
                
                userService.requestUser(data["data"]).then(function (user, status) {
                    userService.storeUser(user["data"]);
                    $state.go("home");
                });
            });
    };
    
    verificarLogin();

});