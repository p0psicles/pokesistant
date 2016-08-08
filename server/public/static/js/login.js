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

        $scope.update = function (user) {
            // $scope.master = angular.copy(user);
            $scope.master = request;
            var data;
            if(user.name && user.password) {
                // PTC
                data = {'username': user.name,'password' : user.password, 'auth': 'ptc'};
                var request = 'http://localhost:8080/getpokemon';
            } else if(user.email && user.password) {
                // Google
                data = {'username': user.email, 'password' : user.password};
                var request = 'http://localhost:8080/getpokemon';
            } else {
                throw new Error('No username or email adres was defined');
            }
            if(request) {
                $http.post(request, data).then(function(response){
                    PokemonService.setPokemons(response.data);
                    console.log(PokemonService.getPokemons());
                    $location.path('/pokemonList');
                });
            }
        };

        $scope.reset = function(){
            $scope.user = angular.copy(scope.master);
        };

    }]);
