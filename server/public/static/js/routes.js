define(['./app'], function (app) {
    'use strict';
    return app.config(['$locationProvider', '$routeProvider', function ($locationProvider, $routeProvider) {
        $locationProvider.hashPrefix('!');

        $routeProvider.when('/login', {
            templateUrl: 'static/partials/login.html',
            controller: 'LoginCtrl'
        });

        $routeProvider.when('/pokemonList', {
            templateUrl: 'static/partials/pokemonList.html',
            controller: 'PokemonListCtrl'
        });

        $routeProvider.otherwise({redirectTo: '/login'});
    }]);
});