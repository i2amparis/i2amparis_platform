$(document).ready(function () {
    var covid_tech_vars = ["PV Investment Share","CSP Investment Share","Onshore wind Investment Share",
        "Offshore wind Investment Share","Geothermal Investment Share","Nuclear Investment Share","Biomass Investment Share",
        "Hydro Investment Share","Biofuels Investment Share"]
    var models = ['gcam', 'gemini_e3', 'tiam'];
    var scenarios = ['COVID Recovery - Max Emissions Cuts','COVID Recovery - Max Jobs 2025','COVID Recovery - Max Jobs 2030']


    $('select.country-select').multipleSelect('destroy').multipleSelect(
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
                create_optimal_tech_mix_viz('covid_portfolio',scenarios,data.value);
            },

        });
    
    create_optimal_tech_mix_viz('covid_portfolio',scenarios,'China')

    function create_optimal_tech_mix_viz(viz_id,target_scenarios,target_country) {
        var viz_type = 'show_stacked_clustered_column_chart';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        var intrfc = 'covid_pub';
        viz_frame.show();
        token_retrieval();
        var y_var_scenarios = target_scenarios;
        var y_var_scenarios_titles = [''];
        var variables = covid_tech_vars;
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_scenarios.length; i++) {
            for (var j = 0; j < variables.length; j++) {
                y_var_names.push(String(y_var_scenarios[i]) + '_' + variables[j]);
                y_var_titles.push(String(y_var_scenarios_titles[i]) + ' - ' + variables[j]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_optimal_tech_mix_query(2030, y_var_scenarios,target_country);

        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": variables,
            "y_var_units": ['-'],
            "y_axis_title": 'Share of technology',
            "x_axis_name": "model__title",
            "x_axis_title": "Model",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": y_var_scenarios,
            "cat_axis_titles": y_var_scenarios_titles,
            "use_default_colors": false,
            "min_max_y_value":[0,1],
            "color_list_request": ["orange","yellow","light_blue","blue","brown",
                "purple","green","dark_blue","light_green"],
            "dataset_type": "query",
            "type": "normal"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }


    function create_optimal_tech_mix_query(year, scenarios, country) {
        var regions = [country];
        var variables = covid_tech_vars;
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

