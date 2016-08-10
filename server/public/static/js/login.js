'use strict';

angular.module('myApp.login', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/login', {
            templateUrl: 'static/partials/login.html',
            controller: 'LoginCtrl'
        });
    }])

    .controller('LoginCtrl', ['$scope', '$http', 'PokemonService', '$location', function($scope,$http,PokemonService, $location) {
        $scope.master = {};
        
        $scope.getPokemonList = function() {
            $http.get('/getPokemon').then(function(response){
                PokemonService.setPokemons(response.data.pokemons);
                console.log(PokemonService.getPokemons());
                $location.path('/pokemonList');
            });
        }

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
                $http.post(requestPogoSession, data).then(function(response){
                    if (response.data.authenticated) {
                        $scope.getPokemonList();
                    }
                });
            }
            
        };

        $scope.reset = function(){
            $scope.user = angular.copy(scope.master);
        };

    }]);
