function errorlog() {
    $.ajax({
            url: '/errorlog/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                var item = 0;
                datas = data.data;
                console.log(datas)
                options = {
                    "order": [0, "asc"],
                    "bAutoWidth": false,
                    "bProcessing": true,
                    "aLengthMenu": [[10, 30, -1], [20, 30, "全部"]],
                    "language": {
                        "lengthMenu": " 每页_MENU_条记录",
                        "zeroRecords": "没有找到记录",
                        "info": "第_PAGE_页(共_PAGES_页)",
                        "infoEmpty": "无记录",
                        "infoFiltered": "(从_MAX_条记录过滤)",
                        "oPaginate": {
                            "sFirst": "首页",
                            "sPrevious": "上页",
                            "sNext": "下页",
                            "sLast": "末页"
                        },
                        "sSearch": "搜索: ",
                        "sLoadingRecords": "正在加载数据-请等待...",
                    },
                    data: datas,
                    columns: [
                        {
                            data: null, "render": function () {
                                item++;
                                return item;
                            }
                        },
                        {data: 'spidername'},

                        {data: 'errortime'},
                        {data: 'errorinfo'},

                    ]
                };

                var table = $('#table_id_example').DataTable(options);

            },
            error: function (data) {
                alert("数据获取失败");
            }
        });
}
function spiderlog() {
    $.ajax({
            url: '/spiderlog/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                var item = 0;
                datas = data.data;
                console.log(datas)
                options = {
                    "order": [0, "asc"],
                    "bAutoWidth": false,
                    "bProcessing": true,
                    "aLengthMenu": [[10, 30, -1], [20, 30, "全部"]],
                    "language": {
                        "lengthMenu": " 每页_MENU_条记录",
                        "zeroRecords": "没有找到记录",
                        "info": "第_PAGE_页(共_PAGES_页)",
                        "infoEmpty": "无记录",
                        "infoFiltered": "(从_MAX_条记录过滤)",
                        "oPaginate": {
                            "sFirst": "首页",
                            "sPrevious": "上页",
                            "sNext": "下页",
                            "sLast": "末页"
                        },
                        "sSearch": "搜索: ",
                        "sLoadingRecords": "正在加载数据-请等待...",
                    },
                    data: datas,
                    columns: [
                        {
                            data: null, "render": function () {
                                item++;
                                return item;
                            }
                        },
                        {data: 'user'},

                        {data: 'role'},
                        {data: 'time'},
                        {data: 'funname'},
                        {data: 'fun'},
                        {data: 'para'},

                    ]
                };

                var table = $('#tablespider').DataTable(options);

            },
            error: function (data) {
                alert("数据获取失败");
            }
        });
}