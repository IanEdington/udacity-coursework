var carlike = function(loc){
  var obj = {loc: loc};
  obj.move = move;
  obj.on = on;
  obj.off = off;
  return obj;
};

var move = function(){
  this.loc += 1;
};
var on = function(){ /* some function */ }
var off = function(){ /* some function */ }
