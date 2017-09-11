$('.nav  li').click(function(e) {
  //console.log(e.currentTarget,"//",e.target,"//",this);
  e.stopPropagation();
  $('.nav li').removeClass('active');
  $(this).addClass('active');
});