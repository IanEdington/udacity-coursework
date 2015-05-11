var Car = function(loc){
  var obj = Object.create(Car.methods);
  obj.loc = loc;
  return obj;
};
Car.methods = {
  move : function(){
    this.loc += 1;
  };
  on : function(){ /* some function */ }
  off : function(){ /* some function */ }
}
