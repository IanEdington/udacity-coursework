var move = function(car){
  car.loc += 1;
};

var carlike = function(obj, loc){
  obj.loc = loc;
  obj.move = move;
  return obj;
};
