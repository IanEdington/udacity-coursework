var HTMLcat = '<div id="Cat-%catname%" class="col-md-6"> <div id="%catname%-header" class="center-content clearfix"> </div> <div id="%catname%-cat-pic"> <img src="%url%" class="img-responsive"></div><div id="%catname%-Counter" class="%class%"> 0 </div> </div>';

var Cat = function(catname, url){
	this.catname = catname;
  this.catPic = this.catname+"-cat-pic";
  this.countName = this.catname+"-Counter";
	this.url = url;
  this.counter = 0;
  this.HTML = HTMLcat.replace(/%catname%/g, catname).replace(/%url%/g, url);
};
Cat.prototype.clicker = function(){
	$('#'+this.countName).click(function(e) {
    this.counter+=1;
		$('#'+this.countName).html(this.counter.toString());
    console.log('clicker was clicked' + this.counter);
	});
  console.log('clicker was called');
};
