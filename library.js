var Car = function(loc){
  var obj = {loc: loc};
  extend(obj, methods);
  return obj;
};
var methods = {
  move : function(){
    this.loc += 1;
  };
  on : function(){ /* some function */ }
  off : function(){ /* some function */ }
}
