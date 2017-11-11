angular.module("app").controller("registerCtrl", function($scope, registerService, userService) {
    
    $scope.user = {};
    
    $scope.fazerRegistro = function(user) {
        registerService.fazerRegistro(user).then(function (data, status) {
             console.Log("teste");
            if(status == 200) {
                userService.storeUser(data);
                $state.go("home")
            }
        });
    };
    
});