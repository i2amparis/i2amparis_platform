var channel_7 = new MessageChannel();
var port_7_1 = channel_7.port1;
// var iframe_1_1 = document.querySelector('iframe');
var iframe_7_1 = document.querySelector('#electrification_ir_co2_reduction_viz_iframe');
iframe_7_1.addEventListener("load", onLoad);

function onLoad() {
    // Listen for button clicks
    var timeframe7_1 = [0, 25, 40, 50, 80];
    var electricity_ratio_viz_iframe_lr_count = 1;
    $(".next-8").click(function () {
        if (electricity_ratio_viz_iframe_lr_count < 4) {
            electricity_ratio_viz_iframe_lr_count = electricity_ratio_viz_iframe_lr_count + 1;
            port_7_1.postMessage([0, timeframe7_1[electricity_ratio_viz_iframe_lr_count]]);
        }
    });
    $(".back-8").click(function () {
        if (electricity_ratio_viz_iframe_lr_count > 1) {
            electricity_ratio_viz_iframe_lr_count = electricity_ratio_viz_iframe_lr_count - 1;
            port_7_1.postMessage([0, timeframe7_1[electricity_ratio_viz_iframe_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_7_1.contentWindow.postMessage('init', '*', [channel_7.port2]);
    setTimeout(function(){    port_7_1.postMessage([0, 25]); }, 2000);
}
