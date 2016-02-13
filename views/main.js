// create the module and name it angryCartels
var counterpoint = angular.module('counterpoint', ['ngRoute']);

// configure our routes
counterpoint.config(function($routeProvider, $locationProvider) {
	$routeProvider

		// route for the home page
		.when('/', {
			templateUrl : 'pages/home.html',
			controller  : 'homeController'
		})

		// use the HTML5 History API to get the pretty urls without a weird /#/ between relevant info
        $locationProvider.html5Mode(true);
});