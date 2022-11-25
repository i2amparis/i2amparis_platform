$(document).ready(function () {

    var viz_id = 'total_co2_emissions_ndc_ranges';
    var viz_type = 'show_dumbell_chart';
    var intrfc = 'wwhglobal_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();
    var y_var_models = ['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'];
    var y_var_mod_titles = ['42', 'E3ME', 'GCAM', 'Gemini-E3', 'ICES', 'MUSE', 'TIAM'];

    /* # Query creation*/
    var jq_obj = create_total_co2_emissions_ndc_ranges_query();
    console.log(viz_id + '- JSON Query Created');
    var viz_payload = {
        "y_var_names": y_var_models,
        "y_var_titles": y_var_mod_titles,
        "y_var_units": ['MtCO2/y'],
        "y_axis_title": 'Emissions|CO2|Energy',
        "x_axis_name": "category",
        "x_axis_title": "Models",
        "x_axis_unit": "-",
        "x_axis_type": "text",
        "color_list_request": ["moody_blue", "light_red", "orange_fire", "grey_green", "light_brown", "gold", "purple"],
        "dataset_type": "query",
        "use_default_colors": false,
        "min_max_y_value":[22000, 48000]
        // "type": "step_by_step"
    };

    start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)


    function create_total_co2_emissions_ndc_ranges_query() {
        var models = ['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'];
        var scenarios = ['PR_NDC_CP', 'PR_NDC_EI', 'PR_Baseline'];
        var regions = ['World'];
        var variable = ['Emissions|CO2|Energy'];


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
            'operand_2': '2050',
            'operation': '<='
        });
        and_dict.push({
            'operand_1': 'value',
            'operand_2': 0,
            'operation': '>'
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


});

