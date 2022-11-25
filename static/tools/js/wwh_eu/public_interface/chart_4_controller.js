var channel_4 = new MessageChannel();
var port_4_1 = channel_4.port1;
// var iframe_1_1 = document.querySelector('iframe');
var iframe_4_1 = document.querySelector('#co2_ccs_ag_co2_reduction_viz_iframe');
iframe_4_1.addEventListener("load", onLoad);

function onLoad() {
    // Listen for button clicks
    var timeframe4_1 = [0, 40, 50, 60, 80];
    var co2_ccs_ag_co2_reduction_lr_count = 1;
    $(".next-5").click(function () {
        if (co2_ccs_ag_co2_reduction_lr_count < 4) {
            co2_ccs_ag_co2_reduction_lr_count = co2_ccs_ag_co2_reduction_lr_count + 1;
            port_4_1.postMessage([0, timeframe4_1[co2_ccs_ag_co2_reduction_lr_count]]);
        }
    });
    $(".back-5").click(function () {
        if (co2_ccs_ag_co2_reduction_lr_count > 1) {
            co2_ccs_ag_co2_reduction_lr_count = co2_ccs_ag_co2_reduction_lr_count - 1;
            port_4_1.postMessage([0, timeframe4_1[co2_ccs_ag_co2_reduction_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_4_1.contentWindow.postMessage('init', '*', [channel_4.port2]);
    setTimeout(function(){ port_4_1.postMessage([0, 40]); }, 1000);

}
