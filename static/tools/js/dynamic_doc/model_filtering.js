$('#mod_filtering_select').multipleSelect(
        {
            filter: true,
            showClear: false,
            animate: 'fade',
            maxHeightUnit: 'row',
            maxHeight: 8,
            dropWidth: 250,
            selectAll: false,
            placeholder: 'Please select a project',
            onClick: function () {
                var project = $('#mod_filtering_select').multipleSelect('getSelects')[0];
                console.log(project)
                $('.model-list div.model-obj').each(function (){
                    if ($(this).data('project').indexOf(project) ===-1){
                        $(this).hide()
                    }
                    else{
                        $(this).show()
                    }
                });
            },

        });