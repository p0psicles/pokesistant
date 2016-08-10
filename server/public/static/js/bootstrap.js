/**
 * bootstraps angular onto the window.document node
 */
define([
    'require',
    'angular',
    'app',
    'routes'
], function (require, angular) {
    'use strict';

    require(['domReady!', 'uiBootstrap'], function (document) {
        angular.bootstrap(document, ['myApp']);
    });
});