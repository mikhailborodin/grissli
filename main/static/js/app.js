var app = angular.module("app", []);
app.factory('api', function ($q, $http) {
  function getUrl() {
    var defer = $q.defer();
    $http.get('/api/v1/url/?format=json').
      success(function (data){
        defer.resolve(data);
      });
    return defer.promise
  }
  function getResult(id) {
    var defer = $q.defer();
    $http.get('/api/v1/result/?format=json&' + 'url_id=' + id).
      success(function (data){
        defer.resolve(data);
      });
    return defer.promise
  }
  return {
    getUrl: getUrl,
    getResult: getResult
  }
});
app.controller('Ctrl', function($scope, $timeout, $http, api) {
  api.getUrl().then(function(data) {
    var urls = [];
    var results = [];
    angular.forEach(data.objects, function(value){
      var delay = (parseInt(value.minute) * 60 + parseInt(value.second)) * 1000;
      urls.push(value.datetime + ' ' + value.url);
      $scope.urls = urls;
      $timeout(function (){
        api.getResult(value.id).then(function(data) {
          results.push(data.objects[0].url.url + '-' + data.objects[0].title + ' - ' + data.objects[0].encoding);
          $scope.results = results;
        });
      }, delay);
    })
  });
});