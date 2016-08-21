require.config({

    // alias libraries paths
    paths: {
        'domReady': 'domReady/domReady',
        'angular': 'angular/angular',
        'angular-route': 'angular-route/angular-route',
        'angular-animate': 'angular-animate/angular-animate',
        'uiBootstrap': 'angular-bootstrap/ui-bootstrap-tpls.min',
        'angular-sanitize': 'angular-sanitize/angular-sanitize',
        'dialog-service': 'angular-dialog-service/dist/dialogs',
        'angular-touch': 'angular-touch/angular-touch'  
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
        'angular-touch': {
            deps: ['angular'],
            exports: 'angular-touch'
        },
        'uiBootstrap': {
            deps: ['angular'],
            exports: 'uiBootstrap'
        },
        'angular-sanitize': {
            deps: ['angular'],
            exports: 'angular-sanitize'
        },
        'dialog-service': {
            deps: ['angular', 'uiBootstrap', 'angular-sanitize'],
            exports: 'dialog-service'
        }
    },

    // kick start application
    deps: ['./bootstrap']
});