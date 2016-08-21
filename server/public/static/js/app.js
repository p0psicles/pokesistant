define([
    'angular',
    'uiBootstrap',
    'angular-route',
    'angular-animate',
    'dialog-service',
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
        'ngAnimate',
        'myApp.services',
        'myApp.login',
        'myApp.pokemonList',
        'myApp.version',
        'dialogs.main'
    ]);
});
