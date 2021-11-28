
// this is to initialize navbar from materialize

$(document).ready(function(){
    $('.sidenav').sidenav();
  });

  // this is to initialize modal from materialize

  
  $(document).ready(function(){
    $('.modal').modal();
  });

  // // datepicker initialization
  // $(document).ready(function(){
  //   $('.datepicker').datepicker();
  // });

  // select initialization
  $(document).ready(function(){
    $('select').formSelect();
  });

  document.addEventListener("DOMContentLoaded", function() {

      // datepicker initialization
      let datepicker = document.querySelectorAll(".datepicker");
      M.Datepicker.init(datepicker, {
          format: "dd mmmm, yyyy",
          i18n: {done: "Select"}
      });
    });