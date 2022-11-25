$("#col_order").change(function () {
    var viz_frame = $('#viz_iframe');
    viz_frame.hide();
    $('#loading_bar').show();
    var col_ordering_grouping = $('#col_order option:selected').attr('data-category');
    if ((col_ordering_grouping === "") && (col_ordering_grouping === null) && (col_ordering_grouping === undefined)) {
        col_ordering_grouping = "";
    }
    var data = {
        "row_categorisation_dataset": "datasetvariableharmonisationguides",
        "col_categorisation_dataset": col_ordering_grouping,
        "col_order": $('#col_order').val(),
        "row_order": "order",
        "y_var_names": ["variable"],
        "y_axis_title": "Variables",
        "y_var_units": ["-"],
        "x_axis_name": "model",
        "x_axis_title": "Models",
        "x_axis_unit": "-",
        "z_axis_name": "io_status",
        "z_axis_title": "Value",
        "z_axis_unit": "-",
        "min_max_z_value": 0,
        // "color_list_request": ["grey_green","dark_blue", "light_blue","lighter_blue", "moody_blue", "ice_gray"],
        "color_list_request": ["green_new", "green_open_new", "yellow_open_new", "orange_new", "purple_new", "white"],
	    "distinct":[
		    	"Fully Harmonised",
			"Partially harmonised",
			"Checked for consistency",
			"Not harmonized",
			"Extractable model output",
			"Not represented in model"

			],
//        "distinct": ["Extractable model output",
//                     "Harmonisable model input: not harmonised",
//                     "Harmonisable model input: Fully harmonised",
//                     "Harmonisable model input: Partially/weakly harmonised",
//                     "Harmonisable model input: Checked for consistency",
//                     "Not represented in model"
//        ],
        "dataset": "i2amparis_main_harmdatanew",
        "dataset_type": "db",
        "workspace": 'pr_global'
    };
    var url = '';
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            if (Array.isArray(data[key])) {
                for (var j = 0; j < data[key].length; j++) {
                    url = url + String(key) + '[]' + "=" + String(data[key][j]) + '&'
                }
            } else {
                url = url + String(key) + "=" + String(data[key]) + '&'
            }

        }
    }

    var complete_url = "/visualiser/show_heat_map_chart?" + url;
    viz_frame.attr('src', complete_url);
    viz_frame.load(function () {
        $(this).show();

        $('#loading_bar').hide();
        $(this).contents().on('click', function () {

            var col_option = $('iframe').contents().find('#col_clicked').text();
            var col_val = $('#model_name option')
                .filter(function () {
                    return $.trim($(this).text()) === col_option;
                }).val();
            $('#model_name').val(col_val);
            $('#model_name').trigger('change');
            var row_option = $('iframe').contents().find('#row_clicked').text();
            var row_val = $('#var_name option')
                .filter(function () {
                    return $.trim($(this).text()) === row_option;
                }).val();
            $('#var_name').val(row_val);
            $('#var_name').trigger('change');
        })
    });


});
$('#col_order').val('default').trigger('change');


var sel_model_name = $("#model_name");
var sel_geo_cov = $('#geo_cov');
var sel_model_type = $('#model_type');
var sel_model_timestep = $('#model_timestep');
var sel_model_desc = $('#model_desc');
var sel_model_dynamic = $('#model_dynamic');
var sel_var_mod_unit = $('#var_mod_unit');
var sel_var_mod_source = $('#var_mod_source');
var sel_var_mod_source_url = $('#var_mod_source_url');
var sel_var_mod_timespan = $('#var_mod_timespan');
var sel_var_name = $("#var_name");
var sel_var_def = $('#var_def');
var sel_var_cat = $('#var_cat');
var sel_unit_container = $('.unit_container');
var sel_source_container = $('.source_container li');
var sel_source_container_whole = $('.source_container');
var sel_timespan_container = $('.timespan_container');

function show_hide_empty_fields() {
    if (sel_var_mod_unit.text() === '') {
        sel_unit_container.hide();
    } else {
        sel_unit_container.show();
    }
    if (sel_var_mod_timespan.text() === '') {
        sel_timespan_container.hide();
    } else {
        sel_timespan_container.show();
    }
}

function clear_url_sources(){
    $('.source_container ul li').remove();
    $('.source_container').empty();
}

