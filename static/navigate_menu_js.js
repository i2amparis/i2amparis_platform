$(document).ready(function () {
    var stopClickSide = false;
    var stopClickHeading = false;
    $(".sidebar h4 a").on('click', function () {
        $(this).find('i.rotate').toggleClass("down");

    });

    $(".accordion button").on('click', function () {
        $(this).find('i.rotate').toggleClass("down");

    });

    $('#accordion_introduction').find('button').click();
    $('li span').on('click', function () {
        var x = $(this).siblings()[0].href.split('#')[1];
        var y = $(this).siblings()[0];
        close_all_collapses(x, y, move_to_collapse);
    });

    $('body').css('height', '100%');

    function close_all_collapses(x_to_open, y_to_move_to, callback) {
        $('#main_bar .collapse.in').not('#collapse_' + x_to_open).collapse('hide');
        setTimeout(function () {
            callback(y_to_move_to, x_to_open, open_chosen_collapse);
        }, 400);
    }

    function move_to_collapse(y_to_move_to, x_to_open, callback) {
        y_to_move_to.click();
        callback(x_to_open);
        y_to_move_to = null;
    }

    function open_chosen_collapse(x_to_open) {
        $('#accordion_' + x_to_open).find('button').click();

    }


});