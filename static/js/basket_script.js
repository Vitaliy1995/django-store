"use strict";

window.onload = function () {
    $('.phone-in-cataloge input[type="number"]').on('click', function() {
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
