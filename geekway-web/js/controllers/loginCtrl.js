angular.module("app").controller("loginCtrl", function ($scope, loginService) {

    $scope.user = {}

    $scope.fazerLogin = function (user) {
        loginService.fazerLogin(user).then(function (data, status) {
                console.log('test')
                userService.storeUser(data);
                $state.go("home");
            });
    };

});