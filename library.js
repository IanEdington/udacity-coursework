var carlike = function(obj, loc){
  obj.loc = loc;
  obj.move = function(){
    this.loc += 1;
  };
  return obj;
};
