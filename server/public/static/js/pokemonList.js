'use strict';

angular.module('myApp.pokemonList', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/pokemonList', {
            templateUrl: 'static/partials/pokemonList.html',
            controller: 'PokemonListCtrl'
        });
    }])

    .controller('PokemonListCtrl', ['$scope', 'PokemonService', function($scope,PokemonService) {
        $scope.pokemonList = PokemonService.getPokemons();
    }]);