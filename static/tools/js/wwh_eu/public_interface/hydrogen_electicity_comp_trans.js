$(document).ready(function () {
    var viz_id = 'hydrogen_electricity_comp_trans';
    var viz_type = 'show_stacked_clustered_column_chart';
    var intrfc = 'wwheu_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    /* # Query creation*/
    var jq_obj = create_hydrogen_electricity_comp_trans_query();
    console.log(viz_id + '- JSON Query Created');
    var viz_payload = {
        "y_var_names": ['EU-TIMES_Final Energy|Transportation|Hydrogen', 'EU-TIMES_Final Energy|Transportation|Non-hydrogen', 'ALADIN_Final Energy|Transportation|Hydrogen', 'ALADIN_Final Energy|Transportation|Non-hydrogen', 'GCAM_Final Energy|Transportation|Hydrogen', 'GCAM_Final Energy|Transportation|Non-hydrogen', 'TIAM_Final Energy|Transportation|Hydrogen', 'TIAM_Final Energy|Transportation|Non-hydrogen'],
        "y_var_titles": ['Hydrogen', 'Non-Hydrogen', 'Hydrogen', 'Non-Hydrogen', 'Hydrogen', 'Non-Hydrogen', 'Hydrogen', 'Non-Hydrogen'],
        "y_var_units": ['EJ/yr'],
        "y_axis_title": "Final Energy in Transportation",
        "x_axis_name": "year",
        "x_axis_title": "Year",
        "x_axis_unit": "-",
        "x_axis_type": "text",
        "cat_axis_names": ['eu_times', 'aladin', 'gcam', 'tiam'],
        "cat_axis_titles": ['EU-TIMES', 'ALADIN', 'GCAM', 'TIAM'],
        "use_default_colors": false,
        "color_list_request": ["casual_green", "gray"],
        "dataset_type": "query",
        "type": "normal"
    };
    start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)


    function create_hydrogen_electricity_comp_trans_query() {
        var regions = ['EU'];
        var models = ['eu_times', 'aladin', 'gcam', 'tiam'];
        var scenarios = ['EUWWH'];
        var variables = ['Final Energy|Transportation|Hydrogen', 'Final Energy|Transportation|Non-hydrogen'];
        var agg_var = 'model_id';
        var agg_func = 'Avg';

        const input_dict = {
            'model__name': models,
            'region__name': regions,
            'variable__name': variables,
            'scenario__name': scenarios
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
                    "params": [agg_var, "variable__name", "year", "region__name", "scenario__name"],
                    "aggregated_params": [{"name": "value", "agg_func": agg_func}]
                },

            },
            "additional_app_parameters": {}

        };

        return {
            "models": models,
            "variables": variables,
            "regions": regions,
            "scenarios": scenarios,
            "query_data": query_data
        }

    }


});

