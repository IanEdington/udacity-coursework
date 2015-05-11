var Car = function(loc){
  var obj = Object.create(Car.prototype);
  obj.loc = loc;
  return obj;
};
Car.prototype.move = function(){
    this.loc += 1;
};
Car.prototype.on = function(){ /* some function */ };
Car.prototype.off = function(){ /* some function */ };
