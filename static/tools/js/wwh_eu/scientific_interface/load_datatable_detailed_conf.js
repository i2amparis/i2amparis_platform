function populate_datatables(model_sel, scenario_sel, region_sel, variable_sel) {
    $('#example').DataTable().destroy();
    const models = model_sel.multipleSelect('getSelects');
    const scenarios = scenario_sel.multipleSelect('getSelects');
    const regions = region_sel.multipleSelect('getSelects');
    const variables = variable_sel.multipleSelect('getSelects');

    const d = {'model__name': models, 'scenario__name': scenarios, 'region__name': regions, 'variable__name': variables,
    'interface':'pr_eu'};
    $.ajax({
            url: "/populate_detailed_analysis_datatables",
            type: "POST",
            data: JSON.stringify(d),
            contentType: 'application/json',
            success: function (data) {
                console.log(data);

                $('#example').DataTable({
                    "data": data,
                    columns: [
                        {"data": "year"},
                        {"data": "value"},
                        {"data": "region"},
                        {"data": "scenario"},
                        {"data": "unit"},
                        {"data": "variable"},
                        {"data": "model"}
                    ],
                    dom: 'Bfrtip',
                    buttons: ['csvHtml5']
                });
                $(".buttons-csv span").text("Export to CSV");
            },
            error: function (data) {
                console.log(data);
            }
        });
   }