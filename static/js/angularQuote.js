(function(){
	var app = angular.module('app')
	app.controller('NgQuote', ['$scope', '$http', function($scope, $http) {
	    $scope.quote_url = "http://127.0.0.1:8000/apiquote_ideas/?format=json";
	    $scope.quotes = []
	    $scope.msg = []
	    $scope.get_data = function() {
	    	if ($scope.quotes[0]) {
			    $scope.msg = $scope.quotes[0]
	    		return $scope.quotes
	    	}
	    	else {
	    		$http.get($scope.quote_url).then(function(response) {
			        $scope.quotes = response.data;
			        $scope.msg = $scope.quotes[0]
			        return $scope.quotes
				});
	    	}
	    }
	    $scope.get_data()
	    $scope.cofifi_user = function() {
	    	$scope.get_data()
	    }
	    $scope.CheckVotes = function(id,user) {
	    	$scope.voted = []
	    	angular.forEach($scope.quotes[id].votes_received, function (item, index) {
		    	$scope.voted.push(item.user)
		    });
		    if ($scope.voted.indexOf(user) >= 0) {
		    	return true
		    }
		    else {
		    	return false
		    }
	    }
	}])
})();
