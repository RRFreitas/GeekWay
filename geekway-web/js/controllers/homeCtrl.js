angular.module("app").controller("homeCtrl", function ($scope, userService, $state) {
    
    $scope.user = {};

    verificarLogin = function() {
        token = userService.getToken();
        
        console.log(token);
        
        if(token == null) {
            $state.go("login");
        }
    };
    
    verificarLogin();

});