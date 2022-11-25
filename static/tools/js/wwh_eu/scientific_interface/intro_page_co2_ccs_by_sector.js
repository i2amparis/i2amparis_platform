$(document).ready(function () {

    $("#ccs1-clear-button").click(function () {
        $('#ccs1 select.sum-boot-select').multipleSelect('setSelects', []);
        $('#ccs1_viz_frame_div').hide();
    });

    $("#ccs1-run-button").click(function () {
        var viz_id = 'ccs1';
        var viz_type = 'show_stacked_column_line_chart';
        var intrfc = 'eu_wwh_scientific';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        var dataset = 'i2amparis_main_wwheuresultscomp';
        var model_sel = $('#ccs1_model_name');
        var model_full = (model_sel.multipleSelect('getSelects').length === 0);
        if (model_full) {
            alert('Please, select at least one value from each field to update the visualisation.')
        } else {
            viz_frame.show();

            /* # Query creation*/
            var jq_obj = create_ccs1_query(dataset);
            console.log(viz_id + ' - JSON Query Created');
            var viz_payload = {
                "y_var_names": ['Extra_Carbon Sequestration|CCS|Industry', 'Extra_Carbon Sequestration|CCS|Power', 'Extra_Carbon Sequestration|CCS|Hydrogen', 'Extra_Carbon Sequestration|CCS|Other Transformation Processes'],
                "y_var_titles": ['Industry', 'Electricity', 'Hydrogen ', 'Other transformation processes'],
                "y_var_units": ['Mt CO2/y', 'Mt CO2/y'],
                "y_axis_title": ['CO2 Captured', 'CO2 Emissions'],
                "x_axis_name": "year",
                "x_axis_title": "Year",
                "x_axis_unit": "-",
                "x_axis_type": "text",
                "line_names": ['Emissions|CO2|Energy'],
                "line_titles": ['CO2 Emissions'],
                "use_default_colors": false,
                "color_list_request": ["dark_gray", "blue", "casual_green", "light_red"],
                "dataset_type": "query"
            };
            start_sci_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)

        }
    });


    function create_ccs1_query(dataset) {
        var sel_model = $('#ccs1_model_name');
        var variable = ['Emissions|CO2|Energy', 'Extra_Carbon Sequestration|CCS|Industry', 'Extra_Carbon Sequestration|CCS|Power', 'Extra_Carbon Sequestration|CCS|Hydrogen', 'Extra_Carbon Sequestration|CCS|Other Transformation Processes'];

        const models = sel_model.multipleSelect('getSelects');
        const scenarios = ['EUWWH'];
        const regions = ['EU']

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
            "dataset": dataset,
            "query_configuration": {
                "select": selected,
                "filter": {
                    "and": and_dict,
                    "or": or_dict
                },
                "ordering": [{
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


    $("#ccs1-run-button").trigger('click');
});

