var Car = function(loc){
  this.loc = loc;
};

Car.prototype.move = function(){
    this.loc += 1;
};
Car.prototype.on = function(){ /* some function */ };
Car.prototype.off = function(){ /* some function */ };
