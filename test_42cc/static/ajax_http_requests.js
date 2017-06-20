$(document).ready(function(){

setInterval(function () {
    $.ajax({
                url: 'check_requests',
                type: 'GET',
                
                cache: false,
                success: function (data) {
                    console.log("OK!!");
                    
                    $('#new_requests').html('');
                    console.log(data.new_requests_nmb);
                    $('#new_requests').text(data.new_requests_nmb + "new request(s)")
                  }
            });
}, 3000);

});