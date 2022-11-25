var method_figure_count = 1;
$(".next-1").click(function () {
    if (method_figure_count < 4) {
        method_figure_count = method_figure_count + 1
    }
});
$(".back-1").click(function () {
    if (method_figure_count > 1) {
        method_figure_count = method_figure_count - 1
        $(".methods-image").removeClass("opaque");
    }
});
$(".next-back").click(function () {
    console.log(method_figure_count);
    var image = $(".methods-image-" + method_figure_count);
    image.addClass("opaque");
});