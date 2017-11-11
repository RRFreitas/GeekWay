angular.module("app").controller("loginCtrl", function ($scope, loginService, userService, $state) {

    $scope.user = {};
    
    verificarLogin = function() {
        user = userService.getUser();
        
        console.log(user);
        
        if(user != null) {
            $state.go("home");
        }
    };

    $scope.fazerLogin = function (user) {
        loginService.fazerLogin(user).then(function (data, status) {
                userService.storeUser(data);
                $state.go("home");
            });
    };
    
    verificarLogin();

});