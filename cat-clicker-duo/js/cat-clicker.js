var ruby = new Cat('ruby', 'cats/ruby.JPG');
$('#cat-row1').html(ruby.HTML);
ruby.clicker();

var jake = new Cat('jake', 'cats/jake.JPG');
$('#cat-row1').append(jake.HTML);
jake.clicker();
