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

            $scope.getPokemonList = function() {
                $http.get('/getPokemon').then(function(response){
                    PokemonService.setPokemons(response.data);
                    console.log(PokemonService.getPokemons());
                    $location.path('/pokemonList');
                });
            };
            $scope.update = function (user) {
                // $scope.master = angular.copy(user);
                $scope.master = undefined;
                var data;
                if(user.name && user.password) {
                    // PTC
                    data = {'username': user.name,'password' : user.password, 'auth': 'ptc'};
                    var requestPogoSession = 'http://localhost:8080/getPogoSession';
                } else if(user.email && user.password) {
                    // Google
                    data = {'username': user.email, 'password' : user.password};
                    var requestPogoSession = '/getPogoSession';
                } else {
                    throw new Error('No username or email adres was defined');
                }
                if(requestPogoSession) {
                    $scope.loading = true;
                    $http.post(requestPogoSession, data).then(function(response){
                        $scope.loading = false;
                        if (response.data.authenticated) {
                            $scope.getPokemonList();
                        }
                    });
                }
            };

            $scope.reset = function () {
                $scope.user = angular.copy(scope.master);
            };

        }]);
});