$(document).ready(function () {

    var viz_id = 'total_co2_emissions';
    var viz_type = 'show_line_chart';
    var intrfc = 'wwheu_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    /* # Query creation*/
    var jq_obj = create_total_co2_emissions_query();
    console.log(viz_id + '- JSON Query Created');
    var viz_payload = {
                    "y_var_names": ['42_EUWWH', 'eu_times_EUWWH','e3me_EUWWH', 'gcam_EUWWH', 'gemini_e3_EUWWH', 'ices_EUWWH', 'muse_EUWWH','nemesis_EUWWH', 'tiam_EUWWH'],
                    "y_var_titles": ['42', 'EU-TIMES','E3ME', 'GCAM', 'Gemini-E3', 'ICES', 'MUSE','NEMESIS', 'TIAM'],
                    "y_var_units": ['MtCO2/y', 'MtCO2/y', 'MtCO2/y', 'MtCO2/y', 'MtCO2/y', 'MtCO2/y', 'MtCO2/y', 'MtCO2/y', 'MtCO2/y'],
                    "y_axis_title": 'Emissions|CO2|Energy',
                    "x_axis_name": "year",
                    "x_axis_title": "Year",
                    "x_axis_unit": "-",
                    "x_axis_type": "text",
                    "color_list_request": ["moody_blue", "cyan", "light_red", "orange_fire", "grey_green", "light_brown", "gold", "ice_gray" ,"purple"],
                    "dataset_type": "query",
                    "use_default_colors": false,
                    // "type": "step_by_step"
                };

    start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)


    function create_total_co2_emissions_query() {
        var models = ['42', 'e3me', 'eu_times', 'gcam', 'gemini_e3', 'ices', 'muse', 'nemesis', 'tiam'];
        var scenarios = ['EUWWH'];
        var regions = ['EU'];
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

