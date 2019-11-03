// comment when deploying, to delay the loading inorder to check 
// that the preloader works properly
// 
$(document).ready(function() {
 
    setTimeout(function(){
        $('body').addClass('loaded');
        $('h1').css('color','#222222');
    }, 3000);
 
});