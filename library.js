var Car = function(loc){
  var obj = {loc: loc};
  obj.move = function(){
    obj.loc+=1;
  };
  return obj;
};

var Van = function(loc){
  var obj = Car(loc);
  obj.grab = function{ /*...*/ };
  return obj;
}

var Cop = function(loc){
  var obj = Car(loc);
  obj.call = function{ /*...*/ };
  return obj;
}
