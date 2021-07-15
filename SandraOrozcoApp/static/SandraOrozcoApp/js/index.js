document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {

    dateClick: function(info) {
        $('#eventoModal').modal('toggle');
        $('#id_fecha').val(info.dateStr);
    },
    
  });
  calendar.render();

  $('#agregar').click(function(){
    agregar("POST");
  });

  function agregar(method){
    var hora = $('#id_hora').val().split(":")
    var minutos=parseInt(hora[1],10)+15;
    var min ="";
    if (minutos >= 60){
      min="00";
    }else{
      min=minutos+"";
    }
    calendar.addEvent({
      title:$('#id_nombre').val(),
      start:$('#id_fecha').val()+ " "+$('#id_hora').val(),
      end:$('#id_fecha').val() +" "+hora[0]+":"+min,
      descripcion: $('#id_email').val(),
      celular: $('id_celular').val(),});
  }
});
