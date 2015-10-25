(function(){
	var app = angular.module('app',['ngAnimate','ui.bootstrap'])
	.config(['$interpolateProvider', function ($interpolateProvider) {
	    $interpolateProvider.startSymbol('[[');
	    $interpolateProvider.endSymbol(']]');
	}]);
	app.controller('NgMenu', ['$scope', function($scope) {
		$scope.dropdown = {};
        $scope.changeClass = function(dropdown){
          if (dropdown == "myMenu") {
            if ($scope.dropdown[dropdown] !== "in") {
	            $scope.dropdown[dropdown] = "in";
	          }
			else {
			$scope.dropdown[dropdown] = "out";
			}
          }
          else {
	          if ($scope.dropdown[dropdown] !== "open") {
	            $scope.dropdown[dropdown] = "open";
	          }
	          else {
	            $scope.dropdown[dropdown] = "closed";
	          }
          }
          console.log($scope.dropdown[dropdown])
        };
	}])
})();
