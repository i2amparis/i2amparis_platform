$(document).ready(function () {

    var viz_id = 'electrification_ir_co2_reduction';
    var viz_type = 'show_line_chart';
    var intrfc = 'wwheu_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    /* # Query creation*/
    var jq_obj = create_electrification_ir_co2_reduction_query();
    console.log(viz_id + '- JSON Query Created');
    var viz_payload = {
            "y_var_names": ['42','eu_times', 'e3me', 'gcam', 'gemini_e3','ices', 'muse', 'nemesis', 'tiam'],
            "y_var_titles": ['42','EU-TIMES', 'E3ME', 'GCAM', 'Gemini-E3', 'ICES','MUSE', 'NEMESIS', 'TIAM'],
            "y_var_units": ['Percentage %'],
            "y_axis_title": 'Electricity in Transport',
            "x_axis_name": "Extra_CO2_reduction_ratio",
            "x_axis_title": "CO2 emissions reduction",
            "x_axis_unit": "percentage %",
            "x_axis_type": "value",
            "use_default_colors": false,
            "color_list_request": ["moody_blue", "cyan", "light_red", "orange_fire", "grey_green", "light_brown", "gold", "ice_gray" ,"purple"],
            "dataset_type": "query",
            "type": "normal"
        };

    start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)


    function create_electrification_ir_co2_reduction_query() {
        var models = ['tiam', 'eu_times', 'e3me', 'gcam', 'gemini_e3', 'muse', 'nemesis', '42', 'ices'];
        var scenarios = ['EUWWH'];
        var regions = ['EU'];
        var variable = ['Extra_Electricity_Share', 'Extra_CO2_reduction_ratio'];


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
                "ordering": []
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

