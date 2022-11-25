$(document).ready(function () {

    function run_gpe_by_fuel_2() {
        var viz_frame = $('#global_primary_energy_by_fuel_2_viz_frame_div');
        viz_frame.show();
        /* Token Retrieval*/
        const csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        });
        /* # Query creation*/
        var jq_obj = create_global_primary_energy_by_fuel_2_query();
        console.log('Global Primary Energy by Fuel 2 JSON Query Created');
        console.log(jq_obj);
        start_qc_v_global_primary_energy_by_fuel_2_process(jq_obj);


    };

    function start_qc_v_global_primary_energy_by_fuel_2_process(json_query_obj) {
        var query = {};
        query["query_name"] = "primary_energy_by_fuel_avg_scenarios_query";
        query["parameters"] = json_query_obj['query_data'];
        $.ajax({
            url: "/data_manager/create_query",
            type: "POST",
            data: JSON.stringify(query),
            contentType: 'application/json',
            success: function (data) {
                console.log('Global Primary Energy by Fuel 2 Query Saved in DB');
                var query_id = data['query_id'];
                create_visualisation_global_primary_energy_by_fuel_2(query_id);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }


    function create_visualisation_global_primary_energy_by_fuel_2(query_id) {
        var viz_frame = $('#global_primary_energy_by_fuel_2_viz_iframe');
        viz_frame.off();
        viz_frame.hide();
        $('#global_primary_energy_by_fuel_2_loading_bar').show();

        var data = {
            "y_var_names": ['PR_CurPol_CP_Primary Energy|Wind', 'PR_CurPol_CP_Primary Energy|Solar', 'PR_CurPol_CP_Primary Energy|Hydro', 'PR_CurPol_CP_Primary Energy|Nuclear', 'PR_CurPol_CP_Primary Energy|Biomass', 'PR_CurPol_CP_Primary Energy|Gas', 'PR_CurPol_CP_Primary Energy|Oil', 'PR_CurPol_CP_Primary Energy|Coal', 'PR_CurPol_EI_Primary Energy|Wind', 'PR_CurPol_EI_Primary Energy|Solar', 'PR_CurPol_EI_Primary Energy|Hydro', 'PR_CurPol_EI_Primary Energy|Nuclear', 'PR_CurPol_EI_Primary Energy|Biomass', 'PR_CurPol_EI_Primary Energy|Gas', 'PR_CurPol_EI_Primary Energy|Oil', 'PR_CurPol_EI_Primary Energy|Coal', 'PR_NDC_CP_Primary Energy|Wind', 'PR_NDC_CP_Primary Energy|Solar', 'PR_NDC_CP_Primary Energy|Hydro', 'PR_NDC_CP_Primary Energy|Nuclear', 'PR_NDC_CP_Primary Energy|Biomass', 'PR_NDC_CP_Primary Energy|Gas', 'PR_NDC_CP_Primary Energy|Oil', 'PR_NDC_CP_Primary Energy|Coal', 'PR_NDC_EI_Primary Energy|Wind', 'PR_NDC_EI_Primary Energy|Solar', 'PR_NDC_EI_Primary Energy|Hydro', 'PR_NDC_EI_Primary Energy|Nuclear', 'PR_NDC_EI_Primary Energy|Biomass', 'PR_NDC_EI_Primary Energy|Gas', 'PR_NDC_EI_Primary Energy|Oil', 'PR_NDC_EI_Primary Energy|Coal'],
            "y_var_titles": ['Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal'],
            "y_var_units": ['EJ/y'],
            "y_axis_title": 'Global Primary Energy by Fuel',
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": ['PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'],
            "cat_axis_titles": ['PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'],
            "use_default_colors": false,
            "color_list_request": ["ice_gray", "gold", "lighter_blue", "oil_green", "calm_brown", "grey_green", "dark_gray", "gray"],
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
        console.log('Global Primary Energy Ready to launch visualisation');
        var complete_url = "/visualiser/show_stacked_clustered_column_chart?" + url;
        viz_frame.attr('src', complete_url);
        viz_frame.on('load', function () {
            document_ready_counter = document_ready_counter + 1;
            check_document_ready(document_ready_counter);
            console.log('Global Primary Energy by Fuel 2 Visualisation Completed');
            $(this).show();
            $.ajax({
                url: "/data_manager/delete_query",
                type: "POST",
                data: JSON.stringify(query_id),
                contentType: 'application/json',
                success: function (data) {
                    console.log("Global Primary Energy by Fuel 2 Temporary Query Deleted");
                },
                error: function (data) {
                    console.log(data);
                }
            });

            $('#global_primary_energy_by_fuel_2_loading_bar').hide();

        });

    }

    function create_global_primary_energy_by_fuel_2_query() {
        var regions = ['World'];
        var scenarios = ['PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'];
        var variables = ['Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal'];
        var agg_func = 'Avg';
        var agg_var = 'scenario_id';

        const input_dict = {
            'scenario__name': scenarios,
            'region__name': regions,
            'variable__name': variables
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
            'operand_2': '2050',
            'operation': '<='
        });


        selected.push('value', 'year');
        const query_data = {
            "dataset": "i2amparis_main_resultscomp",
            "query_configuration": {
                "select": selected,
                "filter": {
                    "and": and_dict,
                    "or": or_dict
                },
                "ordering": [
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
                "grouping": {
                    "params": [agg_var, "variable__name", "year", "region__name"],
                    "aggregated_params": [{"name": "value", "agg_func": agg_func}]
                },

            },
            "additional_app_parameters": {}

        };

        return {
            "scenarios": scenarios,
            "variables": variables,
            "regions": regions,
            "query_data": query_data
        }

    }

    run_gpe_by_fuel_2();




});

