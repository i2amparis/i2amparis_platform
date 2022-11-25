function populate_comparative_datatables(model_sel, scenario_sel, variable_sel, agg_var, agg_func) {
    $('#comparative_tables').DataTable().destroy();
    const models = model_sel.multipleSelect('getSelects');
    const scenarios = scenario_sel.multipleSelect('getSelects');
    const variables = variable_sel.multipleSelect('getSelects');
    const agg_func_val = agg_func.multipleSelect('getSelects')[0];

    const d = {'model__name': models, 'scenario__name': scenarios, 'variable__name': variables,'agg_var': agg_var.val(), 'agg_func': agg_func_val};
    $.ajax({
            url: "/populate_comparative_analysis_datatables",
            type: "POST",
            data: JSON.stringify(d),
            contentType: 'application/json',
            success: function (data) {
                console.log(data);

                $('#comparative_tables').DataTable({
                    "data": data['final_data'],
                    columns: [
                        {"data": "model__title"},
                        {"data": "scenario__title"},
                        {"data": "variable__title"},
                        {"data": "value"},
                        {"data": "unit"},
                        {"data": data['agg_var']},
                    ]
                });
            },
            error: function (data) {
                console.log(data);
            }
        });
   }