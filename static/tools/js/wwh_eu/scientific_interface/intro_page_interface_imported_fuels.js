$(document).ready(function () {

    $("#imported_fuels-clear-button").click(function () {
        $('#imported_fuels select.sum-boot-select').multipleSelect('setSelects', []);
        $('#imported_fuels_viz_frame_div').hide();
    });

    $("#imported_fuels-run-button").click(function () {
        var intrfc = 'eu_wwh_scientific';
        var dataset = 'i2amparis_main_wwheuresultscomp';
        var model_sel = $('#imported_fuels_model_name');
        var model_full = (model_sel.multipleSelect('getSelects').length === 0);
        if (model_full) {
            alert('Please, select at least one value from each field to update the visualisation.')
        } else {
            //Coal Visualisation
            var viz_id = 'imported_fuels_coal';
            var viz_type = 'show_line_chart';
            var viz_frame = $('#' + viz_id + '_viz_frame_div');
            viz_frame.show();
            var jq_obj = create_imported_fuels_coal_query(dataset,'Trade|Primary Energy|Coal|Volume');
            console.log(viz_id + ' - JSON Query Created');
            retrieve_series_info_summary(jq_obj, dataset, viz_id, viz_type, intrfc, false, [], [], [], String(jq_obj["variables"]));

            //Coal Visualisation
            viz_id = 'imported_fuels_gas';
            viz_type = 'show_line_chart';
            viz_frame = $('#' + viz_id + '_viz_frame_div');
            viz_frame.show();
            jq_obj = create_imported_fuels_coal_query(dataset,'Trade|Primary Energy|Gas|Volume');
            console.log(viz_id + ' - JSON Query Created');
            retrieve_series_info_summary(jq_obj, dataset, viz_id, viz_type, intrfc, false, [], [], [], String(jq_obj["variables"]));

              //Oil Visualisation
            viz_id = 'imported_fuels_oil';
            viz_type = 'show_line_chart';
            viz_frame = $('#' + viz_id + '_viz_frame_div');
            viz_frame.show();
            jq_obj = create_imported_fuels_coal_query(dataset,'Trade|Primary Energy|Oil|Volume');
            console.log(viz_id + ' - JSON Query Created');
            retrieve_series_info_summary(jq_obj, dataset, viz_id, viz_type, intrfc, false, [], [], [], String(jq_obj["variables"]));


        }
    });


    function create_imported_fuels_coal_query(dataset, variable_name) {
        var sel_model = $('#imported_fuels_model_name');
        var variable = [variable_name];
        const models = sel_model.multipleSelect('getSelects');
        const scenarios = ['EUWWH'];
        const regions = ['EU']

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
            "dataset": dataset,
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


    $("#imported_fuels-run-button").trigger('click');
});

