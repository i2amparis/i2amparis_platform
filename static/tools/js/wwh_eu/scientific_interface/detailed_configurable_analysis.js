$(document).ready(function () {


    $('#dca-var-next-btn').on('click', function () {
        if ($('#variable_name').multipleSelect('getSelects').length > 0) {
            $('#dca-var-next-btn').parent().hide();
            $('#variable_name').parent().find('.boot-select').addClass('disabled-select');
            $('#variable_name').parent().find('label').addClass('disabled-select');
            $('.clear-sel-button[data-sel_clear="variable_name"]').addClass('disabled-select');
            $('#dca-region-next-btn').parent().show();
            $('#region_name').parent().find('.boot-select').removeClass('disabled-select');
            $('#region_name').parent().find('label').removeClass('disabled-select');
            $('.clear-sel-button[data-sel_clear="region_name"]').removeClass('disabled-select');
            $('#detailed_configurable_progress_text').text('Please select Region(s) . . .');
            $('#dca_progress_bar div').css('width', '25%');
            $('#dca_progress_bar div').attr('aria-valuenow', '25');
            $('#detailed_filtering').addClass("disabled_radio");
            $('#sdg_filtering').addClass("disabled_radio");
            var sdg_select = $('#sdg_select');
            sdg_select.attr('disabled', 'disabled');
            sdg_select.multipleSelect('refreshOptions', {});
        //    Disable unavailable visualisations
            var selected_var = $('#variable_name').multipleSelect('getSelects')[0];
            var var_type = $('.hidden-var-container option[value="'+ selected_var +'"]').attr('data-type');
            if (var_type!='sum') {
                $('#visualisation_type_selection #piechart').parent().addClass("disabled-select");
                $("#visualisation_type_selection #linechart ").prop("checked", true).trigger("click");
            }

        } else {
            alert('Please select a variable before moving on.')
        }
    });

    $('#dca-region-next-btn').on('click', function () {
        if ($('#region_name').multipleSelect('getSelects').length > 0) {
            $('#dca-region-next-btn').parent().hide();
            $('#dca-scenario-next-btn').parent().show();
            $('#scenario_name').parent().find('.boot-select').removeClass('disabled-select');
            $('#scenario_name').parent().find('label').removeClass('disabled-select');
            $('.clear-sel-button[data-sel_clear="scenario_name"]').removeClass('disabled-select');
            $('#region_name').parent().find('.boot-select').addClass('disabled-select');
            $('#region_name').parent().find('label').addClass('disabled-select');
            $('.clear-sel-button[data-sel_clear="region_name"]').addClass('disabled-select');
            $('#detailed_configurable_progress_text').text('Please select Scenario(s) . . .');
            $('#dca_progress_bar div').css('width', '50%');
            $('#dca_progress_bar div').attr('aria-valuenow', '50');

        } else {
            alert('Please select at least one region before moving on.')
        }
    });

    $('#dca-scenario-next-btn').on('click', function () {
        if ($('#scenario_name').multipleSelect('getSelects').length > 0) {
            $('#dca-scenario-next-btn').parent().hide();
            $('#run-button').parent().removeClass('disabled-select');
            $('#model_name').parent().find('.boot-select').removeClass('disabled-select');
            $('#model_name').parent().find('label').removeClass('disabled-select');
            $('.clear-sel-button[data-sel_clear="model_name"]').removeClass('disabled-select');
            $('#scenario_name').parent().find('.boot-select').addClass('disabled-select');
            $('#scenario_name').parent().find('label').addClass('disabled-select');
            $('.clear-sel-button[data-sel_clear="scenario_name"]').addClass('disabled-select');
            $('#detailed_configurable_progress_text').text('Please select Model(s) . . .');
            $('#dca_progress_bar div').css('width', '75%');
            $('#dca_progress_bar div').attr('aria-valuenow', '75');

        } else {
            alert('Please select at least one scenario before moving on.')
        }
    });


    function initialise_sm_selects() {
        $('select.boot-select').each(function () {
            var select = $(this);
            select.multipleSelect('destroy').multipleSelect(
                {
                    filter: true,
                    showClear: false,
                    animate: 'fade',
                    maxHeightUnit: 'row',
                    maxHeight: 8,
                    dropWidth: 250,
                    selectAll: false,
                    placeholder: 'Please select a value',
                    onClick: function () {
                        update_unavailable_select_options(select.attr('id'));
                        populate_selects('#' + select.attr('id'));
                    },

                });
        });
    }

    function reset_all_variables() {
        $('select.sdg-select').multipleSelect('setSelects', []);
        var sdg_select = $('#sdg_select');
        sdg_select.attr('disabled', 'disabled');
        sdg_select.multipleSelect('refreshOptions', {});
        sdg_select.multipleSelect('setSelects', []);
        var variable_select = $('#variable_name');
        variable_select.multipleSelect('setSelects', []);
        variable_select.find('option').remove();
        $(".hidden-var-container").children().clone().appendTo("#variable_name");
        variable_select.multipleSelect('refreshOptions', {});
        variable_select.multipleSelect('setSelects', []);
    }


    function initialise_sdg_variables() {
        $('select.sdg-select').multipleSelect('setSelects', []);
        var sdg_select = $('#sdg_select');
        sdg_select.attr('disabled', 'disabled');
        sdg_select.multipleSelect('refreshOptions', {});
        $(document).on('change', 'input:radio[id="sdg_variables"]', function (event) {
            sdg_select.removeAttr('disabled');
            sdg_select.multipleSelect('refreshOptions', {});
        });
        $(document).on('change', 'input:radio[id="all_variables"]', function (event) {
            reset_all_variables();
        });
    }


    initialise_sm_selects();
    $('select.sdg-select').each(function () {
        var select = $(this);
        select.multipleSelect(
            {
                filter: true,
                showClear: false,
                animate: 'fade',
                maxHeightUnit: 'row',
                maxHeight: 8,
                dropWidth: 250,
                selectAll: false,
                placeholder: 'Please select an SDG',
                onClick: function () {
                    populate_variables();
                },

            });
    });
    initialise_sdg_variables();
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        var target = $(e.target).attr("href"); // activated tab
        console.log(target);
        if (target==='#scientific_tool'){
            clear_detailed_configurable_analysis();
        };
    });


    function populate_variables() {
        var sdg_select = $('#sdg_select');
        var variable_select = $('#variable_name');
        variable_select.multipleSelect('setSelects', []);
        variable_select.find('option').remove();
        var selected_sdg = sdg_select.multipleSelect('getSelects');
        const input = {
            'sdg_name': selected_sdg[0]
        };
        $.ajax({
            url: "/get_sdg_variables",
            type: "POST",
            data: JSON.stringify(input),
            contentType: 'application/json',
            success: function (data) {
                console.log(data);
                var options = '';
                for (var i = 0; i < data.length; i++) {
                    options = options + '<option value="' + data[i]['variable_name'] + '">' + data[i]['variable_title'] + '</option>'
                }
                variable_select.append(options);
                variable_select.multipleSelect('refreshOptions', {});
                variable_select.multipleSelect('setSelects', []);

            },
            error: function (data) {
                console.log('Cannot update variable select AJAX Call failed.');
            }
        });

    }


    function transform_multiple_select(selector) {
        selector.multipleSelect('destroy').multipleSelect(
            {
                filter: true,
                selectAll: false,
                showClear: false,
                animate: 'fade',
                maxHeightUnit: 'row',
                maxHeight: 8,
                dropWidth: 250,
                placeholder: 'Please select a value'
            }
        );
    }

    function transform_multiple_add_listeners(selector) {
        selector.multipleSelect('refreshOptions', {
            onClick: function () {
                update_unavailable_select_options(selector.attr('id'));
            },

        });
    }

    function populate_selects(selector) {
        var sel = $(selector);
        var others_sel = $('select.boot-select:not(' + selector + ')');
        var selected = sel.multipleSelect('getSelects');

        if (selected.length >= 2) {
            others_sel.each(function () {
                var oth_sel = $(this);
                $(this).removeAttr('multiple');
                if ($(this).multipleSelect('getSelects').length === 0) {
                    transform_multiple_select(oth_sel);
                    $(this).multipleSelect('setSelects', []);
                    transform_multiple_add_listeners($(this));
                } else {
                    transform_multiple_select(oth_sel);
                    transform_multiple_add_listeners($(this));
                }
            })

        } else {
            update_others_function(selector);
        }

    }


    function update_others_function(selector) {
        var others_sel = $('select.mul-select:not(' + selector + ')');
        others_sel.attr('multiple', 'multiple');
        others_sel.multipleSelect('destroy');
        (others_sel).each(function () {
            var other_select = $(this);
            $(this).multipleSelect(
                {
                    filter: true,
                    showClear: false,
                    animate: 'fade',
                    maxHeightUnit: 'row',
                    maxHeight: 8,
                    selectAll: false,
                    dropWidth: 250,
                    placeholder: 'Please select a value',
                    onClick: function () {
                        update_unavailable_select_options(other_select.attr('id'));
                        populate_selects('#' + other_select.attr('id'));
                    },

                });
        });

    }

    var fe_all_scenarios = [];
    var fe_all_regions = [];
    var fe_all_models = [];

    function update_unavailable_select_options(changed) {

        const models = $('#model_name').multipleSelect('getSelects');
        const scenarios = $('#scenario_name').multipleSelect('getSelects');
        const regions = $('#region_name').multipleSelect('getSelects');
        const variables = $('#variable_name').multipleSelect('getSelects');

        var filtering = $('input[name="detailed_filtering_input"]:checked').val();

        const input = {
            'model__name': models,
            'scenario__name': scenarios,
            'region__name': regions,
            'variable__name': variables,
            'changed_field': changed,
            'fe_all_scenarios': fe_all_scenarios,
            'fe_all_regions': fe_all_regions,
            'fe_all_models': fe_all_models,
            'interface': 'pr_eu'
        };

        $.ajax({
            url: "/update_scientific_model_selects_" + filtering,
            type: "POST",
            data: JSON.stringify(input),
            contentType: 'application/json',
            success: function (data) {
                fe_all_models = data['models'];
                fe_all_scenarios = data['scenarios'];
                fe_all_regions = data['regions'];
                $("#scientific_tool .boot-select option").removeAttr('disabled');
                var j;
                for (j = 0; j < data['models'].length; j++) {
                    $("#model_name option[value='" + data['models'][j] + "']").attr('disabled', 'disabled');
                }

                for (j = 0; j < data['scenarios'].length; j++) {
                    $("#scenario_name option[value='" + data['scenarios'][j] + "']").attr('disabled', 'disabled');
                }

                for (j = 0; j < data['regions'].length; j++) {
                    $("#region_name option[value='" + data['regions'][j] + "']").attr('disabled', 'disabled');
                }

                for (j = 0; j < data['variables'].length; j++) {
                    $("#variable_name option[value='" + data['variables'][j] + "']").attr('disabled', 'disabled');
                }

                $('select.boot-select').each(function () {
                    var select = $(this);
                    select.multipleSelect('refreshOptions', {})
                });

            },
            error: function (data) {
                console.log('Cannot update disabled selects. AJAX Call failed.');
            }
        });


    }

    $(".clear-sel-button").click(function () {
        var clear_sel = $(this).data("sel_clear");
        $('select.boot-select#' + clear_sel).multipleSelect('setSelects', []);
        var mul_selected = false;
        $('select.boot-select:not(#' + clear_sel + '):not("#variable_name")').each(function () {
            if ($(this).multipleSelect('getSelects').length >= 2) {
                mul_selected = true;
            }
        });
        if (mul_selected === false) {
            $('select.boot-select#' + clear_sel).attr('multiple', 'multiple');
        }
        update_unavailable_select_options(clear_sel);
    });

    $("#clear-button").click(function () {
        clear_detailed_configurable_analysis();
    });

    function clear_detailed_configurable_analysis() {
        fe_all_scenarios = [];
        fe_all_regions = [];
        fe_all_models = [];
        $('#dca-scenario-next-btn').parent().hide();
        $('#dca-region-next-btn').parent().hide();
        $('#run-button').parent().addClass('disabled-select');
        $('#model_name').parent().find('.boot-select').addClass('disabled-select');
        $('#model_name').parent().find('label').addClass('disabled-select');
        $('.clear-sel-button[data-sel_clear="model_name"]').addClass('disabled-select');
        $('#dca-var-next-btn').parent().show();
        $('#variable_name').parent().find('.boot-select').removeClass('disabled-select');
        $('#variable_name').parent().find('label').removeClass('disabled-select');
        $('.clear-sel-button[data-sel_clear="variable_name"]').removeClass('disabled-select');
        $('#region_name').parent().find('.boot-select').addClass('disabled-select');
        $('#region_name').parent().find('label').addClass('disabled-select');
        $('.clear-sel-button[data-sel_clear="region_name"]').addClass('disabled-select');
        $('#scenario_name').parent().find('.boot-select').addClass('disabled-select');
        $('#scenario_name').parent().find('label').addClass('disabled-select');
        $('.clear-sel-button[data-sel_clear="scenario_name"]').addClass('disabled-select');
        $('#detailed_configurable_progress_text').text('Please select a Variable . . .');
        $('#dca_progress_bar div').css('width', '2%');
        $('#dca_progress_bar div').attr('aria-valuenow', '2');
        $('select.boot-select').multipleSelect('setSelects', []);
        $('select.boot-select:not("#variable_name")').attr('multiple', 'multiple');
        update_unavailable_select_options("clear_all");
        $('#detailed_filtering').removeClass("disabled_radio");
        initialise_sm_selects();

        $('#sdg_filtering').removeClass("disabled_radio");
        reset_all_variables();
        $("#all_variables").prop("checked", true).trigger("click");
        $('#visualisation_type_selection #piechart').parent().removeClass("disabled-select");

        $('#chart-side-info').hide();
        $('#viz_frame_div').hide();
        $('#chart_info').show();
        $('#example').DataTable().clear().draw();

    }
});


