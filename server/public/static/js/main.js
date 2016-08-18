require.config({

    // alias libraries paths
    paths: {
        'domReady': 'requirejs-domready/domReady',
        'angular': 'angular/angular',
        'angular-route': 'angular-route/angular-route',
        'uiBootstrap': 'angular-bootstrap/ui-bootstrap'
    },

    // angular does not support AMD out of the box, put it in a shim
    shim: {
        'angular': {
            exports: 'angular'
        },
        'angular-route': {
            deps: ['angular']
        },
        'uiBootstrap': {
            deps: ['angular'],
            exports: 'uiBootstrap'
        }
    },

    // kick start application
    deps: ['./bootstrap']
});