var module = angular.module('testApp', []);

module.controller('testController', function($scope) {
	console.log("Test App Controller");
	$scope.test = "Yes";
});

module.run(function() {
	console.log("Test App");
});