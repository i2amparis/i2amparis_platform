var channel_2 = new MessageChannel();
var port_2_1 = channel_2.port1;
var iframe_2_1 = document.querySelector('#energy_co2_emissions_by_sector_viz_iframe');
iframe_2_1.addEventListener("load", onLoad);

function onLoad() {
    // Listen for button clicks
    var timeframe2_1 = [2005, 2020, 2030, 2050];
    var co2emissions_by_sec_lr_count = 1;
    $(".next-3").click(function () {
        if (co2emissions_by_sec_lr_count < 3) {
            co2emissions_by_sec_lr_count = co2emissions_by_sec_lr_count + 1;
            port_2_1.postMessage([2005, timeframe2_1[co2emissions_by_sec_lr_count]]);
        }
    });
    $(".back-3").click(function () {
        if (co2emissions_by_sec_lr_count > 1) {
            co2emissions_by_sec_lr_count = co2emissions_by_sec_lr_count - 1;
            port_2_1.postMessage([2005, timeframe2_1[co2emissions_by_sec_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_2_1.contentWindow.postMessage('init', '*', [channel_2.port2]);
    setTimeout(function(){  port_2_1.postMessage([2005, 2020]); }, 400);
}
