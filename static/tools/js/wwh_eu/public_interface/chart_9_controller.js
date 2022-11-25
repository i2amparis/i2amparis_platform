var channel_9 = new MessageChannel();
var port_9_1 = channel_9.port1;
// var iframe_1_1 = document.querySelector('iframe');
var iframe_9_1 = document.querySelector('#hydrogen_production_by_fuel_viz_iframe');
iframe_9_1.addEventListener("load", onLoad);

function onLoad() {
    // Listen for button clicks
    var timeframe9_1 = [2005, 2035, 2040, 2050];
    var hydrogen_production_by_fuel_viz_iframe_lr_count = 1;
    $(".next-10").click(function () {
        if (hydrogen_production_by_fuel_viz_iframe_lr_count < 3) {
            hydrogen_production_by_fuel_viz_iframe_lr_count = hydrogen_production_by_fuel_viz_iframe_lr_count + 1;
            port_9_1.postMessage([2005, timeframe9_1[hydrogen_production_by_fuel_viz_iframe_lr_count]]);
        }
    });
    $(".back-10").click(function () {
        if (hydrogen_production_by_fuel_viz_iframe_lr_count > 1) {
            hydrogen_production_by_fuel_viz_iframe_lr_count = hydrogen_production_by_fuel_viz_iframe_lr_count - 1;
            port_9_1.postMessage([2005, timeframe9_1[hydrogen_production_by_fuel_viz_iframe_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_9_1.contentWindow.postMessage('init', '*', [channel_9.port2]);
    setTimeout(function(){   port_9_1.postMessage([2005, 2035]); }, 400);
}
