var username = document.querySelector('#username');
function Submit(){
  
  if(username.value.length > 1){
      Swal.fire({
      position: 'center',
      icon: 'success',
      title: 'You logged in as '+ username.value,
      showConfirmButton: false,
      timer: 1500
    })

    window.setTimeout(function() {
          window.location = 'Chat.html';
      }, 2000);
    
    
    }else{
      Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'The password or the username is incorrect!'
    })
  
    }
    
  }