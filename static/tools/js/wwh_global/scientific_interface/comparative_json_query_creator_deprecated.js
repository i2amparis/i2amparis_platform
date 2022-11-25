function create_query_json_column() {
    var sel_model = $('#model_name_intro_comp');
    var sel_scenario = $('#scenario_name_intro_comp');
    var sel_variable = $('#variable_name_intro_comp');

    const models = new Array(1);
    models[0] = sel_model.val();

    const scenarios = sel_scenario.val();

    const variables = new Array(1);
    variables[0] = sel_variable.val();


    var aggfunc = $('#agg_func_intro_comp');
	// var aggvar = $('#agg_var_intro_comp');
    var aggvar = $('input[name="agg_var_input"]:checked');

	const aggfuncval = new Array(1);
	aggfuncval[0] = aggfunc.val();

	const aggvarval =  new Array(1);
	aggvarval[0] = aggvar.val();


	const aggvartitle = new Array(1);
	aggvartitle[0] = aggvar.parent().text().trim();

    var multiple_field = "scenario";
    var val_list = scenarios;
    var title_list = sel_scenario.multipleSelect('getSelects', 'text');


    //ordering
    var ordering;
    if (aggvarval[0]==='year'){
        ordering = 'year'
    }else if(aggvarval[0]==='region_id'){
        ordering='region__reg_type'
    }

    if(val_list.length===0){
        val_list = []
    }

    const input_dict = {'model__name': models, 'scenario__name': scenarios, 'variable__name': variables};
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
        if (temp.length > 1) {
            for (var x in temp) {
                or_dict.push({
                    'operand_1': selected[j],
                    'operand_2': temp[x],
                    'operation': '='
                });
            }
        } else {
            and_dict.push({
                'operand_1': selected[j],
                'operand_2': input_dict[selected[j]][0],
                'operation': '='
            });
        }
    }
    if (aggvarval[0]==='year'){
        and_dict.push({
            'operand_1': 'region__name',
            'operand_2': ['World'],
            'operation': 'in'

        });

    }
    // and_dict.push({
    //     'operand_1': 'region__name',
    //     'operand_2': ['MEX', 'BLR', 'KOR', 'IND', 'HRV', 'LBY', 'CAN', 'SVN', 'LUX', 'GBR', 'THA', 'BGR', 'ECU', 'ETH', 'NOR', 'ESP', 'PAK', 'RUS', 'PER', 'JPN', 'MEA', 'CHE', 'EST', 'BEL', 'IRQ', 'KWT', 'AZE', 'SWE', 'SAU', 'TUR', 'COL', 'AUT', 'UGA', 'FRA', 'AGO', 'CHN', 'GHA', 'GRC', 'ITA', 'DZA', 'PRT', 'QAT', 'HUN', 'MKD', 'USA', 'KEN', 'NGA', 'ARG', 'MOZ', 'LVA', 'VEN', 'BOL', 'CHL', 'UKR', 'NLD', 'GAB', 'ZAF', 'KAZ', 'IRN', 'ARE', 'NZL', 'DEU', 'UZB', 'TKM', 'BRA', 'LTU', 'FIN', 'DNK', 'POL', 'SVK', 'BGD', 'EGY', 'MLT', 'VNM', 'IRL', 'CZE', 'CYP', 'AUS', 'TWN', 'ROU', 'MYS', 'ISL', 'IDN'],
    //     'operation': 'in'
    //
    // });
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
                    "parameter": ordering,
                    "ascending": true
                },

            ]
            ,
            "grouping": {"params":[aggvarval[0], "model__name", "scenario__name", "variable__name"], "aggregated_params":[{"name":"value","agg_func": aggfuncval[0]}]},
        },
        "additional_app_parameters": {
            "multiple_field": multiple_field,
            "val_list": val_list,
            "title_list": title_list,
            "grouping_var": aggvarval[0],
            "grouping_var_title": aggvartitle[0]
        }

    };

    return {
        "models": models,
        "scenarios": scenarios,
        "variables": variables,
        "multiple_field": multiple_field,
        "query_data": query_data
    }

}


function retrieve_series_info_column(model_sel, scenario_sel, variable_sel, agg_var, agg_func_sel, jq_obj){
    const units_info = {
        "model_name": jq_obj["models"],
        "scenario_name": jq_obj["scenarios"],
        "variable_name": jq_obj["variables"],
        "multiple": jq_obj["multiple_field"]
    };

    var instances = [];
    var final_val_list = [];
    var final_title_list = [];
    var final_unit_list = [];
    $.ajax({
        url: "/data_manager/retrieve_series_info",
        type: "POST",
        data: JSON.stringify(units_info),
        contentType: 'application/json',
        success: function (data) {

            instances = data["instances"];
            for (var i = 0; i < instances.length; i++) {
                final_val_list.push(instances[i]['series']);
                final_title_list.push(instances[i]['title']);
                final_unit_list.push(instances[i]['unit']);
            }

            var grouping_val;
            var grouping_var_title;
            if ('grouping_var' in jq_obj['query_data']['additional_app_parameters']) {
                grouping_val = jq_obj['query_data']['additional_app_parameters']['grouping_var']//the variable that is used for the column grouping
                grouping_var_title = jq_obj['query_data']['additional_app_parameters']['grouping_var_title']//the title of the variable that is used for the column grouping
            } else {
                grouping_val = ''
            }

            var json_object = {
                "data": jq_obj['query_data'],
                "multiple_field": jq_obj["multiple_field"],
                "val_list": final_val_list,
                "title_list": final_title_list,
                "unit_list": final_unit_list,
                "grouping_var": grouping_val,
                "grouping_var_title": grouping_var_title
            };

            start_qc_v_column_process(model_sel, scenario_sel, variable_sel, agg_var, agg_func_sel, json_object);

        },
        error: function (data) {
            console.log(data);
        }
    });


}



