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

    return angular.module('myApp.pokemonList', ['ngRoute'])

        .controller('PokemonListCtrl', ['$scope', '$http', 'PokemonService', 'dialogs', function ($scope, $http, PokemonService, dialogs) {
            $scope.pokemonList = PokemonService.getPokemons();
            $scope.updateList = function () {
                $http.get('/pokemon').then(function (response) {
                    PokemonService.setPokemons(response.data.pokemons);
                    $scope.pokemonList = PokemonService.getPokemons();
                });
            };
            $scope.openMoveDetails = function (moveId) {
                dialogs.create('static/partials/moveDetails.html', 'moveDetailsController', moveId, {}, 'ctrl');
            };
        }])
        .controller('moveDetailsController', function ($scope, $uibModalInstance, $http, $filter, data) {
            $scope.data = data;
            $http.get('/static/json/GAME_DATA_MOVES.json').then(function (response) {
                $scope.moveDetails = $filter('filter')(response.data, {ID: $scope.data}, true)[0];
                $scope.header = $scope.moveDetails.Name;
            });
            $scope.done = function () {
                $uibModalInstance.close($scope.data);
            };
        });
});