$("#run-button").click(function () {
    var viz_frame = $('#viz_frame_div');
    var chart_info = $('#chart-side-info');
    var model_sel = $('#model_name');
    var scenario_sel = $('#scenario_name');
    var region_sel = $('#region_name');
    var variable_sel = $('#variable_name');
    var variable_empty = (variable_sel.multipleSelect('getSelects').length === 0);
    if (variable_empty) {
        alert('Please, select a variable to complete the visualisation.')
    } else {
        $('#detailed_configurable_progress_text').text('You can choose among different types of visualisation, select another model or combination of models or completely clear the selected fields.');
        $('#dca_progress_bar div').css('width', '100%');
        $('#dca_progress_bar div').attr('aria-valuenow', '100');
        $('.viz-container').show();
        viz_frame.show();
        chart_info.show();
        /* Token Retrieval*/
        const csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        });

        /* # Query creation*/
        var jq_obj = create_query_json();
        retrieve_series_info_detailed(model_sel, scenario_sel, region_sel, variable_sel, jq_obj);

    }
});

function start_qc_v_process(model_sel, scenario_sel, region_sel, variable_sel, json_query_obj) {
    var query = {};
    query["query_name"] = "scientific_tool_query";
    query["parameters"] = json_query_obj['data'];
    create_chart_info_text(json_query_obj);
    var variable_selection = (variable_sel.multipleSelect('getSelects', 'text'));
    $.ajax({
        url: "/data_manager/create_query",
        type: "POST",
        data: JSON.stringify(query),
        contentType: 'application/json',
        success: function (data) {
            console.log("Detailed Configurable Analysis query created");
            var query_id = data['query_id'];
            create_visualisation(query_id, json_query_obj['val_list'], json_query_obj['title_list'], json_query_obj['unit_list'], variable_selection);
        },
        error: function (data) {
            console.log(data);
        }
    });
    populate_datatables(model_sel, scenario_sel, region_sel, variable_sel);
}


