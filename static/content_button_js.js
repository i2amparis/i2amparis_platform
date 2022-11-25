document.getElementById("mySidebar").style.width = '0px';
$('.content_btn').on('click', function () {
    if (document.getElementById("mySidebar").style.width != '0px') {
        console.log(document.getElementById("mySidebar").style.width);
        closeNav();
    }
    else {
        console.log(document.getElementById("mySidebar").style.width);
        openNav();
    }

});

function openNav() {

    document.getElementById("mySidebar").style.width = "18rem";

}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";

}