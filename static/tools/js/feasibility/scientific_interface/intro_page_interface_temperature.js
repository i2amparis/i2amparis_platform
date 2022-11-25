$(document).ready(function () {

    $("#feasibility_temperature-clear-button").click(function () {
        $('#feasibility_temperature select.sum-boot-select').multipleSelect('setSelects', []);
        $('#feasibility_temperature_viz_frame_div').hide();
    });

    $("#feasibility_temperature-run-button").click(function () {
        var viz_frame = $('#feasibility_temperature_viz_frame_div');
        var model_sel = $('#feasibility_temperature_model_name');
        var scenario_sel = $('#feasibility_temperature_scenario_name');
        var region_sel = $('#feasibility_temperature_region_name');
        var model_full = (model_sel.multipleSelect('getSelects').length === 0);
        var scenario_full = (scenario_sel.multipleSelect('getSelects').length === 0);
        var region_full = (region_sel.multipleSelect('getSelects').length === 0);
        if (model_full || scenario_full || region_full) {
            alert('Please, select at least one value from each field to update the visualisation.')
        } else {
            viz_frame.show();
            /* Token Retrieval*/
            const csrftoken = getCookie('csrftoken');
            $.ajaxSetup({
                beforeSend: function (xhr) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            });

            /* # Query creation*/
            var jq_obj = create_feasibility_temperature_query();
            console.log('Temperature|Global Mean');
            retrieve_series_model_scenario(jq_obj);

        }
    });

    function start_qc_v_feasibility_temperature_process(variable, json_query_obj){
        var query = {};
        query["query_name"] = "feasibility_temperature_query";
        query["parameters"] = json_query_obj['data'];
        // var variable_selection = (variable_sel.multipleSelect('getSelects', 'text'));
        $.ajax({
            url: "/data_manager/create_query",
            type: "POST",
            data: JSON.stringify(query),
            contentType: 'application/json',
            success: function (data) {
                console.log('Temperature Query Saved in DB');
                var query_id = data['query_id'];
                create_visualisation_feasibility_temperature(query_id, json_query_obj, variable);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }


    function create_visualisation_feasibility_temperature(query_id, json_query_obj, variable) {
        var val_list = json_query_obj['val_list'];
        var title_list = json_query_obj['title_list'];
        var unit_list = json_query_obj['unit_list'];
        var color_list = json_query_obj['color_list'];
        var line_type_list = json_query_obj['line_type_list'];
        var viz_frame = $('#feasibility_temperature_viz_iframe');
        viz_frame.off();
        viz_frame.hide();
        $('#feasibility_temperature_loading_bar').show();
        console.log(val_list)

        var data = {
            "y_var_names": val_list,
            "y_var_titles": title_list,
            "y_var_units": unit_list,
            "y_axis_title": String(variable),
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            // "min_max_y_value":[11000, 43000],
            "color_list_request": color_list,
            "line_type_list": line_type_list,
            "use_default_colors": false,
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
        console.log('Temperature Ready to launch visualisation');
        var complete_url = "/visualiser/show_line_chart?" + url;
        viz_frame.attr('src', complete_url);
        viz_frame.on('load', function () {
            console.log('Temperature Visualisation Completed');
            $(this).show();
            $.ajax({
                url: "/data_manager/delete_query",
                type: "POST",
                data: JSON.stringify(query_id),
                contentType: 'application/json',
                success: function (data) {
                    console.log("Temperature Temporary Query Deleted");
                    // document_ready_counter = document_ready_counter + 1 ;
                    // check_document_ready(document_ready_counter);
                },
                error: function (data) {
                    console.log(data);
                }
            });

            $('#feasibility_temperature_loading_bar').hide();

        });

    }

    function create_feasibility_temperature_query() {
        var sel_model = $('#feasibility_temperature_model_name');
        var sel_scenario = $('#feasibility_temperature_scenario_name');
        var sel_region = $('#feasibility_temperature_region_name');
        var variable = ['Temperature|Global Mean'];

        const models = sel_model.multipleSelect('getSelects');
        const scenarios = sel_scenario.multipleSelect('getSelects');
        const regions = sel_region.multipleSelect('getSelects');

        const input_dict = {
            'model__name': models,
            'scenario__name': scenarios,
            'region__name': regions,
            'variable__name': variable
        };
        var selected = [];
        for (var i in input_dict) {
            if (input_dict[i].length > 0) {
                selected.push(i);
            }
        }
        var and_dict = [];
        var or_dict = [];
        for (var j in selected) {
            var temp = input_dict[selected[j]];

            and_dict.push({
                'operand_1': selected[j],
                'operand_2': temp,
                'operation': 'in'
            });
        }
        and_dict.push({
            'operand_1': 'year',
            'operand_2': '2015',
            'operation': '>='
        });


        selected.push('value', 'year');
        const query_data = {
            "dataset": "i2amparis_main_feasibilityresultscomp",
            "query_configuration": {
                "select": selected,
                "filter": {
                    "and": and_dict,
                    "or": or_dict
                },
                "ordering": [
                    {
                        "parameter": "model__name",
                        "ascending": true
                    },
                    {
                        "parameter": "scenario__name",
                        "ascending": true
                    },
                    {
                        "parameter": "year",
                        "ascending": true
                    }
                ]
                ,
                "grouping": {"params": [], "aggregated_params": []},
            },
            "additional_app_parameters": {}

        };

        return {
            "models": models,
            "regions": regions,
            "scenarios": scenarios,
            "variables": variable,
            "query_data": query_data
        }

    }

    function retrieve_series_model_scenario(jq_obj) {
        const units_info = {
            "model_name": jq_obj["models"],
            "region_name": jq_obj["regions"],
            "scenario_name": jq_obj["scenarios"],
            "variable_name": jq_obj["variables"],
            "dataset": 'i2amparis_main_feasibilityresultscomp'
        };
        var instances = [];
        var final_val_list = [];
        var final_title_list = [];
        var final_unit_list = [];
        var final_color_list = [];
        var final_line_type_list = [];        
        $.ajax({
            url: "/data_manager/retrieve_series_model_scenario",
            type: "POST",
            data: JSON.stringify(units_info),
            contentType: 'application/json',
            success: function (data) {
                console.log('Temperature Unit Info Retrieved');
                instances = data["instances"];
                for (var i = 0; i < instances.length; i++) {
                    final_val_list.push(instances[i]['series']);
                    final_title_list.push(instances[i]['title']);
                    final_unit_list.push(instances[i]['unit']);
                    final_color_list.push(instances[i]['color']);
                    final_line_type_list.push(instances[i]['line_type'])
                }
                var json_object = {
                    "data": jq_obj['query_data'],
                    "val_list": final_val_list,
                    "title_list": final_title_list,
                    "unit_list": final_unit_list,
                    "color_list": final_color_list,
                    "line_type_list": final_line_type_list
                };
                start_qc_v_feasibility_temperature_process(jq_obj["variables"], json_object)

            },
            error: function (data) {
                console.log(data);
            }
        });

    }

    $("#feasibility_temperature-run-button").trigger('click');
});

