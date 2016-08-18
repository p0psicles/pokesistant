define([
    'angular',
    // 'ui.bootstrap',
    './services',
    './login',
    './pokemonList',
    './version/version',
    './version/version-directive',
    './version/interpolate-filter'
], function (angular) {
    'use strict';
    return angular.module('myApp.login', ['ngRoute'])
        .controller('LoginCtrl', ['$scope', '$http', 'PokemonService', '$location', function ($scope, $http, PokemonService, $location) {
            $scope.master = {};
            $scope.loading = false;

            $scope.getPokemonList = function () {
                $http.get('/getPokemon').then(function (response) {
                    PokemonService.setPokemons(response.data.pokemons);
                    console.log(PokemonService.getPokemons());
                    $location.path('/pokemonList');
                });
            };
            $scope.update = function (user) {
                // $scope.master = angular.copy(user);
                $scope.master = undefined;
                var data;
                if (typeof user !== "undefined") {
                    if (user.name && user.password) {
                        // PTC
                        data = {'username': user.name, 'password': user.password, 'auth': 'ptc'};
                        var requestPogoSession = '/getPogoSession';
                    } else if (user.email && user.password) {
                        // Google
                        data = {'username': user.email, 'password': user.password};
                        var requestPogoSession = '/getPogoSession';
                    } else {
                        $scope.error = true;
                        $scope.errorMessage = 'No username/email and/or password was defined';
                    }
                } else {
                    $scope.error = true;
                    $scope.errorMessage = 'Please enter login credentials';
                }
                if (requestPogoSession) {
                    $scope.loading = true;
                    $http.post(requestPogoSession, data).then(function successCallback(response) {
                        $scope.loading = false;
                        if (response.data.authenticated) {
                            $scope.getPokemonList();
                        }
                    }, function errorCallback(error) {
                        $scope.loading = false;
                        $scope.error = true;
                        $scope.errorMessage = 'Unable to login. Error code: ' + error.status;
                        console.error('Unable to login because of error code ' + error.status);
                    });
                }
            }
            ;

            $scope.reset = function () {
                $scope.user = angular.copy(scope.master);
            };

        }
        ]);
});