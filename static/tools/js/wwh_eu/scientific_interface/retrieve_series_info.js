function retrieve_series_info_summary(jq_obj, dataset, viz_id, viz_type, intrfc, default_colors, line_names, line_titles, line_units, y_axis_title) {
    const units_info = {
        "model_name": jq_obj["models"],
        "region_name": jq_obj["regions"],
        "scenario_name": jq_obj["scenarios"],
        "variable_name": jq_obj["variables"],
        "dataset": dataset
    };
    var instances = [];
    var final_val_list = [];
    var final_title_list = [];
    var final_unit_list = [];
    var final_color_list = [];
    var final_line_type_list = [];
        
    console.log(units_info)
    $.ajax({
        headers: { "X-CSRFToken": token },
        url: "/data_manager/retrieve_series_model_scenario",
        type: "POST",
        data: JSON.stringify(units_info),
        contentType: 'application/json',
        success: function (data) {
            console.log(viz_id + ' - Info Retrieved');
            instances = data["instances"];
            for (var i = 0; i < instances.length; i++) {
                final_val_list.push(instances[i]['series']);
                final_title_list.push(instances[i]['title']);
                final_unit_list.push(instances[i]['unit']);
                final_color_list.push(instances[i]['color']);
                final_line_type_list.push(instances[i]['line_type'])
            }

            var viz_payload = {
                "y_var_names": final_val_list,
                "y_var_titles": final_title_list,
                "y_var_units": final_unit_list.concat(line_units),
                "y_axis_title": y_axis_title,
                "x_axis_name": "year",
                "x_axis_title": "Year",
                "x_axis_unit": "-",
                "x_axis_type": "text",
                "line_names": line_names,
                "line_titles": line_titles,
                "use_default_colors": default_colors,
                "color_list_request": final_color_list,
                "line_type_list": final_line_type_list,
                "dataset_type": "query"
            };
            start_sci_query_creation_viz_execution(jq_obj, viz_id, viz_payload, viz_type, intrfc)

        },
        error: function (data) {
            console.log(data);
        }
    });

}