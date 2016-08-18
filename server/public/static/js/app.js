define([
    'angular',
    'uiBootstrap',
    'angular-route',
    './services',
    './login',
    './pokemonList',
    './version/version',
    './version/version-directive',
    './version/interpolate-filter'
], function (angular) {
    'use strict';
    // Declare app level module which depends on views, and components
    return angular.module('myApp', [
        'ui.bootstrap',
        'ngRoute',
        'myApp.services',
        'myApp.login',
        'myApp.pokemonList',
        'myApp.version'
    ]);
});
