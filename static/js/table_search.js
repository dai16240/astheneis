var options = {
  valueNames: [ 'id', 'first_name', 'last_name', 'phone', 'address' ]
};

// Init list
var userList = new List('users', options);

$("#searchInput").keyup(function () {
    var searchString = $(this).val();
    userList.search(searchString);
});
$('.search').on('keyup', function(event) { // Fired on 'keyup' event
  if($('.list').children().length === 0) { // Checking if list is empty
    $('#users').css('display', 'none');
  } else {
    $('#users').css('display', 'block'); // Hide the Not Found message
  }
});