var intervalo = null;
var waterFlow = document.getElementById("waterflow");
waterFlow.addEventListener("click", function() {
    // Validating if the function has already been performed
    if (typeof callControlWaterFlow === "undefined") {
        // Setting true to perform the function more than once
        callControlWaterFlow = true;
        var progressBar = $('.progress-bar'); 
        intervalo = setInterval(function() {
            $.ajax({
                url: "status_water_flow",
                success: function(data) {
                    var progresso = parseInt(data);
                    progressBar.attr('aria-valuenow', progresso);
                    progressBar.css('width', progresso + '%');
                    if (progresso > 99 ) {
                        clearInterval(intervalo); 
                        $('.loading').hide();
                        $('#response').html("Deu bom, baby dogs já tem água para beber!<br/>Caso queira dar mais água, atualize a página.");
                    } 
                },
                error: function() {
                    clearInterval(intervalo); 
                    $('.loading').hide();
                    $('#response').html("Erro ao executar ação!");
                }
            });
        }, 1000);
    } else if (typeof callControlAbortWaterFlow !== "undefined") {
        $('#response').html("Para executar novamente, atualize a página.");
    }
});


var abortWaterFlow = document.getElementById("abortwaterflow");
abortWaterFlow.addEventListener("click", function() {
    // Validating if the function has already been performed
    if (typeof callControlAbortWaterFlow === "undefined") {
        // Setting true to perform the function more than once
        callControlAbortWaterFlow = true;
        // Clearing the interval to stop refreshing the progress bar
        clearInterval(intervalo); 

        $.ajax({
            url: "abort_water_flow",
            success: function(data) {
                var progresso = parseInt(data);
                if (progresso == 1) {
                    $('.loading').hide();
                    $('#response').html("Parado com sucesso, caso queira dar mais água, atualize a página.");
                } else {
                    $('.loading').hide();
                    $('#response').html("Não foi possível para!");
                }
            },
            error: function() { 
                $('.loading').hide();
                $('#response').html("Erro ao executar ação!");
            }
        });
    };
});

