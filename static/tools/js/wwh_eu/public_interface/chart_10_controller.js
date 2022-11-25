var stat = 0;
var channel_10 = new MessageChannel();
var channel_11 = new MessageChannel();
var port_10_1 = channel_10.port1;
var port_11_1 = channel_11.port1;
var iframe_10_1 = document.querySelector('#hydrogen_electricity_comp_ind_viz_iframe');
var iframe_11_1 = document.querySelector('#hydrogen_electricity_comp_trans_viz_iframe');
// iframe_11_1.addEventListener("load", onLoad1);
iframe_10_1.addEventListener("load", doneLoading);
iframe_11_1.addEventListener("load", doneLoading);

function doneLoading() {
    stat = stat + 1
    if (stat === 2) {
        onLoad();
    }
}

function onLoad() {
    // Listen for button clicks
    var timeframe10_1 = [2005, 2025, 2040, 2050];
    var hydrogen_el_comp_viz_iframe_lr_count = 1;
    $(".next-11").click(function () {
        if (hydrogen_el_comp_viz_iframe_lr_count < 3) {
            hydrogen_el_comp_viz_iframe_lr_count = hydrogen_el_comp_viz_iframe_lr_count + 1;
            port_10_1.postMessage([2005, timeframe10_1[hydrogen_el_comp_viz_iframe_lr_count]]);
            port_11_1.postMessage([2005, timeframe10_1[hydrogen_el_comp_viz_iframe_lr_count]]);
        }
    });
    $(".back-11").click(function () {
        if (hydrogen_el_comp_viz_iframe_lr_count > 1) {
            hydrogen_el_comp_viz_iframe_lr_count = hydrogen_el_comp_viz_iframe_lr_count - 1;
            port_10_1.postMessage([2005, timeframe10_1[hydrogen_el_comp_viz_iframe_lr_count]]);
            port_11_1.postMessage([2005, timeframe10_1[hydrogen_el_comp_viz_iframe_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_10_1.contentWindow.postMessage('init', '*', [channel_10.port2]);
    iframe_11_1.contentWindow.postMessage('init', '*', [channel_11.port2]);
    setTimeout(function () {
        port_10_1.postMessage([2005, 2025]);
        port_11_1.postMessage([2005, 2025]);
    }, 400);
}
