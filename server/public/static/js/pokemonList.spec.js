'use strict';

describe('myApp.pokemonList module', function() {

    beforeEach(module('myApp.pokemonList'));

    describe('pokemonList controller', function(){

        it('should ....', inject(function($controller) {
            //spec body
            var pokemonListCtrl = $controller('PokemonListCtrl');
            expect(pokemonListCtrl).toBeDefined();
        }));

    });
});