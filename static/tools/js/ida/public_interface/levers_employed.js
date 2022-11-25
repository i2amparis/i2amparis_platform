$(document).ready(function () {
    var viz_id = 'ida_levers'

    var models = ['forecast','eu_times','nemesis','gcam','gemini_e3','aladin']
    var models_prettify = ['FORECAST','EU TIMES','NEMESIS','GCAM','GEMINI E3','ALADIN']
    var regions = ['EU28'];
    var year = 2050

    var sector_var_mapping = {
    "Power":[
        "IDA|Emissions|CO2|Energy|Supply|Electricity|Power generation",
        "IDA|Emissions|CO2|Energy|Supply|Electricity|Conversion efficiency",
        "IDA|Emissions|CO2|Energy|Supply|Electricity|Renewables",
        "IDA|Emissions|CO2|Energy|Supply|Electricity|Nuclear",
        // "IDA|Emissions|CO2|Energy|Supply|Electricity|CO2 intensity",
        "IDA|Emissions|CO2|Energy|Supply|Electricity|CCS",
        "IDA|Emissions|CO2|Energy|Supply|Electricity|Emission end level 2050",
        "IDA|Emissions|CO2|Energy|Supply|Electricity|Power generation rel. to WWH",
    ],
    "Industry":[
        "IDA|Emissions|CO2|Energy|Demand|Industry|GDP",
        "IDA|Emissions|CO2|Energy|Demand|Industry|Energy efficiency",
        "IDA|Emissions|CO2|Energy|Demand|Industry|Renewables",
        "IDA|Emissions|CO2|Energy|Demand|Industry|Electrification",
        "IDA|Emissions|CO2|Energy|Demand|Industry|Heat",
        "IDA|Emissions|CO2|Energy|Demand|Industry|PtG/PtL",
        // "IDA|Emissions|CO2|Energy|Demand|Industry|CO2 intensity",
        "IDA|Emissions|CO2|Energy|Demand|Industry|CCS",
        "IDA|Emissions|CO2|Energy|Demand|Industry|Emission end level 2050",
        "IDA|Emissions|CO2|Energy|Demand|Industry|GDP rel. to WWH",
    ],
    "Buildings":[
        "IDA|Emissions|CO2|Energy|Demand|Buildings|Population",
        "IDA|Emissions|CO2|Energy|Demand|Buildings|Energy efficiency",
        "IDA|Emissions|CO2|Energy|Demand|Buildings|Renewables",
        "IDA|Emissions|CO2|Energy|Demand|Buildings|Electrification",
        "IDA|Emissions|CO2|Energy|Demand|Buildings|Heat",
        "IDA|Emissions|CO2|Energy|Demand|Buildings|PtG/PtL",
        // "IDA|Emissions|CO2|Energy|Demand|Buildings|CO2 intensity",
        "IDA|Emissions|CO2|Energy|Demand|Buildings|Emission end level 2050",
    ],
    "Transport":[
        "IDA|Emissions|CO2|Energy|Demand|Transport|Population",
        "IDA|Emissions|CO2|Energy|Demand|Transport|Energy efficiency",
        "IDA|Emissions|CO2|Energy|Demand|Transport|Renewables",
        "IDA|Emissions|CO2|Energy|Demand|Transport|Electrification",
        "IDA|Emissions|CO2|Energy|Demand|Transport|PtG/PtL",
        // "IDA|Emissions|CO2|Energy|Demand|Transport|CO2 intensity",
        "IDA|Emissions|CO2|Energy|Demand|Transport|Emission end level 2050",
    ]}


    $('select.levers_scenario_select').multipleSelect('destroy').multipleSelect(
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
                create_ida_levers_viz()
            },

        });
    
    $('select.levers_sector_select').multipleSelect('destroy').multipleSelect(
        {
            filter: true,
            showClear: false,
            animate: 'fade',
            maxHeightUnit: 'row',
            maxHeight: 8,
            dropWidth: 250,
            selectAll: false,
            placeholder: 'Please select a sector',
            onClick: function (data) {
                create_ida_levers_viz()
            },

        }); 

    create_ida_levers_viz()

    function create_ida_levers_viz() {
        var viz_type = 'show_stacked_clustered_column_chart';
        var intrfc = 'ida_pub';
        var viz_frame = $('#' + viz_id + '_viz_frame_div');
        viz_frame.show();
        token_retrieval();

        var scenarios = $('#levers_scenario_select').multipleSelect('getSelects')
        var sector = $('#levers_sector_select').multipleSelect('getSelects')[0]

        var variables = sector_var_mapping[sector]

        var y_var_scenarios = scenarios;
        var y_var_scenarios_titles = scenarios;
        var y_var_names = []
        var y_var_titles = []
        for (var i = 0; i < y_var_scenarios.length; i++) {
            for (var j = 0; j < variables.length; j++) {
                y_var_names.push(String(y_var_scenarios[i]) + '_' + variables[j]);
                y_var_titles.push(variables[j].split("|")[variables[j].split("|").length-1]);
            }
        }
        /* # Query creation*/
        var jq_obj = create_ida_levers_query(scenarios,variables);
        console.log(viz_id + '- JSON Query Created');
        var viz_payload = {
            "y_var_names": y_var_names,
            "y_var_titles": y_var_titles,
            "y_var_units": ['%'],
            "y_axis_title": 'Total emissions change',
            "x_axis_name": "model__title",
            "x_axis_title": "Model",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "cat_axis_names": scenarios,
            "cat_axis_titles": scenarios,
            "use_default_colors": false,
            "color_list_request": ["red", "gray", "casual_green", "yellow", "dark_gray",
                "blue", "light_brown","purple","orange","light_blue"],
            "dataset_type": "query",
            "type": "normal"
        };

        start_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)
    }

    function create_ida_levers_query(scenarios, variables) {
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
            "dataset": "i2amparis_main_idaresultscomp",
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

