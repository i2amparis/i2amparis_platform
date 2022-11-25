var channel_8 = new MessageChannel();
var port_8_1 = channel_8.port1;
// var iframe_1_1 = document.querySelector('iframe');
var iframe_8_1 = document.querySelector('#electrification_fec_viz_iframe');
iframe_8_1.addEventListener("load", onLoad);

function onLoad() {
    // Listen for button clicks
    var timeframe8_1 = [2005, 2020, 2040, 2050];
    var electricity_fec_viz_iframe_lr_count = 1;
    $(".next-9").click(function () {
        if (electricity_fec_viz_iframe_lr_count < 3) {
            electricity_fec_viz_iframe_lr_count = electricity_fec_viz_iframe_lr_count + 1;
            port_8_1.postMessage([2005, timeframe8_1[electricity_fec_viz_iframe_lr_count]]);
        }
    });
    $(".back-9").click(function () {
        if (electricity_fec_viz_iframe_lr_count > 1) {
            electricity_fec_viz_iframe_lr_count = electricity_fec_viz_iframe_lr_count - 1;
            port_8_1.postMessage([2005, timeframe8_1[electricity_fec_viz_iframe_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_8_1.contentWindow.postMessage('init', '*', [channel_8.port2]);
    setTimeout(function(){   port_8_1.postMessage([2005, 2020]); }, 400);
}