sel_model_name.change(function () {
    clear_url_sources();
    // var html ="";
    sel_geo_cov.text($('#' + String($(this).val()) + ' .d_model_coverage').text());
    sel_model_type.text($('#' + String($(this).val()) + ' .d_model_type').text());
    sel_model_timestep.text($('#' + String($(this).val()) + ' .d_model_timestep').text());
    sel_model_desc.attr('href', '/detailed_model_doc/' + String($(this).val()));
    sel_model_dynamic.attr('href', '/dynamic_doc/' + String($('#model_name').val()));
    sel_model_desc.html("<i class=\"fa fa-book\"></i> Detailed Documentation of " + String($(this).find('option:selected').text()));
    sel_model_dynamic.html("<i class=\"fa fa-search\"></i> Dynamic Documentation of " + String($(this).find('option:selected').text()));
    sel_var_mod_unit.text($('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_unit').text());
    var temp_mod_url = $('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_source_url span');
    var temp_mod_source = $('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_source_info span');
    var temp_mod_title = $('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_source_title span');
    if(temp_mod_source.length !== 0){
        sel_source_container_whole.show();
    }else{
        sel_source_container_whole.hide();
    }

    var titles = temp_mod_title.map(x=> temp_mod_title.eq(x).text());
    var titles_unq = [];
    for (title_idx=0; title_idx < titles.length; title_idx++){
        var temp_title = titles[title_idx];
        if (!titles_unq.includes(temp_title)){
            titles_unq.push(temp_title);
        }
    }
    $('.source_container').append("<div class='heading' style='font-size: 1em!important;'>Sources</div>");
        for (title_idx2=0; title_idx2<titles_unq.length; title_idx2++){
        var temp_source = [];
        for (let i=0; i< temp_mod_source.length; i++ ){
            if (temp_mod_title.eq(i).text() === titles_unq[title_idx2]){
                if (String(temp_mod_url.eq(i).text()) !="") {
                    temp_source.push('<li><a href="' + String(temp_mod_url.eq(i).text()) + '" target="_blank" rel="noopener noreferrer">' + String(temp_mod_source.eq(i).text()) + '</a></li>')
                }
            }

        }
        if (temp_source !=[]) {
            $('.source_container').append("<li> " + titles_unq[title_idx2] + " <ul> " + temp_source.join(" ") + " </ul> </li>");
        }
    }
    sel_var_mod_timespan.text($('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_timespan').text());
    show_hide_empty_fields();
});
sel_var_name.change(function () {
    clear_url_sources();
    sel_var_def.text($('#' + String($(this).val()) + ' .d_var_definition').text());
    sel_var_cat.text($('#' + String($(this).val()) + ' .d_var_category').text());
    sel_var_mod_unit.text($('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_unit').text());
    var temp_mod_url = $('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_source_url span');
    var temp_mod_source = $('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_source_info span');
    var temp_mod_title = $('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_source_title span');
    if (temp_mod_url.length !== 0) {
        sel_source_container_whole.show();
    } else {
        sel_source_container_whole.hide();
    }
    var titles = temp_mod_title.map(x=> temp_mod_title.eq(x).text());
    // var titles = temp_mod_source.map(x=> temp_mod_source.eq(x).text().split('_')[1]);
    var titles_unq = [];
    for (title_idx=0; title_idx < titles.length; title_idx++){
        var temp_title = titles[title_idx];
        if (!titles_unq.includes(temp_title)){
            titles_unq.push(temp_title);
        }
    }
    $('.source_container').append("<div class='heading' style='font-size:1em!important;'>Sources</div>");
    for (title_idx2=0; title_idx2<titles_unq.length; title_idx2++){
        var temp_source = [];
        for (let i=0; i< temp_mod_source.length; i++ ){
            if (temp_mod_title.eq(i).text() === titles_unq[title_idx2]){
                if (String(temp_mod_url.eq(i).text()) !="") {
                    temp_source.push('<li><a href="' + String(temp_mod_url.eq(i).text()) + '" target="_blank" rel="noopener noreferrer">' + String(temp_mod_source.eq(i).text()) + '</a></li>')
                }
            }

        }
        if (temp_source !=[]) {
            $('.source_container').append("<li> " + titles_unq[title_idx2] + " <ul> " + temp_source.join(" ") + " </ul> </li>");
        }
    }
    sel_var_mod_timespan.text($('#' + String(sel_model_name.val()) + '_' + String(sel_var_name.val()) + ' .d_var_mod_timespan').text());
    show_hide_empty_fields();

});
sel_model_desc.attr('href', '/detailed_model_doc/' + String(sel_model_name.val()));
sel_geo_cov.text($('#' + String(sel_model_name.val()) + ' .d_model_coverage').text());
sel_model_type.text($('#' + String(sel_model_name.val()) + ' .d_model_type').text());
sel_model_timestep.text($('#' + String(sel_model_name.val()) + ' .d_model_timestep').text());
sel_model_dynamic.attr('href', '/dynamic_doc/' + String(sel_model_name.val()));
sel_model_desc.html("<i class=\"fa fa-book\"></i> Detailed Documentation of " + String(sel_model_name.find('option:selected').text()));
sel_model_dynamic.html("<i class=\"fa fa-search\"></i> Dynamic Documentation of " + String(sel_model_name.find('option:selected').text()));
sel_var_def.text($('#' + String(sel_var_name.val()) + ' .d_var_definition').text());
sel_var_cat.text($('#' + String(sel_var_name.val()) + ' .d_var_category').text());
sel_source_container_whole.hide();
show_hide_empty_fields();


