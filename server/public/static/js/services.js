angular.module('myApp.services', [

]).service('PokemonService', function () {
    var _pokemonList = {};

    return {
        getPokemons: function () {
            return _pokemonList;
        },

        setPokemons: function (pokemonList) {
            _pokemonList = pokemonList;
        }
    }
});