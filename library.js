var carlike = function(obj, loc){
  obj.loc = loc;
  obj.move = function(){
    obj.loc += 1;
  };
  return obj;
};
