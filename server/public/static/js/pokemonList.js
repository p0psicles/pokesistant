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

        .controller('PokemonListCtrl', ['$scope', '$http', 'PokemonService', function ($scope, $http, PokemonService) {
            $scope.pokemonList = PokemonService.getPokemons();
            $scope.updateList = function () {
                $http.get('/pokemon').then(function (response) {
                    PokemonService.setPokemons(response.data.pokemons);
                    $scope.pokemonList = PokemonService.getPokemons();
                });
            };
        }]);
});