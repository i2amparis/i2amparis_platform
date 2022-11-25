$(document).ready(function () {

    var viz_id = 'energy_co2_emissions_by_sector';
    var viz_type = 'show_stacked_clustered_column_chart';
    var intrfc = 'wwheu_pub';
    var viz_frame = $('#' + viz_id + '_viz_frame_div');
    viz_frame.show();
    token_retrieval();

    /* # Query creation*/
    var jq_obj = create_energy_co2_emissions_by_sector_query();
    console.log(viz_id + '- JSON Query Created');
    var viz_payload = {
        "y_var_names": ['ALADIN_Emissions|CO2|Energy|Supply', 'ALADIN_Emissions|CO2|Energy|Demand|Industry', 'ALADIN_Emissions|CO2|Energy|Demand|Residential and Commercial', 'ALADIN_Emissions|CO2|Energy|Demand|Transportation', 'ALADIN_Emissions|CO2|Energy|Demand|AFOFI', 'ALADIN_Emissions|CO2|Energy|Demand|Other Sector', 'E3ME_Emissions|CO2|Energy|Supply', 'E3ME_Emissions|CO2|Energy|Demand|Industry', 'E3ME_Emissions|CO2|Energy|Demand|Residential and Commercial', 'E3ME_Emissions|CO2|Energy|Demand|Transportation', 'E3ME_Emissions|CO2|Energy|Demand|AFOFI', 'E3ME_Emissions|CO2|Energy|Demand|Other Sector', 'EU-TIMES_Emissions|CO2|Energy|Supply', 'EU-TIMES_Emissions|CO2|Energy|Demand|Industry', 'EU-TIMES_Emissions|CO2|Energy|Demand|Residential and Commercial', 'EU-TIMES_Emissions|CO2|Energy|Demand|Transportation', 'EU-TIMES_Emissions|CO2|Energy|Demand|AFOFI', 'EU-TIMES_Emissions|CO2|Energy|Demand|Other Sector', 'FORECAST_Emissions|CO2|Energy|Supply', 'FORECAST_Emissions|CO2|Energy|Demand|Industry', 'FORECAST_Emissions|CO2|Energy|Demand|Residential and Commercial', 'FORECAST_Emissions|CO2|Energy|Demand|Transportation', 'FORECAST_Emissions|CO2|Energy|Demand|AFOFI', 'FORECAST_Emissions|CO2|Energy|Demand|Other Sector', '42_Emissions|CO2|Energy|Supply', '42_Emissions|CO2|Energy|Demand|Industry', '42_Emissions|CO2|Energy|Demand|Residential and Commercial', '42_Emissions|CO2|Energy|Demand|Transportation', '42_Emissions|CO2|Energy|Demand|AFOFI', '42_Emissions|CO2|Energy|Demand|Other Sector', 'GCAM_Emissions|CO2|Energy|Supply', 'GCAM_Emissions|CO2|Energy|Demand|Industry', 'GCAM_Emissions|CO2|Energy|Demand|Residential and Commercial', 'GCAM_Emissions|CO2|Energy|Demand|Transportation', 'GCAM_Emissions|CO2|Energy|Demand|AFOFI', 'GCAM_Emissions|CO2|Energy|Demand|Other Sector', 'Gemini-E3_Emissions|CO2|Energy|Supply', 'Gemini-E3_Emissions|CO2|Energy|Demand|Industry', 'Gemini-E3_Emissions|CO2|Energy|Demand|Residential and Commercial', 'Gemini-E3_Emissions|CO2|Energy|Demand|Transportation', 'Gemini-E3_Emissions|CO2|Energy|Demand|AFOFI', 'Gemini-E3_Emissions|CO2|Energy|Demand|Other Sector', 'ICES_Emissions|CO2|Energy|Supply', 'ICES_Emissions|CO2|Energy|Demand|Industry', 'ICES_Emissions|CO2|Energy|Demand|Residential and Commercial', 'ICES_Emissions|CO2|Energy|Demand|Transportation', 'ICES_Emissions|CO2|Energy|Demand|AFOFI', 'ICES_Emissions|CO2|Energy|Demand|Other Sector', 'MUSE_Emissions|CO2|Energy|Supply', 'MUSE_Emissions|CO2|Energy|Demand|Industry', 'MUSE_Emissions|CO2|Energy|Demand|Residential and Commercial', 'MUSE_Emissions|CO2|Energy|Demand|Transportation', 'MUSE_Emissions|CO2|Energy|Demand|AFOFI', 'MUSE_Emissions|CO2|Energy|Demand|Other Sector', 'NEMESIS_Emissions|CO2|Energy|Supply', 'NEMESIS_Emissions|CO2|Energy|Demand|Industry', 'NEMESIS_Emissions|CO2|Energy|Demand|Residential and Commercial', 'NEMESIS_Emissions|CO2|Energy|Demand|Transportation', 'NEMESIS_Emissions|CO2|Energy|Demand|AFOFI', 'NEMESIS_Emissions|CO2|Energy|Demand|Other Sector', 'TIAM_Emissions|CO2|Energy|Supply', 'TIAM_Emissions|CO2|Energy|Demand|Industry', 'TIAM_Emissions|CO2|Energy|Demand|Residential and Commercial', 'TIAM_Emissions|CO2|Energy|Demand|Transportation', 'TIAM_Emissions|CO2|Energy|Demand|AFOFI', 'TIAM_Emissions|CO2|Energy|Demand|Other Sector'],
        "y_var_titles": ['Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors', 'Energy Supply', ' Industry', 'Residential and Commercial ', 'Transportation', 'Agriculture, Forestry and Fisheries', 'Other sectors'],
        "y_var_units": ['MtCO2/y'],
        "y_axis_title": 'CO2 Emissions',
        "x_axis_name": "year",
        "x_axis_title": "Year",
        "x_axis_unit": "-",
        "x_axis_type": "text",
        "cat_axis_names": ['aladin', 'e3me', 'eu_times', 'forecast', '42', 'gcam', 'gemini_e3', 'ices', 'muse', 'nemesis', 'tiam'],
        "cat_axis_titles": ['ALADIN', 'E3ME', 'EU-TIMES', 'FORECAST', '42', 'GCAM', 'Gemini-E3', 'ICES', 'MUSE', 'NEMESIS', 'TIAM'],
        "use_default_colors": false,
        "color_list_request": ["blue", "dark_gray", "gold", "violet", "calm_brown", "gray"],
        "dataset_type": "query",
        "type": "normal"
    };

    start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)


    function create_energy_co2_emissions_by_sector_query() {
        var regions = ['EU'];
        var models = ['aladin', 'e3me', 'eu_times', 'forecast', '42', 'gcam', 'gemini_e3', 'ices', 'muse', 'nemesis', 'tiam'];
        var variables = ['Emissions|CO2|Energy|Supply', 'Emissions|CO2|Energy|Demand|Industry', 'Emissions|CO2|Energy|Demand|Residential and Commercial', 'Emissions|CO2|Energy|Demand|Transportation', 'Emissions|CO2|Energy|Demand|AFOFI', 'Emissions|CO2|Energy|Demand|Other Sector'];
        var agg_func = 'Avg';
        var agg_var = 'model_id';

        const input_dict = {
            'model__name': models,
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
                    "params": [agg_var, "variable__name", "year", "region__name"],
                    "aggregated_params": [{"name": "value", "agg_func": agg_func}]
                },

            },
            "additional_app_parameters": {}

        };

        return {
            "models": models,
            "variables": variables,
            "regions": regions,
            "query_data": query_data
        }

    }


});

