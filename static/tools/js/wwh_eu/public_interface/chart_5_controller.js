var channel_5 = new MessageChannel();
var port_5_1 = channel_5.port1;
// var iframe_1_1 = document.querySelector('iframe');
var iframe_5_1 = document.querySelector('#import_dependency_viz_iframe');
iframe_5_1.addEventListener("load", onLoad);

function onLoad() {
    // Listen for button clicks
    var timeframe5_1 = [0, 25, 40, 50, 60];
    var import_dependency_lr_count = 1;
    $(".next-6").click(function () {
        if (import_dependency_lr_count < 4) {
            import_dependency_lr_count = import_dependency_lr_count + 1;
            port_5_1.postMessage([0, timeframe5_1[import_dependency_lr_count]]);
        }
    });
    $(".back-6").click(function () {
        if (import_dependency_lr_count > 1) {
            import_dependency_lr_count = import_dependency_lr_count - 1;
            port_5_1.postMessage([0, timeframe5_1[import_dependency_lr_count]]);
        }
    });


    // Transfer port2 to the iframe
    iframe_5_1.contentWindow.postMessage('init', '*', [channel_5.port2]);
     setTimeout(function(){  port_5_1.postMessage([0, 25]); }, 1000);
}
