angular.module("app").controller("registerCtrl", function($scope, registerService, userService, $mdToast, $state) {
    
    $scope.user = {};
    
    $scope.fazerRegistro = function(user) {
        user.data_nasc = moment(user.data_nasc).format('YYYY-MM-DD');
        registerService.fazerRegistro(user)
            .then(function(data) {
                $state.go("login");
                $mdToast.show(
                        $mdToast.simple()
                        .textContent("Registrado com sucesso.")
                        .highlightClass('md-primary')
                        .position('top left')
                        .action('OK')
                        .hideDelay(6000)
                    );
            }, function(data) {
                if(data["status"] == 409) {
                   $scope.user.email = "";
                   $mdToast.show(
                        $mdToast.simple()
                        .textContent(data["data"])
                        .highlightClass('md-warn')
                        .position('top left')
                        .action('OK')
                        .hideDelay(6000)
                    );
                }
            });
    };
    
});