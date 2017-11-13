angular.module("app").controller("loginCtrl", function ($scope, loginService, userService, $state) {

    $scope.user = {};
    
    verificarLogin = function() {
        token = userService.getToken();
        
        console.log(token);
        
        if(token != null) {
            $state.go("home");
        }
    };

    $scope.fazerLogin = function (user) {
        loginService.fazerLogin(user).then(function (data, status) {
                userService.storeToken(data);
                $state.go("home");
            });
    };
    
    verificarLogin();

});