$(document).ready(function () {
    var viz_id= 'ida_benchmarking'

    var models = ['forecast','eu_times','nemesis','gcam','gemini_e3','aladin']
    var models_prettify = ['FORECAST','EU TIMES','NEMESIS','GCAM','GEMINI E3','ALADIN']
    var regions = ['EU28'];

    var units_mapping = {
        "Benchmarking|Industry|Energy intensity":"MJ/US$2010",
        "Benchmarking|Industry|GDP per capita":"k US$2010/capita",
        "Benchmarking|Industry|Electrification rate":"%",
        "Benchmarking|Industry|CO2 intensity (gross)":"Mt CO2/EJ",
        "Benchmarking|Industry|CO2 intensity (net)":"Mt CO2/EJ",
        "Benchmarking|Buildings|Energy per capita":"GJ/capita",
        "Benchmarking|Buildings|Electrification rate":"%",
        "Benchmarking|Buildings|District heat rate":"%",
        "Benchmarking|Buildings|CO2 intensity ":"Mt CO2/EJ",
        "Benchmarking|Transport|Energy per capita":"GJ/capita",
        "Benchmarking|Transport|Electrification rate":"%",
        "Benchmarking|Transport|Biofuel admixture quota":"%",
        "Benchmarking|Transport|CO2 intensity ":"Mt CO2/EJ",
    }


    $('select.indicator_scenario_select').multipleSelect('destroy').multipleSelect(
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
                create_ida_benchmarking_viz()
            },

        });
    
    $('select.indicator_variable_select').multipleSelect('destroy').multipleSelect(
        {
            filter: true,
            showClear: false,
            animate: 'fade',
            maxHeightUnit: 'row',
            maxHeight: 8,
            dropWidth: 250,
            selectAll: false,
            placeholder: 'Please select an indicator',
            onClick: function (data) {
                create_ida_benchmarking_viz()
            },

        });

    create_ida_benchmarking_viz()

    function create_ida_benchmarking_viz(){
        var viz_type = 'show_line_chart';
        var intrfc = 'ida_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        viz_frame.show();
        token_retrieval();

        var scenarios = $('#indicator_scenario_select').multipleSelect('getSelects')
        var variables = $('#indicator_variable_select').multipleSelect('getSelects')

        var y_var_models = models;
        var y_var_mod_titles = models_prettify;
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_models.length; i++) {
            for (var j = 0; j < scenarios.length; j++) {
                y_var_names.push(String(y_var_models[i]) + '_' + scenarios[j]);
                y_var_titles.push(String(y_var_mod_titles[i]) + ' - ' + scenarios[j]);
            }
        }

        /* # Query creation*/
        var jq_obj = create_ida_benchmarking_query(scenarios,variables);
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": y_var_titles,
            "y_var_units": Array(12).fill([units_mapping[variables[0]]]),
            "y_axis_title": variables[0],
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            // "min_max_y_value":[0.79, 2.92],
            "color_list_request": [
                "blue", "red", "orange", "green", "brown", "purple",
                "light_blue","light_red","yellow","light_brown","beige_purple"],
            "dataset_type": "query",
            "use_default_colors": false,
            // "type": "compare_4",
            // "type": "step_by_step"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)

    }
   


    function create_ida_benchmarking_query(scenarios,variables) {
        const input_dict = {
            'model__name': models,
            'scenario__name': scenarios,
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

         and_dict.push({
            'operand_1': 'year',
            'operand_2': '2020',
            'operation': '>='
        });

        and_dict.push({
            'operand_1': 'year',
            'operand_2': '2100',
            'operation': '<='
        });


        selected.push('value', 'year');
        const query_data = {
            "dataset": "i2amparis_main_idaresultscomp",
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
            "variables": variables,
            "query_data": query_data
        }

    }


});

