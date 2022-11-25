$(document).ready(function () {
    var viz_id = 'electrification_fec';
    var viz_type = 'show_stacked_clustered_column_chart';
    var intrfc = 'wwheu_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    /* # Query creation*/
    var jq_obj = create_electrification_fec_query();
    console.log(viz_id + '- JSON Query Created');
    var viz_payload = {
            "y_var_names": ['ALADIN_Final Energy|Transportation|Electricity', 'ALADIN_Final Energy|Transportation|Non-Electricity', 'E3ME_Final Energy|Transportation|Electricity', 'E3ME_Final Energy|Transportation|Non-Electricity', 'EU-TIMES_Final Energy|Transportation|Electricity', 'EU-TIMES_Final Energy|Transportation|Non-Electricity', '42_Final Energy|Transportation|Electricity', '42_Final Energy|Transportation|Non-Electricity', 'GCAM_Final Energy|Transportation|Electricity', 'GCAM_Final Energy|Transportation|Non-Electricity', 'Gemini-E3_Final Energy|Transportation|Electricity', 'Gemini-E3_Final Energy|Transportation|Non-Electricity', 'ICES_Final Energy|Transportation|Electricity', 'ICES_Final Energy|Transportation|Non-Electricity', 'MUSE_Final Energy|Transportation|Electricity', 'MUSE_Final Energy|Transportation|Non-Electricity', 'NEMESIS_Final Energy|Transportation|Electricity', 'NEMESIS_Final Energy|Transportation|Non-Electricity', 'TIAM_Final Energy|Transportation|Electricity', 'TIAM_Final Energy|Transportation|Non-Electricity'],
            "y_var_titles": ['Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity', 'Electricity', 'Non-Electricity'],
            "y_var_units": ['EJ/y'],
            "y_axis_title": 'Transport Final Energy',
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": ['aladin', 'e3me', 'eu_times', '42', 'gcam', 'gemini_e3', 'ices', 'muse', 'nemesis', 'tiam'],
            "cat_axis_titles": ['ALADIN', 'E3ME', 'EU-TIMES', '42', 'GCAM', 'Gemini-E3', 'ICES', 'MUSE', 'NEMESIS', 'TIAM'],
            "use_default_colors": false,
            "color_list_request": ["light_blue", "gray", "dark_gray", "grey_green"],
            "dataset_type": "query",
            "type": "normal"
        };

    start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)


    function create_electrification_fec_query() {
        var regions = ['EU'];
        var models = ['aladin', 'e3me', 'eu_times', '42', 'gcam', 'gemini_e3', 'ices', 'muse', 'nemesis', 'tiam'];
        var variables = ['Final Energy|Transportation|Electricity', 'Final Energy|Transportation|Non-Electricity'];
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


        selected.push('value', 'year');
        const query_data = {
            "dataset": "i2amparis_main_wwheuresultscomp",
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


});

