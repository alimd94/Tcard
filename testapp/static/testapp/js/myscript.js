$(document).ready(function () {
  if (getCookie('refresh')) {
    console.log("if (getCookie('refresh'))");
    login()
  }
    $('#loginform').submit(function(e){
        e.preventDefault();
        login();
    })

    function login(){
      if (getCookie('refresh')) {
        console.log("if (getCookie('refresh'))");
        data = {
          'refresh':getCookie('refresh')
        }
  
        var settings = {
          "url": "http://localhost:8000/testapp/token/refresh/",
          "method": "POST",
          "data": data
        };
        
        $.ajax(settings).done(function (response) {
          console.log("ajax refresh done");
          $('#loginformdiv').hide();
          setCookie("access",response.access,10)
          readproduct()
          $('#tableProdcut').show();
        }).fail(function (jqXHR, textStatus) {
          console.log("ajax refresh fail");
          console.log(jqXHR);
          console.log(textStatus);
          eraseCookie('refresh')
          eraseCookie('access')
          $('#loginformdiv').show();
          $('#tableProdcut').hide();
        });
      } else {
        data = {
          'username' :$('#username').val(),
          'password' :$('#password').val()
        }
  
        var settings = {
          "url": "http://localhost:8000/testapp/token/",
          "method": "POST",
          "data": data
        };
        
        $.ajax(settings).done(function (response) {
          console.log("ajax login done");
          $('#loginformdiv').hide();
          setCookie("access",response.access,10)
          setCookie("refresh",response.refresh,10)
          readproduct()
          $('#tableProdcut').show();
        });
      }
   
    }

    function readproduct(){
        var settings = {
          "url": "http://localhost:8000/testapp/read/",
          "method": "GET",
          "headers": {
            "Authorization": "Bearer "+ getCookie('access')
          },
        };

        $.ajax(settings).done(function (response) {
          filltable(response);
        });
    }

    function filltable(response){
      $('#tableProdcut tr').not(':first').not(':last').remove();
      var html = '';
      for(var i = 0; i < response.length; i++)
                  html += '<tr><td>' + response[i].name + 
                          '</td><td>' + response[i].brand + 
                          '</td><td>' + response[i].price + 
                          '</td><td>' + response[i].description + 
                          '</td></tr>';
      $('#tableProdcut tr').first().after(html);
    }

    function setCookie(name,value,days) {
      var expires = "";
      if (days) {
          var date = new Date();
          date.setTime(date.getTime() + (days*24*60*60*1000));
          expires = "; expires=" + date.toUTCString();
      }
      document.cookie = name + "=" + (value || "")  + expires + "; path=/";
  }
  function getCookie(name) {
      var nameEQ = name + "=";
      var ca = document.cookie.split(';');
      for(var i=0;i < ca.length;i++) {
          var c = ca[i];
          while (c.charAt(0)==' ') c = c.substring(1,c.length);
          if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
      }
      return null;
  }

function eraseCookie(name) {   
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
});




