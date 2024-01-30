$(document).ready(function () {

    $('select.sector_select').multipleSelect('destroy').multipleSelect(
        {
            filter: true,
            showClear: false,
            animate: 'fade',
            maxHeightUnit: 'row',
            maxHeight: 8,
            dropWidth: 250,
            selectAll: false,
            placeholder: 'Please select a variable',
            onClick: function (data) {
                create_total_co2_emissions_viz()
            },

        });
    
    $('select.scenario_select').multipleSelect('destroy').multipleSelect(
        {
            filter: true,
            showClear: false,
            animate: 'fade',
            maxHeightUnit: 'row',
            maxHeight: 8,
            dropWidth: 250,
            selectAll: false,
            placeholder: 'Please select a scenario',
            onClick: function (data) {
                create_total_co2_emissions_viz()
            },

        });


    create_total_co2_emissions_viz()

    function create_total_co2_emissions_viz() {
        var viz_type = 'show_line_chart';
        var viz_id = 'total_co2_emissions';
        var intrfc = 'feasibility_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');


        var sector = $('#sector_select').multipleSelect('getSelects')[0]
        console.log(sector)
        var scenario = $('#scenario_select').multipleSelect('getSelects')[0]

        viz_frame.show();
        token_retrieval();

        var jq_obj = create_total_co2_emissions_query(sector,scenario);
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
                        "y_var_names": [`gcam_${scenario}`,`gemini_e3_${scenario}`,`muse_${scenario}`,`tiam_${scenario}`],
                        "y_var_titles": ['GCAM','Gemini-E3','MUSE','TIAM'],
                        "y_var_units": ['MtCO2/y', 'MtCO2/y', 'MtCO2/y', 'MtCO2/y'],
                        "y_axis_title": 'Emissions|CO2',
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
    }

    function create_total_co2_emissions_query(sector,scenario) {
        var models = ['gcam','gemini_e3','muse','tiam'];
        var scenarios = [scenario];
        var regions = ['World'];
        var variable = [sector];


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
            "dataset": "i2amparis_main_feasibilityresultscomp",
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



