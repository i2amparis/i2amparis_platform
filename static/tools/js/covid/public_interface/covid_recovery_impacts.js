$(document).ready(function () {
    var co2_vars = ["CO2 emissions cuts|Absolute","CO2 emissions cuts|Relative"]
    var job_2025_vars = ["Energy Jobs 2025|Absolute","Energy Jobs 2025|Relative"]
    var job_2030_vars = ["Energy Jobs 2030|Absolute","Energy Jobs 2030|Relative"]
    var co2_units = ["MtCO2","%"]
    var job_units = ["1000 job-years","%"]

    var models = ['gcam', 'gemini_e3', 'tiam'];
    var scenarios = ['COVID Recovery - Average portfolio']


    $('select.country-select-impacts').multipleSelect('destroy').multipleSelect(
        {
            filter: true,
            showClear: false,
            animate: 'fade',
            maxHeightUnit: 'row',
            maxHeight: 8,
            dropWidth: 250,
            selectAll: false,
            placeholder: 'Please select a country/region',
            onClick: function (data) {
                create_covid_impacts_viz('covid_impacts_co2',co2_vars,co2_units)
                create_covid_impacts_viz('covid_impacts_jobs_2025',job_2025_vars,job_units)
                create_covid_impacts_viz('covid_impacts_jobs_2030',job_2030_vars,job_units)
            },

        });
    
    $('select.result_type_select').multipleSelect('destroy').multipleSelect(
        {
            filter: true,
            showClear: false,
            animate: 'fade',
            maxHeightUnit: 'row',
            maxHeight: 8,
            dropWidth: 250,
            selectAll: false,
            placeholder: 'Please select the type of results',
            onClick: function (data) {
                create_covid_impacts_viz('covid_impacts_co2',co2_vars,co2_units)
                create_covid_impacts_viz('covid_impacts_jobs_2025',job_2025_vars,job_units)
                create_covid_impacts_viz('covid_impacts_jobs_2030',job_2030_vars,job_units)
            },

        });

    create_covid_impacts_viz('covid_impacts_co2',co2_vars,co2_units)
    create_covid_impacts_viz('covid_impacts_jobs_2025',job_2025_vars,job_units)
    create_covid_impacts_viz('covid_impacts_jobs_2030',job_2030_vars,job_units)

    function create_covid_impacts_viz(viz_id,target_variables,target_units) {
        var viz_type = 'show_stacked_clustered_column_chart';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        var intrfc = 'covid_pub';

        var country = $('#country_select').multipleSelect('getSelects')[0]
        var results_type = $('#result_type_select').multipleSelect('getSelects')[0]

        if (results_type == "Absolute") {
            var variables = [target_variables[0]]
            var units = [target_units[0]]
        } else {
            var variables = [target_variables[1]]
            var units = [target_units[1]]
        }

        viz_frame.show();
        token_retrieval();
        var y_var_scenarios = scenarios;
        var y_var_scenarios_titles = [''];
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_scenarios.length; i++) {
            for (var j = 0; j < variables.length; j++) {
                y_var_names.push(String(y_var_scenarios[i]) + '_' + variables[j]);
                y_var_titles.push(String(y_var_scenarios_titles[i]) + ' - ' + variables[j]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_covid_impacts_query(2030, variables, country);
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": variables,
            "y_var_units": units,
            "y_axis_title": variables[0].split("|")[0],
            "x_axis_name": "model__title",
            "x_axis_title": "Model",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": y_var_scenarios,
            "cat_axis_titles": y_var_scenarios_titles,
            "use_default_colors": true,
            // "min_max_y_value":[0,1],
            // "color_list_request": ["orange","yellow","light_blue","blue","brown",
            //     "purple","green","dark_blue","light_green"],
            "dataset_type": "query",
            "type": "normal",
            "view_legend": false,
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }


    function create_covid_impacts_query(year, variables, country) {
        var regions = [country];
        var variables = variables;
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
            "dataset": "i2amparis_main_covidresultscomp",
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

