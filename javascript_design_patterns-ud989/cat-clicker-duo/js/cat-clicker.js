catNames = [
	'ruby',
	'jake',
	'rod',
	'simon',
	'coutny'
];

for (var i in catNames){
	var cat = new Cat(catNames[i], 'cats/'+catNames[i]+'.JPG');
}