function create_visualisation(query_id, val_list, title_list, unit_list, variable) {
    var viz_frame = $('#viz_iframe');
    viz_frame.off();
    viz_frame.hide();
    $('#loading_bar').show();

    var data = {
        "y_var_names": val_list,
        "y_var_titles": title_list,
        "y_var_units": unit_list,
        "y_axis_title": String(variable),
        "x_axis_name": "year",
        "x_axis_title": "Year",
        "x_axis_unit": "-",
        "x_axis_type": "text",
        "color_list_request": ["moody_blue", "dark_blue", "violet", "light_red", "ceramic", "orange_yellow", "grey_green", "cyan", "black"],
        "dataset": query_id,
        "dataset_type": "query"
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
    var viz_selection = $('input[name="visualisation_input"]:checked').val();

    var complete_url = "/visualiser/"+ viz_selection +"?" + url;
    viz_frame.attr('src', complete_url);
    viz_frame.on('load', function () {
        $(this).show();
        $.ajax({
            url: "/data_manager/delete_query",
            type: "POST",
            data: JSON.stringify(query_id),
            contentType: 'application/json',
            success: function (data) {
                console.log("Detailed Configurable Analysis Temporary Query Deleted");
            },
            error: function (data) {
                console.log(data);
            }
        });

        $('#loading_bar').hide();

    });

}

function toTitleCase(str) {
    return str.replace(/(?:^|\s)\w/g, function (match) {
        return match.toUpperCase();
    });
}

function create_chart_info_text(query_obj) {
    $('#updated-chart-info').empty();
    var field_list = ['model', 'scenario', 'region', 'variable'];
    var multiple_field = query_obj['multiple_field'];
    field_list = field_list.filter(e => e !== multiple_field);
    var dynam_text = '';
    for (var j = 0; j < field_list.length; j++) {
        dynam_text = dynam_text + '<div>' + '<h5 style="margin-bottom: 0.4em; font-weight: 600">' + toTitleCase(field_list[j]) + "</h5>" + "<p style=\"margin-bottom: 0.7em;font-size: 0.9em\">" + String($('#' + field_list[j] + '_name').multipleSelect('getSelects', 'text')[0]) + '</p></div>';
    }
    dynam_text = dynam_text + '<h5 style="margin-bottom: 0.4em">' + toTitleCase(multiple_field) + 's </h5> <ul style="font-size:0.9em">';
    var multiple_values = $('#' + multiple_field + '_name').multipleSelect('getSelects', 'text');
    for (j = 0; j < multiple_values.length; j++) {
        dynam_text = dynam_text + '<li>' + multiple_values[j] + '</li>'
    }
    dynam_text = dynam_text + '</ul>'
    $(dynam_text).appendTo('#updated-chart-info');

}

//Close-down selects when pressing on the iframe

$('#viz_frame_div iframe').contents().find('body').click(function () {
    $('select.boot-select').multipleSelect('close');
});
