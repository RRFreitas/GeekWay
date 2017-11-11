angular.module("app").config(function ($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/login');

    $stateProvider
        .state('login', {
            url: '/login',
            controller: 'loginCtrl',
            templateUrl: 'view/login.html'
        })
        .state('register', {
            url: '/register',
            templateUrl: 'view/register.html'
        })
});