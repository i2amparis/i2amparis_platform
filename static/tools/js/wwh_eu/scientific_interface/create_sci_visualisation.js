function create_sci_visualisation(query_id, viz_id, data, viz_type) {
    var viz_frame = $('#' + viz_id + '_viz_iframe');
    viz_frame.off();
    viz_frame.hide();
    $('#' + viz_id + '_loading_bar').show();

    var url = '';
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            if (Array.isArray(data[key])) {
                for (var j = 0; j < data[key].length; j++) {
                    url = url + String(key) + '[]' + "=" + String(data[key][j]) + '&'
                }
            } else {
                url = url + String(key) + "=" + String(data[key]) + '&'
            }

        }
    }
    url = url + "dataset=" + query_id
    console.log(viz_id + '- Ready to launch visualisation');
    var complete_url = "/visualiser/" + viz_type + "?" + url;
    viz_frame.attr('src', complete_url);
    viz_frame.on('load', function () {
        console.log(viz_id + '- Visualisation Completed');
        $(this).show();
        $.ajax({
            headers: { "X-CSRFToken": token },
            url: "/data_manager/delete_query",
            type: "POST",
            data: JSON.stringify(query_id),
            contentType: 'application/json',
            success: function (data) {
                console.log(viz_id + "- Query Deleted");
                document_ready_counter = document_ready_counter + 1;
                console.log('Counting Viz: ' + String(document_ready_counter));
                check_document_ready(document_ready_counter);
            },
            error: function (data) {
                console.log(data);
            }
        });

        $('#' + viz_id + '_loading_bar').hide();

    });

}
