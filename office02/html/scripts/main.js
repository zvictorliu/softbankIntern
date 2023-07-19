$(function(){
  $(".button").on("touchstart mousedown",function(event){
    event.preventDefault();
    var str = $(this).attr("id");
    $.raiseALMemoryEvent('DanceOption', str)
  })
});

