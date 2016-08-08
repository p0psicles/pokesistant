'use strict';

angular.module('myApp.login', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/login', {
            templateUrl: 'static/partials/login.html',
            controller: 'LoginCtrl'
        });
    }])

    .controller('LoginCtrl', ['$scope', '$http', function($scope,$http) {
        $scope.master = {};

        $scope.update = function (user) {
            // $scope.master = angular.copy(user);
            $scope.master = request;

            if(user.name && user.password) {
                // PTC
                var request = 'http://localhost:8080/getpokemon?username='+user.name+'&password='+user.password+'&auth=ptc';
            } else if(user.email && user.password) {
                // Google
                var request = 'http://localhost:8080/getpokemon?username='+user.email+'&password='+user.password;
            } else {
                throw new Error('No username or email adres was defined');
            }
            if(request) {
                $http.get(request).then(function(response){
                    console.log(response);
                });
            }
        };

        $scope.reset = function(){
            $scope.user = angular.copy(scope.master);
        };

    }]);