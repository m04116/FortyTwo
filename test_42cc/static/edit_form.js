$(document).ready(function(){

    // var form = $('edit_form');
    // var url = form.attr('action');
    // var csrf_token = $('#edit_form [name="csrfmiddlewaretoken"]').val();
    // var data = {
    //     'name': $('#name').val(),
    //     'last_name': $('#last_name').val(),
    //     'birth_date': $('#birth_date').val(),
    //     'photo': $('#photo').val(),
    //     'email': $('#email').val(),
    //     'jabber': $('#jabber').val(),
    //     'skype': $('#skype').val(),
    //     'other_contacts': $('#other_contacts').val(),
    //     'bio': $('#bio').val(),

    //     'csrfmiddlewaretoken': csrf_token


    $('#btn_submit').click(function (){

        var form = $('edit_form');
        var url = form.attr('action');
        var csrf_token = $('#edit_form [name="csrfmiddlewaretoken"]').val();
        var data = {
            'name': $('#name').val(),
            'last_name': $('#last_name').val(),
            'birth_date': $('#birth_date').val(),
            'photo': $('#photo').val(),
            'email': $('#email').val(),
            'jabber': $('#jabber').val(),
            'skype': $('#skype').val(),
            'other_contacts': $('#other_contacts').val(),
            'bio': $('#bio').val(),

            'csrfmiddlewaretoken': csrf_token};


        $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: false,
        success: function (data) {
            console.log("OK!!");
            },

        error: function () {
            console.log("error!!!")
            }
        });


    });
    
    
});