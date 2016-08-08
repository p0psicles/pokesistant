'use strict';

/* https://github.com/angular/protractor/blob/master/docs/toc.md */

describe('my app', function() {


  it('should automatically redirect to /login when location hash/fragment is empty', function() {
    browser.get('index.html');
    expect(browser.getLocationAbsUrl()).toMatch("/login");
  });


  describe('login', function() {

    beforeEach(function() {
      browser.get('index.html#!/view1');
    });


    it('should render login when user navigates to /login', function() {
      expect(element.all(by.css('[ng-view] p')).first().getText()).
        toMatch(/Login option:/);
    });

  });


  describe('pokemonList', function() {

    beforeEach(function() {
      browser.get('index.html#!/pokemonList');
    });


    it('should render pokemonList when user navigates to /view2', function() {
      expect(element.all(by.css('[ng-view] .pokemonTile')).first().isPresent()).toBe(true);
    });

  });
});
