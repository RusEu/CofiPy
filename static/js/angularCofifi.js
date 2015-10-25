(function(){
	var app = angular.module('app')
	app.controller('ctrl', ['$scope', '$http', function($scope, $http) {
		$scope.cofifi_url = "http://127.0.0.1:8000/cofificofifi_users/?format=json";
	    $scope.quote_url = "http://127.0.0.1:8000/quotequote_ideas/?format=json";
	    $scope.cofifi = []
	    $scope.get_usernames = []
	    $scope.UserBidder = function(user) {
	    	if (user == "bidder") {
	    		console.log(user)
	    		return true
	    	}
	    	else {
	    		return false
	    	}
	    }
		$scope.get_cofifi = function() {
			$http.get($scope.cofifi_url).then(function(response) {
		        $scope.cofifi = response.data
			});
		}
		$scope.get_quote = function() {
			$scope.quote = []
			$http.get($scope.quote_url).success(function(response) {
		        $scope.quote = response.data;
		        return $scope.quote;
			});
		}
		$scope.get_cofifi()
		console.log($scope.cofifi)
	}])
})();
