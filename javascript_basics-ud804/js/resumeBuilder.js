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


function getRelationship(x, y) {
    if (typeof x === 'number' && ! isNaN(x)) {
        if (typeof y === 'number' && ! isNaN(y)) {
            if (x === y) {
                return '=';
            } else if (x < y) {
                return '<';
            } else if (x > y) {
                return '>';
            }
        } else  {
            return 'Can\'t compare relationships because ' + y + ' is not a number';
        }
    } else {
        if (typeof y === 'number' && ! isNaN(y)) {
            return "Can\'t compare relationships because " + x + " is not a number";
        } else {
            return 'Can\'t compare relationships because ' + x + ' and ' + y + ' are not numbers';
        }
    }
}

// Try logging these functions to test your code!
console.log(getRelationship(1,4));
console.log(getRelationship(1,1));
console.log(getRelationship("that",2));
console.log(getRelationship("this"," something else"));
console.log(getRelationship(3));
console.log(getRelationship("hi"));
console.log(getRelationship(NaN));
console.log(getRelationship(NaN, undefined));
