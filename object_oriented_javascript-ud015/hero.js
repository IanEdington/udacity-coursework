var hero = aHero();
var newSaga = function(){
  var foil = aFoil();
  var saga = function(){
    var deed = aDeed();
    log(hero+deed+foil);
  };
  saga();
  saga();
};
newSaga();
newSaga();
