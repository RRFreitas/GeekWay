var app = angular.module("app", ['ui.router', 'ngCookies', 'ngMessages', 'ngMaterial', 'material.svgAssetsCache']);

app.config(['$qProvider', function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
}]);