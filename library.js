var carlike = function(obj, loc){
  obj.loc = loc;
  obj.move = move;
  return obj;
};

var move = function(){
  this.loc += 1;
};
