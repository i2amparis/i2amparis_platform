$(document).ready(function () {
    create_final_energy_sector_industry_viz();
    create_final_energy_sector_transportation_viz();
    create_final_energy_sector_buildings_viz();

    function create_final_energy_sector_industry_viz() {
        var viz_id = 'final_energy_sector_industry';
        var viz_type = 'show_line_chart';
        var intrfc = 'wwhglobal_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        viz_frame.show();
        token_retrieval();
        var y_var_models = ['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'];
        var y_var_mod_titles = ['42', 'E3ME', 'GCAM', 'Gemini-E3', 'ICES', 'MUSE', 'TIAM'];
        var scenarios = ['PR_Baseline', 'PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'];
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_models.length; i++) {
            for (var j = 0; j < scenarios.length; j++) {
                y_var_names.push(String(y_var_models[i]) + '_' + scenarios[j]);
                y_var_titles.push(String(y_var_mod_titles[i]) + ' - ' + scenarios[j]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_final_energy_by_fuel_query('Final Energy|Industry');
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": y_var_titles,
            "y_var_units": ['EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr'],
            "y_axis_title": 'Final Energy in Industry',
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "use_default_colors": false,
            "min_max_y_value":[],
            "color_list_request": ["moody_blue", "light_red", "orange_fire", "grey_green", "light_brown", "gold", "purple"],
            "dataset_type": "query",
            "type": "compare_5"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }

    function create_final_energy_sector_transportation_viz() {
        var viz_id = 'final_energy_sector_transportation';
        var viz_type = 'show_line_chart';
        var intrfc = 'wwhglobal_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        viz_frame.show();
        token_retrieval();
        var y_var_models = ['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'];
        var y_var_mod_titles = ['42', 'E3ME', 'GCAM', 'Gemini-E3', 'ICES', 'MUSE', 'TIAM'];
        var scenarios = ['PR_Baseline', 'PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'];
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_models.length; i++) {
            for (var j = 0; j < scenarios.length; j++) {
                y_var_names.push(String(y_var_models[i]) + '_' + scenarios[j]);
                y_var_titles.push(String(y_var_mod_titles[i]) + ' - ' + scenarios[j]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_final_energy_by_fuel_query('Final Energy|Transportation');
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": y_var_titles,
            "y_var_units": ['EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr'],
            "y_axis_title": 'Final Energy in Transportation',
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "use_default_colors": false,
            "min_max_y_value": [],
            "color_list_request": ["moody_blue", "light_red", "orange_fire", "grey_green", "light_brown", "gold", "purple"],
            "dataset_type": "query",
            "type": "compare_5"
        };
        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }


    function create_final_energy_sector_buildings_viz() {
        var viz_id = 'final_energy_sector_buildings';
        var viz_type = 'show_line_chart';
        var intrfc = 'wwhglobal_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        viz_frame.show();
        token_retrieval();
        var y_var_models = ['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'];
        var y_var_mod_titles = ['42', 'E3ME', 'GCAM', 'Gemini-E3', 'ICES', 'MUSE', 'TIAM'];
        var scenarios = ['PR_Baseline', 'PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'];
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_models.length; i++) {
            for (var j = 0; j < scenarios.length; j++) {
                y_var_names.push(String(y_var_models[i]) + '_' + scenarios[j]);
                y_var_titles.push(String(y_var_mod_titles[i]) + ' - ' + scenarios[j]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_final_energy_by_fuel_query('Final Energy|Residential and Commercial');
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": y_var_titles,
            "y_var_units": ['EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr', 'EJ/yr'],
            "y_axis_title": 'Final Energy in Buildings',
            "x_axis_name": "year",
            "x_axis_title": "Year",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "use_default_colors": false,
            "min_max_y_value": [],
            "color_list_request": ["moody_blue", "light_red", "orange_fire", "grey_green", "light_brown", "gold", "purple"],
            "dataset_type": "query",
            "type": "compare_5"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }


    function create_final_energy_by_fuel_query(variable) {
        var regions = ['World'];
        var models = ['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam'];
        var scenarios = ['PR_Baseline', 'PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'];
        var variables = [variable];
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
            'operand_2': '2050',
            'operation': '<='
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
            "variables": variables,
            "regions": regions,
            "scenarios": scenarios,
            "query_data": query_data
        }

    }


});

