var channel_6 = new MessageChannel();
var port_6_1 = channel_6.port1;
// var iframe_1_1 = document.querySelector('iframe');
var iframe_6_1 = document.querySelector('#imported_fuels_viz_iframe');
iframe_6_1.addEventListener("load", onLoad);

function onLoad() {
    // Listen for button clicks
    var timeframe6_1 = [2005, 2020, 2030, 2050];
    var imported_fuels_viz_iframe_lr_count = 1;
    $(".next-7").click(function () {
        if (imported_fuels_viz_iframe_lr_count < 3) {
            imported_fuels_viz_iframe_lr_count = imported_fuels_viz_iframe_lr_count + 1;
            port_6_1.postMessage([2005, timeframe6_1[imported_fuels_viz_iframe_lr_count]]);
        }
    });
    $(".back-7").click(function () {
        if (imported_fuels_viz_iframe_lr_count > 1) {
            imported_fuels_viz_iframe_lr_count = imported_fuels_viz_iframe_lr_count - 1;
            port_6_1.postMessage([2005, timeframe6_1[imported_fuels_viz_iframe_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_6_1.contentWindow.postMessage('init', '*', [channel_6.port2]);
    setTimeout(function(){  port_6_1.postMessage([2005, 2020]); }, 400);
}
