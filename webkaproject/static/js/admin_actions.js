$('button[name="send_object_data"]').on('click', function (event) {
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