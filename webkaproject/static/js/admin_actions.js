alert("Aue basota");

$("#acceptButton").on('click', function (event) {
    alert("Aue accept");
    let $form = $('#edit_form');
    $.ajax({
        url: '/admin1/accept_data',
        type: "POST",
        data: $form.serialize(),
        dataType: "html",

        success: function (response) {
            $("#table_block").html(JSON.parse(response)['result'])
            $('#exampleModal').modal("hide")
        }
    });
});


$('button[name="send_object_data"]').on('click', function (event) {
    alert("Aue redact");
    let $form = $(event.currentTarget).parent();
    var edit_form = $("#edit_form");
    $.ajax({
        url: $('button[name="send_object_data"]').data("data-url"),
        type: "POST",
        data: $form.serialize(),
        dataType: "html",

        success: function (response) {
            $("#modal_window").html(JSON.parse(response)['result'])



            $('#exampleModal').modal("show")
        }
    });
});
