angular.module("app").controller("homeCtrl", function ($scope, userService, $state) {

    verificarLogin = function() {
        user = userService.getUser();
        
        console.log(user);
        
        if(user == null) {
            $state.go("login");
        }
    };
    
    verificarLogin();

});