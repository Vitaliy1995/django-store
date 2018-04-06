"use strict";

window.onload = function () {
    $('.phone-in-cataloge').on('click', 'input[type="number"]', function(event) {
        let t_href = event.target;
        const URL = "/basket/edit/" + t_href.name + "/" + t_href.value + "/";

        $.ajax({
            url: URL,

            success: function (data) {
                $('.phone-in-cataloge').html(data.result);
            },
        });
        event.preventDefault();
    });
}
