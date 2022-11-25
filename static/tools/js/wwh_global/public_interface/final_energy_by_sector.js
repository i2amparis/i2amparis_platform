$(document).ready(function () {
    create_final_energy_sector_2020_viz();
    create_final_energy_sector_2030_viz();
    create_final_energy_sector_2050_viz();

    function create_final_energy_sector_2020_viz() {
        var viz_id = 'final_energy_sector_2020';
        var viz_type = 'show_stacked_clustered_column_chart';
        var intrfc = 'wwhglobal_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        viz_frame.show();
        token_retrieval();
        var y_var_scenarios = ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'];
        var y_var_scenarios_titles = ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'];
        var variables = ['Final Energy|Industry', 'Final Energy|Transportation',
            'Final Energy|Residential and Commercial', 'Final Energy|Other'];
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_scenarios.length; i++) {
            for (var j = 0; j < variables.length; j++) {
                y_var_names.push(String(y_var_scenarios[i]) + '_' + variables[j]);
                y_var_titles.push(String(y_var_scenarios_titles[i]) + ' - ' + variables[j]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_final_energy_by_fuel_query(2020, ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI']);
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": y_var_titles,
            "y_var_units": ['EJ/yr'],
            "y_axis_title": 'Final Energy',
            "x_axis_name": "model__title",
            "x_axis_title": "Model",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'],
            "cat_axis_titles": ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'],
            "use_default_colors": false,
            // 'min_max_y_value': [0, 450],
            "color_list_request": [ "dark_gray", "violet", "gold", "purple"],
            "dataset_type": "query",
            "type": "normal"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }

    function create_final_energy_sector_2030_viz() {
        var viz_id = 'final_energy_sector_2030';
        var viz_type = 'show_stacked_clustered_column_chart';
        var intrfc = 'wwhglobal_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        viz_frame.show();
        token_retrieval();
        var y_var_scenarios = ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'];
        var y_var_scenarios_titles = ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'];
        var variables = ['Final Energy|Industry', 'Final Energy|Transportation',
            'Final Energy|Residential and Commercial', 'Final Energy|Other'];
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_scenarios.length; i++) {
            for (var j = 0; j < variables.length; j++) {
                y_var_names.push(String(y_var_scenarios[i]) + '_' + variables[j]);
                y_var_titles.push(String(y_var_scenarios_titles[i]) + ' - ' + variables[j]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_final_energy_by_fuel_query(2030, ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI']);
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": y_var_titles,
            "y_var_units": ['EJ/yr'],
            "y_axis_title": 'Final Energy',
            "x_axis_name": "model__title",
            "x_axis_title": "Model",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'],
            "cat_axis_titles": ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'],
            "use_default_colors": false,
            "color_list_request": [ "dark_gray", "violet", "gold", "purple"],
            // 'min_max_y_value': [0, 450],
            "dataset_type": "query",
            "type": "normal"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }


    function create_final_energy_sector_2050_viz() {
        var viz_id = 'final_energy_sector_2050';
        var viz_type = 'show_stacked_clustered_column_chart';
        var intrfc = 'wwhglobal_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        viz_frame.show();
        token_retrieval();
        var y_var_scenarios = ['PR_Baseline', 'PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'];
        var y_var_scenarios_titles = ['PR_Baseline', 'PR_CurPol_EI', 'PR_NDC_EI'];
        var variables = ['Final Energy|Industry', 'Final Energy|Transportation',
            'Final Energy|Residential and Commercial', 'Final Energy|Other'];
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_scenarios.length; i++) {
            for (var j = 0; j < variables.length; j++) {
                y_var_names.push(String(y_var_scenarios[i]) + '_' + variables[j]);
                y_var_titles.push(String(y_var_scenarios_titles[i]) + ' - ' + variables[j]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_final_energy_by_fuel_query(2050, ['PR_Baseline', 'PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI']);
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": y_var_titles,
            "y_var_units": ['EJ/yr'],
            "y_axis_title": 'Final Energy',
            "x_axis_name": "model__title",
            "x_axis_title": "Model",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": ['PR_Baseline', 'PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'],
            "cat_axis_titles": ['PR_Baseline', 'PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'],
            "use_default_colors": false,
            "color_list_request": [ "dark_gray", "violet", "gold", "purple"],
            // 'min_max_y_value': [0, 450],
            "dataset_type": "query",
            "type": "normal"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }


    function create_final_energy_by_fuel_query(year, scenarios) {
        var regions = ['World'];
        var models = ['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'];
        var variables = ['Final Energy|Industry', 'Final Energy|Transportation',
            'Final Energy|Residential and Commercial', 'Final Energy|Other'];
        var agg_func = 'Avg';
        var agg_var = 'scenario_id';

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
        and_dict.push({
            'operand_1': 'year',
            'operand_2': year,
            'operation': '='
        });


        selected.push('value', 'year');
        const query_data = {
            "dataset": "i2amparis_main_resultscomp",
            "query_configuration": {
                "select": selected,
                "filter": {
                    "and": and_dict,
                    "or": or_dict
                },
                "ordering": [
                    {
                        "parameter": "model__title",
                        "ascending": true
                    }
                ]
                ,
                "grouping": {
                    "params": [agg_var, "variable__name", "year", "region__name", "model__title"],
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

