var waterflow = document.getElementById("waterflow");
var control = false;
waterflow.addEventListener("click", function() {
    var progressBar = $('.progress-bar');
    var intervalo = setInterval(function() {
        $.ajax({
            url: "status_water_flow",
            success: function(data) {
                var progresso = parseInt(data);
                progressBar.attr('aria-valuenow', progresso);
                progressBar.css('width', progresso + '%');
                if (progresso == 100 && control == false) {
                    clearInterval(intervalo); 
                    $('.loading').hide();
                    $('#response').html("Deu bom, baby dogs já tem água para beber!");
                    control = true;
                } else if (control == true) {
                    clearInterval(intervalo); 
                    $('#response').html("Você já deu água para os baby dogs, caso queria realmente dar mais, atualize a página!");
                }
            },
            error: function() {
                clearInterval(intervalo); 
                $('.loading').hide();
                $('#response').html("Erro ao executar ação!");
            }
        });
    }, 1000);
});


var abortwaterflow = document.getElementById("abortwaterflow");
abortwaterflow.addEventListener("click", function() {
    $.ajax({
        url: "abort_water_flow",
        success: function(data) {
            var progresso = parseInt(data);
            console.log(progresso);
            if (progresso == 1) {
                $('.loading').hide();
                $('#response').html("Parado com sucesso!");
                control = true;
            } else if (control == true) {
                $('#response').html("Erro ao executar ação!");
            }
        },
        error: function() { 
            $('.loading').hide();
            $('#response').html("Erro ao executar ação!");
        }
    });
});