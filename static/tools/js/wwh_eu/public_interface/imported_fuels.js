$(document).ready(function () {

   $('select.model-select2').multipleSelect('destroy').multipleSelect(
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
                run_imported_fuels();
            },

        });

    var viz_id = 'imported_fuels';
    var viz_type = 'show_line_chart';
    var intrfc = 'wwheu_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    function run_imported_fuels() {
        /* # Query creation*/
        const variables = $('#model_select2').multipleSelect('getSelects');
        var jq_obj = create_imported_fuels_query(variables)
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": ['eu_times',  'gemini_e3', 'tiam'],
            "y_var_titles": ['EU-TIMES', 'Gemini-E3',  'TIAM'],
            "y_var_units": ['billion US$2010/yr OR local currency', 'billion US$2010/yr OR local currency', 'billion US$2010/yr OR local currency'],
            "y_axis_title": 'Imported fossil fuels',
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "use_default_colors": false,
            "color_list_request": ["cyan", "grey_green", "purple"],
            "dataset_type": "query",
            "stacked": "false",
            // "type": "step_by_step"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }
    run_imported_fuels();


    function create_imported_fuels_query(sel_variables) {
        var models = ['eu_times', 'tiam', 'gemini_e3'];
        var scenarios = ['EUWWH'];
        var regions = ['EU'];
        var variable = sel_variables;


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

