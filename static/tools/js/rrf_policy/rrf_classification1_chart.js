$(document).ready(function () {

    function run_rrf_classification1() {
        /* Token Retrieval*/
        const csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        });
        /* # Query creation*/
        var jq_obj = create_rrf_classification1_query();
        console.log(jq_obj);
        console.log('RRF Classification 1 JSON Query Created');
        start_qc_v_rrf_classification_1_process(jq_obj);


    };

    function start_qc_v_rrf_classification_1_process(json_query_obj) {
        var query = {};
        query["query_name"] = "rrf_classification_1_query";
        query["parameters"] = json_query_obj['query_data'];
        $.ajax({
            url: "/data_manager/create_query",
            type: "POST",
            data: JSON.stringify(query),
            contentType: 'application/json',
            success: function (data) {
                console.log('RRF Policy Classification 1 Query Saved in DB');
                var query_id = data['query_id'];
                create_visualisation_rrf_classification_1(query_id);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }


    function create_visualisation_rrf_classification_1(query_id) {
        var viz_frame = $('#classification_1_viz_iframe');
        viz_frame.off();
        viz_frame.hide();
        $('#classification_1_loading_bar').show();

        var data = {
            "y_var_names": ['Green', 'Digital', 'Other'],
            "y_var_titles": ['Green', 'Digital', 'Other'],
            "y_var_units": ['millions €'],
            "y_axis_title": 'Overall national resource allocation',
            "x_axis_name": "country",
            "x_axis_title": "Country",
            "x_axis_unit": "-",
            "x_axis_type": "text",
            "min_max_y_value": [0,100],
            "use_default_colors": false,
            "color_list_request": ["casual_green", "light_blue", "gold"],
            "dataset": query_id,
            "dataset_type": "query"
        };
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
        console.log('RRF Classification 1 Ready to launch visualisation');
        var complete_url = "/visualiser/show_stacked_column_chart?" + url;
        viz_frame.attr('src', complete_url);
        viz_frame.on('load', function () {
            console.log('RRF Classification 1 Visualisation Completed');
            $(this).show();
            $.ajax({
                url: "/data_manager/delete_query",
                type: "POST",
                data: JSON.stringify(query_id),
                contentType: 'application/json',
                success: function (data) {
                    console.log("RRF Classification 1 Temporary Query Deleted");
                },
                error: function (data) {
                    console.log(data);
                }
            });

            $('#classification_1_loading_bar').hide();

        });

    }

    function create_rrf_classification1_query() {
        var agg_func = 'Sum';
        var agg_var = 'first_classification';

        var selected = [];
        var and_dict = [];
        var or_dict = [];

        selected.push('first_classification', 'budget', 'total_ratio', 'country');
        const query_data = {
            "dataset": "i2amparis_main_rrfpolicy",
            "query_configuration": {
                "select": selected,
                "filter": {
                    "and": and_dict,
                    "or": or_dict
                },
                "ordering": [
                    {
                        "parameter": "country",
                        "ascending": true
                    },

                ]
                ,
                "grouping": {
                    "params": [agg_var, "country"],
                    "aggregated_params": [
                        {"name": "budget", "agg_func": agg_func},
                        {"name": "total_ratio", "agg_func": agg_func}
                    ]
                },

            },
            "additional_app_parameters": {"total_unit": "€ millions"}

        };

        return {
            "query_data": query_data
        }

    }

    run_rrf_classification1();


});

