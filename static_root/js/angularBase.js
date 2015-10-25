(function(){
	var app = angular.module('app',['ngAnimate','ui-bootstrap'])
	.config(['$interpolateProvider', function ($interpolateProvider) {
	    $interpolateProvider.startSymbol('[[');
	    $interpolateProvider.endSymbol(']]');
	}]);
	app.controller('NgMenu', ['$scope', function($scope) {
		$scope.dropdown = {};
        $scope.changeClass = function(dropdown){
          if ($scope.dropdown[dropdown] !== "dropdownToggleActive") {
            $scope.dropdown[dropdown] = "dropdownToggleActive";
          }
          else {
            $scope.dropdown[dropdown] = "dropdownToggleDissabled";
          }
          console.log($scope.dropdown[dropdown])
        };
	}])
})();
