var Car = function(loc){
  this.loc = loc;
};
Car.prototype.move = function(){
  this.loc+=1;
};

// SUB-Classing
  // there are always two parts to a class
  // both need to be inherited for the
  // SUB-classing to work
var Van = function(loc){
  //1.create the unique elements
  //inherited from the Car constuctor
  Car.call(this, loc);
};
//2.make the van prototype inherite from
//the car prototype.
Van.prototype = Object.create(Car.prototype);
Van.prototype.constructor = Van;

Van.prototype.grab = function{ /*...*/ };

// another example
var Cop = function(loc, radio){
  Car.call(this, loc);
  this.radio = radio;
};
Cop.prototype = Object.create(Car.prototype);
Cop.prototype.constructor = Cop;

Cop.prototype.call = function{ /*...*/ };
