///// Section-1 CSS-Slider /////    
  // Auto Switching Images for CSS-Slider
  function bannerSwitcher() {
    next = $('.sec-1-input').filter(':checked').next('.sec-1-input');
    if (next.length) next.prop('checked', true);
    else $('.sec-1-input').first().prop('checked', true);
  }

  var bannerTimer = setInterval(bannerSwitcher, 5000);

  $('nav .controls label').click(function() {
    clearInterval(bannerTimer);
    bannerTimer = setInterval(bannerSwitcher, 100000)
  });


///// Anchor Smooth Scroll /////
//   $('.main-menu a, .learn-more-button a').click(function(e){
    
//     e.preventDefault();
        
//     var target = $(this).attr('href');
        
//     $('html, body').animate({scrollTop: $(target).offset().top}, 1000);
//     return false;
//   });
//   
/*global $, console*/
function () {
  'use strict';
  
  // Start navbar 
  (function () {
    
    
    // Add class active when the user clicks the lis of the menu
    $('.nav .list li').on('click', 'a', function () {
      $(this).parent().addClass('active').siblings().removeClass('active');
    });
    
    
    var openCategories = $('.nav #open-categories'),
        categories = $('.drop-down');
    
    
    // Toggle categories on clicking
    openCategories.on('click', function () {
      $("#" + $(this).data('dropdown')).toggleClass('show');
      // When the user clicks the window if the categories is not the target, close it.
      $(window).on('mouseup', function (e) {
        if ( categories.hasClass('show')
            && ! categories.is(e.target)
            && categories.has(e.target).length === 0
            && ! openCategories.is(e.target) ) {
          categories.removeClass('show');
        }
      });
    });
    
    
    // Toggle menu, This will be shown in Extra small screens only
    $('.nav .toggle-nav').on('click', function () {
      $( "#" + $(this).data('toggle') ).slideToggle(300);
    });
    
    
  }());
};