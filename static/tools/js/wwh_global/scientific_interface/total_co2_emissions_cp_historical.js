$(document).ready(function () {

    var viz_id = 'total_co2_emissions_cp_historical';
    var viz_type = 'show_line_chart';
    var intrfc = 'wwhglobal_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    /* # Query creation*/
    var jq_obj = create_total_co2_emissions_cp_historical_query();
    console.log(viz_id + '- JSON Query Created');
    var viz_payload = {
        "y_var_names": ['Emissions|CO2|Energy'],
        "y_var_titles": ['CO2 Emissions'],
        "y_var_units": ['Mt CO2/yr'],
        "y_axis_title": 'Historical CO2 Emissions from Energy Use',
        "x_axis_name": "year",
        "x_axis_title": "Year",
        "x_axis_unit": "-",
        "x_axis_type": "text",
        "min_max_y_value":[11000, 43000],
        "color_list_request": ["black"],
        "dataset_type": "query",
        "use_default_colors": false,
        "type": "normal",
        // "type": "step_by_step"
    };

    start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)


    function create_total_co2_emissions_cp_historical_query() {
        var variable = ['Emissions|CO2|Energy'];


        const input_dict = {
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
            'operand_2': '2020',
            'operation': '<='
        });


        selected.push('value', 'year');
        const query_data = {
            "dataset": "i2amparis_main_historicaldata",
            "query_configuration": {
                "select": selected,
                "filter": {
                    "and": and_dict,
                    "or": or_dict
                },
                "ordering": [
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
            "variables": variable,
            "query_data": query_data
        }

    }


});

