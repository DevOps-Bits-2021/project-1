$('.nextBtn').on('click',function(){
  var parentRef =  $(this).parent();
  var inputVal = parentRef.find('input').val();
  if(checkLength(inputVal,1)){
    add_remove_effects(parentRef,'shake');
    $('.container').addClass('error');
    return ;
  } else {
    if(checkLength(inputVal,4)){
      return ;
    }
  }
  if(!parentRef.hasClass('lastField')){
   parentRef.addClass('hide'); 
   parentRef.next().addClass('shown').addClass('visible');
   $('.bullets span.active').removeClass('active').next().addClass('active');
  } else {
    $('.container').css('background','#fff').html($('.spinnerWrapper').html());
    setTimeout(function(){
      $('.container').html('<div class="success"><i class="fa fa-check"></i><h2>Account Created</h2></div>');
    },4000);
  }
  $('.container').removeClass('error');
});

function checkLength(data,length){
  data = $.trim(data);
  if(data.length < length){
    return true;
  }
  return false;
}
var add_remove_effects = function(ref,classname){
  var $a = ref.addClass(classname);
  var $b = classname;
    setTimeout(function(){
      $a.removeClass($b);
    },450);     
}