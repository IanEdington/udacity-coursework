var Car = function(loc){
  var obj = {loc: loc};
  extend(obj, Car.methods);
  return obj;
};
Car.methods = {
  move : function(){
    this.loc += 1;
  };
  on : function(){ /* some function */ }
  off : function(){ /* some function */ }
}
