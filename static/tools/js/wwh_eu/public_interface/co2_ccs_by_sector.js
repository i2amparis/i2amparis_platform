$(document).ready(function () {

    $('select.model-select').multipleSelect('destroy').multipleSelect(
        {
            filter: true,
            showClear: false,
            animate: 'fade',
            maxHeightUnit: 'row',
            maxHeight: 8,
            dropWidth: 250,
            selectAll: false,
            placeholder: 'Please select a value',
            onClick: function () {
                run_co2_ccs_by_sector();
            },

        });


    var viz_id = 'co2_ccs_by_sector';
    var viz_type = 'show_stacked_column_line_chart';
    var intrfc = 'wwheu_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    function run_co2_ccs_by_sector() {
        /* # Query creation*/
        const models = $('#model_select').multipleSelect('getSelects');
        var jq_obj = create_co2_ccs_by_sector_query(models);
        console.log(viz_id + '- JSON Query Created');
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

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }
    run_co2_ccs_by_sector();

    function create_co2_ccs_by_sector_query(sel_models) {
        var regions = ['EU'];
        var scenarios = ['EUWWH'];
        var models = sel_models;
        var variables = ['Emissions|CO2|Energy', 'Extra_Carbon Sequestration|CCS|Industry', 'Extra_Carbon Sequestration|CCS|Power', 'Extra_Carbon Sequestration|CCS|Hydrogen', 'Extra_Carbon Sequestration|CCS|Other Transformation Processes'];

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
            "variables": variables,
            "regions": regions,
            "scenarios": scenarios,
            "query_data": query_data
        }

    }

    run_co2_ccs_by_sector();


});

