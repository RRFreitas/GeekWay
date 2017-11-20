angular.module("app").controller("homeCtrl", function ($scope, userService, $state) {
    
    $scope.verificarLogin = function() {
        token = userService.getToken();
        
        console.log(token);
        
        if(token == null) {
            $state.go("login");
        }else {
            $scope.user = userService.getUser();
        }
    };
    
    $scope.sair = function() {
        userService.removeToken();
        userService.removeUser();
        
        $state.go("login");
    }
    
    $scope.verificarLogin();
    
    console.log($scope.user);

});