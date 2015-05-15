var HTMLcat = '<div id="Cat-%catname%" class="col-md-6"> <div id="%catname%-header" class="center-content clearfix"> </div> <div id="%catname%-cat-pic"> <img src="%url%" class="img-responsive"></div><div id="%catname%-Counter" class="counter"> 0 </div> </div>';

var Cat = function(catname, url){
	this.catname = catname;
  this.catPic = this.catname+"-cat-pic";
  this.countName = this.catname+"-Counter";
	this.url = url;
  this.counter = 0;
  this.HTML = HTMLcat.replace(/%catname%/g, catname).replace(/%url%/g, url);
};
Cat.prototype.clicker = function(){
  var counter = this.counter;
  var countName = this.countName;
	$('#'+this.catPic).click(function(e) {
    console.log('clicker was clicked' + counter);
    counter+=1;
		$('#'+countName).html(counter);
	});
  console.log('clicker was called');
};
