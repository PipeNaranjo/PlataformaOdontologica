document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    
    dateClick: function(info) {
        $('#eventoModal').modal('toggle');
        $('#id_fecha').val(info.dateStr);
    },
    eventClick: function(info){

    }
  });
  calendar.render();

  $('#agregar').click(function(){
    agregar("POST");
  });

  function agregar(method){
    hora = $('#id_hora').val().split(":")
    minutos=parseInt(hora[1],10)+15;
    if (minutos >= 60){
      min="00";
    }else{
      min=minutos+"";
    }
    evento={
      title:$('#id_nombre').val(),
      start:$('#id_fecha').val()+ " "+$('#id_hora').val(),
      end:$('#id_fecha').val() +" "+hora[0]+":"+min,
      descripcion: $('#id_email').val(),
      celular: $('id_celular').val(),
    }
    

    
  };
});

function abrir() {

  $('#loginModal').modal('toggle');
    
}
function cerrar(){
	document.getElementById("miModal").style.display="none";
}