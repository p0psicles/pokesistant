require.config({

    // alias libraries paths
    paths: {
        'domReady': 'domready/domReady',
        'angular': 'angular/angular',
        'angular-route': 'angular-route/angular-route',
        'angular-animate': 'angular-animate/angular-animate',
        'uiBootstrap': 'angular-bootstrap/ui-bootstrap-tpls.min'
    },

    // angular does not support AMD out of the box, put it in a shim
    shim: {
        'angular': {
            exports: 'angular'
        },
        'angular-route': {
            deps: ['angular']
        },
        'angular-animate': {
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