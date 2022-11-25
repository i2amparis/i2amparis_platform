function populate_datatables() {
    $('#example').DataTable().destroy();

    $.ajax({
        url: "/populate_rrf_policy_datatables",
        type: "POST",
        data: JSON.stringify({}),
        contentType: 'application/json',
        success: function (data) {
            console.log(data);

            $('#example').DataTable({
                "pageLength": 30,
                "data": data,
                columns: [
                    {"data": "title"},
                    {"data": "description"},
                    {"data": "country"},
                    {"data": "budget"},
                    {"data": "total_ratio"},
                    {"data": "first_classification"},
                    {"data": "second_classification"}
                ],
                dom: 'Bfrtip',
                buttons: ['csvHtml5'],
                columnDefs: [
                    {"width": "24%", "targets":0},
                    {"width": "35%", "targets":1},
                    {"width": "7%", "targets":2},
                    {"width": "7%", "targets":3},
                    {"width": "7%", "targets":4},
                    {"width": "10%", "targets":5},
                    {"width": "10%", "targets":6}]
            });
            $(".buttons-csv span").text("Export to CSV");
        },
        error: function (data) {
            console.log(data);
        }
    });
}

populate_datatables()