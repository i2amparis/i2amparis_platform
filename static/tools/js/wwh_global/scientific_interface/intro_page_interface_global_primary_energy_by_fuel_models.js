$(document).ready(function () {

    function run_gpe_by_fuel_1() {
        var viz_frame = $('#global_primary_energy_by_fuel_1_viz_frame_div');
        viz_frame.show();
        /* Token Retrieval*/
        const csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        });
        /* # Query creation*/
        var jq_obj = create_global_primary_energy_by_fuel_1_query();
        console.log(jq_obj);
        console.log('Global Primary Energy by Fuel 1 JSON Query Created');
        start_qc_v_global_primary_energy_by_fuel_1_process(jq_obj);


    };

    function start_qc_v_global_primary_energy_by_fuel_1_process(json_query_obj) {
        var query = {};
        query["query_name"] = "primary_energy_by_fuel_avg_models_query";
        query["parameters"] = json_query_obj['query_data'];
        $.ajax({
            url: "/data_manager/create_query",
            type: "POST",
            data: JSON.stringify(query),
            contentType: 'application/json',
            success: function (data) {
                console.log('Global Primary Energy by Fuel 1 Query Saved in DB');
                var query_id = data['query_id'];
                create_visualisation_global_primary_energy_by_fuel_1(query_id);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }


    function create_visualisation_global_primary_energy_by_fuel_1(query_id) {
        var viz_frame = $('#global_primary_energy_by_fuel_1_viz_iframe');
        viz_frame.off();
        viz_frame.hide();
        $('#global_primary_energy_by_fuel_1_loading_bar').show();

        var data = {
            "y_var_names": ['42_Primary Energy|Wind', '42_Primary Energy|Solar', '42_Primary Energy|Hydro', '42_Primary Energy|Nuclear', '42_Primary Energy|Biomass', '42_Primary Energy|Gas', '42_Primary Energy|Oil', '42_Primary Energy|Coal', 'E3EME_Primary Energy|Wind', 'E3EME_Primary Energy|Solar', 'E3EME_Primary Energy|Hydro', 'E3EME_Primary Energy|Nuclear', 'E3EME_Primary Energy|Biomass', 'E3EME_Primary Energy|Gas', 'E3EME_Primary Energy|Oil', 'E3EME_Primary Energy|Coal', 'GCAM_Primary Energy|Wind', 'GCAM_Primary Energy|Solar', 'GCAM_Primary Energy|Hydro', 'GCAM_Primary Energy|Nuclear', 'GCAM_Primary Energy|Biomass', 'GCAM_Primary Energy|Gas', 'GCAM_Primary Energy|Oil', 'GCAM_Primary Energy|Coal', 'Gemini-E3_Primary Energy|Wind', 'Gemini-E3_Primary Energy|Solar', 'Gemini-E3_Primary Energy|Hydro', 'Gemini-E3_Primary Energy|Nuclear', 'Gemini-E3_Primary Energy|Biomass', 'Gemini-E3_Primary Energy|Gas', 'Gemini-E3_Primary Energy|Oil', 'Gemini-E3_Primary Energy|Coal', 'ICES_Primary Energy|Wind', 'ICES_Primary Energy|Solar', 'ICES_Primary Energy|Hydro', 'ICES_Primary Energy|Nuclear', 'ICES_Primary Energy|Biomass', 'ICES_Primary Energy|Gas', 'ICES_Primary Energy|Oil', 'ICES_Primary Energy|Coal', 'MUSE_Primary Energy|Wind', 'MUSE_Primary Energy|Solar', 'MUSE_Primary Energy|Hydro', 'MUSE_Primary Energy|Nuclear', 'MUSE_Primary Energy|Biomass', 'MUSE_Primary Energy|Gas', 'MUSE_Primary Energy|Oil', 'MUSE_Primary Energy|Coal', 'TIAM_Primary Energy|Wind', 'TIAM_Primary Energy|Solar', 'TIAM_Primary Energy|Hydro', 'TIAM_Primary Energy|Nuclear', 'TIAM_Primary Energy|Biomass', 'TIAM_Primary Energy|Gas', 'TIAM_Primary Energy|Oil', 'TIAM_Primary Energy|Coal'],
            "y_var_titles": ['Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal', 'Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal'],
            "y_var_units": ['EJ/y'],
            "y_axis_title": 'Global Primary Energy by Fuel',
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": ['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'],
            "cat_axis_titles": ['42', 'E3EME', 'GCAM', 'Gemini-E3', 'ICES', 'MUSE', 'TIAM'],
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
            console.log('Global Primary Energy by Fuel 1 Visualisation Completed');
            $(this).show();
            $.ajax({
                url: "/data_manager/delete_query",
                type: "POST",
                data: JSON.stringify(query_id),
                contentType: 'application/json',
                success: function (data) {
                    console.log("Global Primary Energy by Fuel 1 Temporary Query Deleted");
                },
                error: function (data) {
                    console.log(data);
                }
            });

            $('#global_primary_energy_by_fuel_1_loading_bar').hide();

        });

    }

    function create_global_primary_energy_by_fuel_1_query() {
        var regions = ['World'];
        var models = ['42','e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'];
        var variables = ['Primary Energy|Wind', 'Primary Energy|Solar', 'Primary Energy|Hydro', 'Primary Energy|Nuclear', 'Primary Energy|Biomass', 'Primary Energy|Gas', 'Primary Energy|Oil', 'Primary Energy|Coal'];
        var agg_func = 'Avg';
        var agg_var = 'model_id';

        const input_dict = {
            'model__name': models,
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
                        "parameter": "model__name",
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
            "models": models,
            "variables": variables,
            "regions": regions,
            "query_data": query_data
        }

    }

    run_gpe_by_fuel_1();




});

