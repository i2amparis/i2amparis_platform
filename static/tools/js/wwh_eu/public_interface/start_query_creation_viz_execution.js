function start_query_creation_viz_execution(json_query_obj, viz_id, viz_payload, viz_type, intrfc) {
        var query = {};
        query["query_name"] = intrfc + "_" + viz_id + "_query";
        query["parameters"] = json_query_obj['query_data'];
        $.ajax({
            url: "/data_manager/create_query",
            type: "POST",
            data: JSON.stringify(query),
            contentType: 'application/json',
            success: function (data) {
                console.log(viz_id + '- Query Saved in DB');
                var query_id = data['query_id'];
                create_visualisation(query_id, viz_id, viz_payload, viz_type)
            },
            error: function (data) {
                console.log(data);
            }
        });
    }
