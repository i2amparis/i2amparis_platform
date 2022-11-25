$(document).ready(function () {
    var viz_id = 'hydrogen_production_by_fuel';
    var viz_type = 'show_stacked_clustered_column_chart';
    var intrfc = 'wwheu_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    /* # Query creation*/
    var jq_obj = create_hydrogen_production_by_fuel_query();
    console.log(viz_id + '- JSON Query Created');
    var viz_payload = {
        "y_var_names":  ['EU-TIMES_Secondary Energy|Hydrogen|Fossil|w/o CCS', 'EU-TIMES_Secondary Energy|Hydrogen|Fossil|w/ CCS', 'EU-TIMES_Secondary Energy|Hydrogen|Biomass|w/ CCS', 'EU-TIMES_Secondary Energy|Hydrogen|Biomass|w/o CCS', 'EU-TIMES_Secondary Energy|Hydrogen|Electricity', 'GCAM_Secondary Energy|Hydrogen|Fossil|w/o CCS', 'GCAM_Secondary Energy|Hydrogen|Fossil|w/ CCS', 'GCAM_Secondary Energy|Hydrogen|Biomass|w/ CCS', 'GCAM_Secondary Energy|Hydrogen|Biomass|w/o CCS', 'GCAM_Secondary Energy|Hydrogen|Electricity', 'TIAM_Secondary Energy|Hydrogen|Fossil|w/o CCS', 'TIAM_Secondary Energy|Hydrogen|Fossil|w/ CCS', 'TIAM_Secondary Energy|Hydrogen|Biomass|w/ CCS', 'TIAM_Secondary Energy|Hydrogen|Biomass|w/o CCS', 'TIAM_Secondary Energy|Hydrogen|Electricity'],
        "y_var_titles": ['Fossil without CCS', 'Fossil with CCS', 'Biomass with CCS', 'Biomass without CCS', 'Electricity', 'Fossil without CCS', 'Fossil with CCS', 'Biomass with CCS', 'Biomass without CCS', 'Electricity', 'Fossil without CCS', 'Fossil with CCS', 'Biomass with CCS', 'Biomass without CCS', 'Electricity'],
        "y_var_units": ['EJ/yr'],
        "y_axis_title": 'Hydrogen Production',
        "x_axis_name": "year",
        "x_axis_title": "Year",
        "x_axis_unit": "-",
        "x_axis_type": "text",
        "cat_axis_names": ['eu_times', 'gcam', 'tiam'],
        "cat_axis_titles": ['EU-TIMES', 'GCAM', 'TIAM'],
        "use_default_colors": false,
        "color_list_request": ["dark_gray","gray", "calm_brown", "brown", "blue"],
        "dataset_type": "query",
        "type": "normal"
    };

    start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)


    function create_hydrogen_production_by_fuel_query() {
        var regions = ['EU'];
        var models = ['eu_times', 'gcam', 'tiam'];
        var variables = [ 'Secondary Energy|Hydrogen|Fossil|w/o CCS', 'Secondary Energy|Hydrogen|Fossil|w/ CCS', 'Secondary Energy|Hydrogen|Biomass|w/ CCS', 'Secondary Energy|Hydrogen|Biomass|w/o CCS', 'Secondary Energy|Hydrogen|Electricity'];
        var scenarios = ['EUWWH'];
        var agg_func = 'Avg';
        var agg_var = 'model_id';

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
                "ordering": [
                    {
                        "parameter": "model__name",
                        "ascending": true
                    },
                    {
                        "parameter": "year",
                        "ascending": true
                    }
                ]
                ,
                "grouping": {
                    "params": [agg_var, "variable__name", "year", "region__name", "scenario__name"],
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

