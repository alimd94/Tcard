$(document).ready(function () {
    $('#loginform').submit(function(e){
        e.preventDefault();
        login();
        console.log("ssssssssssss");
    })

    function login(){
      data = {
        'username' :$('#username').val(),
        'password' :$('#password').val()
      }
      // var formData = new FormData($('#loginform'));
      console.log("ssssssssssss");
      var settings = {
        "url": "http://localhost:8000/testapp/token/",
        "method": "POST",
        // "timeout": 0,
        // "processData": false,
        // "mimeType": "multipart/form-data",
        // "contentType": false,
        "data": data
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
    }
  });




