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

if(Array.isArray(skills) && skills.length > 0) {
	$('#header').append(HTMLskillsStart)
	$('#main').append(skills);
}
