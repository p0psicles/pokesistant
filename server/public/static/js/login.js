define([
    'angular',
    'angular-animate',
    'uiBootstrap',
    './services',
    './login',
    './pokemonList',
    './version/version',
    './version/version-directive',
    './version/interpolate-filter'
], function (angular) {
    'use strict';
    return angular.module('myApp.login', ['ngRoute', 'ui.bootstrap'])
        .controller('LoginCtrl', ['$scope', '$http', 'PokemonService', '$location', function ($scope, $http, PokemonService, $location) {
            $scope.master = {};
            $scope.loading = false;

            $scope.alerts = [];
            $scope.closeAlert = function (index) {
                $scope.alerts.splice(index, 1);
            };

            $scope.getPokemonList = function () {
                $http.get('/pokemon').then(function (response) {
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
                        var requestPogoSession = '/login';
                    } else if (user.email && user.password) {
                        // Google
                        data = {'username': user.email, 'password': user.password};
                        var requestPogoSession = '/login';
                    } else {
                        $scope.alerts.push({type: 'warning', msg: 'No username/email and/or password was defined'});
                    }
                } else {
                    $scope.alerts.push({type: 'warning', msg: 'Please enter login credentials'});
                }
                if (requestPogoSession) {
                    $scope.loading = true;
                    $http.post(requestPogoSession, data).then(function successCallback(response) {
                        $scope.loading = false;
                        if (response.data.authenticated) {
                            $scope.getPokemonList();
                        } else {
                            $scope.alerts.push({type: 'danger', msg: response.data.error_msg});
                        }
                    }, function errorCallback(error) {
                        $scope.loading = false;
                        $scope.alerts.push({type: 'danger', msg: 'Unable to login. Error code: ' + error.status});
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