var progressBar = $('.progress-bar');

setInterval(addprogress, 100);

function addprogress() {
    progressBar.width(0);
    var width = progressBar.width() + 4.7;
    progressBar.width(width);
}

function fluxoAgua() {
    $.ajax({
        url: "agua",
        beforeSend: function () {
            $('.loading').show();
            addprogress();
        },
        success: function (data) {
            $('#response').html(data);
        },
        error: function () {
            alert('Erro ao carregar a view!');
        },
        complete: function () {
            $('.loading').hide();
            progressBar.width(0);
        }
    });
}
