// $("#main").append('Ian Edington');

// var awesomeThoughts = 'I am Ian and I am AWESOME!';
// console.log(awesomeThoughts);

// var funThoughts = awesomeThoughts.replace('AWESOME', 'FUN');
// $('#main').append(funThoughts);

var formatedName = HTMLheaderName.replace('%data%','Ian Edington');
var formatedRole = HTMLheaderRole.replace('%data%','Product Manager');
var skills = ['awesomeness', 'programming', 'teaching', 'BizDev'];

var bio = {
	"name" : "Ian Edington",
	"age" : 28,
	"skills" : skills
};


$('#header').append(formatedName);
$('#header').append(formatedRole);
$('#main').append(bio.age);

// if(Array.isArray(skills) && skills.length > 0) {
// 	$('#header').append(HTMLskillsStart);
//
// 	var formatedSkills ='';
//
//   for (index in skills) {
// 	  formatedSkills = formatedSkills.concat(HTMLskills.replace('%data%', bio.skills[index]));
// 	}
// 	$('#main').append(formatedSkills);
// }


// $(document).click(function(loc) {
// 	var x = loc.pageX;
// 	var y = loc.pageY;
//
// 	logClicks(x,y);
// });

function inName(name) {
	name = name.split(' ');
	console.log(name);
	name[1] = name[1].toUpperCase();
	name[0] = name[0].slice(0,1).toUpperCase() + name[0].slice(1).toLowerCase();

	return name[0] + ' ' + name[1];
}

$('#main').append(internationalizeButton);
