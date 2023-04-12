function table() {
    $.ajax({
        url: '/table/',
        success: function (data) {
            $('#attendance-table').html(data);
        }
    });
}

setInterval(function () {
    table();
}, 5000);