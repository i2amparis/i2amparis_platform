$(document).ready(function () {
    $('.closebtn').click(function (){
        closeNav();
    })
    $('.content-section').hide();
    $('.methods').show();
    var heading = $('.heading-link[data-section="methods"]');
    heading.css('background', '#849627');
    heading.css('color', 'white');
    document.getElementById("footer").style.width = "75%";
        document.getElementById("footer").style.float = "right";

    function openNav() {
        document.getElementById("mySidenav").style.width = "25%";
        document.getElementById("main").style.marginLeft = "25%";
        document.getElementById("footer").style.width = "75%";
        document.getElementById("footer").style.float = "right";
    }

    function closeNav() {
        document.getElementById("mySidenav").style.width = "0%";
        document.getElementById("main").style.marginLeft = "0%";
        document.getElementById("footer").style.width = "100%";
        document.getElementById("footer").style.float = "left";
    }


    $('.sidenav a').click(function () {
            $('.sidenav a').css('background', '#11111100');
            $('.sidenav a').css('color', '#818181');
            if ($(this).hasClass('heading-link')) {
                $('.content-section').hide();
                if ($(this).attr('data-section') === 'policies') {
                    var subheading = $('.sub-heading-link a').first();
                    subheading.css('background', '#849627');
                    subheading.css('color', 'white');
                    $('.content-section.policies').show();
                    $('.content-section.policies .subcontent').hide();
                    $('.content-section .subcontent').first().show();
                }
                $('.content-section.' + $(this).attr('data-section')).show();
            } else if ($(this).parent().hasClass('sub-heading-link')) {
                var policies_heading = $('a[data-section="policies"]')
                policies_heading.css('background', '#849627');
                policies_heading.css('color', 'white');
                $('.content-section').hide();
                $('.content-section.policies div.subcontent').hide();
                $('.subcontent.' + $(this).attr('data-section')).show();
                $('.content-section.policies').show();
            }

            $(this).not(document.getElementsByClassName("closebtn")).css('background', '#849627');
            $(this).not(document.getElementsByClassName("closebtn")).css('color', 'white');
        }
    );

    $('.content_btn').on('click', function () {
        if (document.getElementById("mySidenav").style.width !== '0%') {
            closeNav();
        } else {
            openNav();
        }
    });
    openNav();

});