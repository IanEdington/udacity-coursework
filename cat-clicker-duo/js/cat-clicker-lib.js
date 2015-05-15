var HTMLcat = '<div id="Cat-%catname%" class="col-xs-6"> <div id="%catname%-header" class="center-content clearfix"> %catname% </div> <div id="%catname%-cat-pic"> <img src="%url%" class="property-thumbnail img-responsive"></div><div id="%catname%-Counter" class="counter"> 0 </div> </div>';

var Cat = function(catname, url){
  var catPic = catname+"-cat-pic";
  var countName = catname+"-Counter";
  var counter = 0;
  $('#cat-row1').append(HTMLcat.replace(/%catname%/g, catname).replace(/%url%/g, url));
  $('#'+catPic).click(function(e) {
    console.log('clicker was clicked' + counter);
    counter+=1;
		$('#'+countName).html(counter);
	});
};
