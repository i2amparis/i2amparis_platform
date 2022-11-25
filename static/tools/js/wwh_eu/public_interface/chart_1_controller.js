var channel_1 = new MessageChannel();
var port_1_1 = channel_1.port1;
// var iframe_1_1 = document.querySelector('iframe');
var iframe_1_1 = document.querySelector('#total_co2_emissions_viz_iframe');
iframe_1_1.addEventListener("load", onLoad);

function onLoad() {
    // Listen for button clicks
    var timeframe1_1 = [2005, 2020, 2030, 2050];
    var total_co2emissions_lr_count = 1;
    $(".next-2").click(function () {
        if (total_co2emissions_lr_count < 3) {
            total_co2emissions_lr_count = total_co2emissions_lr_count + 1;
            port_1_1.postMessage([2005, timeframe1_1[total_co2emissions_lr_count]]);
        }
    });
    $(".back-2").click(function () {
        if (total_co2emissions_lr_count > 1) {
            total_co2emissions_lr_count = total_co2emissions_lr_count - 1;
            port_1_1.postMessage([2005, timeframe1_1[total_co2emissions_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_1_1.contentWindow.postMessage('init', '*', [channel_1.port2]);
    setTimeout(function(){ port_1_1.postMessage([2005, 2020]); }, 400);
}
