
function showpassword(mode){
    const pass =mode==2?document.getElementById('password2'):document.getElementById('password1');
    const eye =mode==2?document.getElementById('eye2'):document.getElementById('eye1');
    if(pass.getAttribute('type')=="password"){
        pass.setAttribute('type','text');
        eye.classList.add('fa-eye-slash');
    }
    else{
        pass.setAttribute('type','password');
        eye.classList.remove('fa-eye-slash');
    }
        
}
