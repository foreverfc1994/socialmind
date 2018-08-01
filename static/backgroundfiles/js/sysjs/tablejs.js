function getTableLogData(data) {
    var item = 0;
    options = {
        "order": [0, "asc"],
        "bAutoWidth": false,
        "aLengthMenu": [[10,30,-1], [20, 30, "全部"]],
        "language": {
            "lengthMenu": " 每页_MENU_条记录",
            "zeroRecords": "没有找到记录",
            "info": "第_PAGE_页(共_PAGES_页)",
            "infoEmpty": "无记录",
            "infoFiltered": "(从_MAX_条记录过滤)",
            "oPaginate":{
                "sFirst": "首页",
                "sPrevious": "上页",
                "sNext": "下页",
                "sLast": "末页"
            },
            "sSearch": "搜索: ",
            "sLoadingRecords": "正在加载数据-请等待...",
        },
        "data": data,
        "columns": [
            {"data": "authorId", "visible": false},
            {"data": "serialNum", "title": "序号", "render": function(){
                item++;
                return item;
                }},
            {"data": "name", "title": "作者昵称"},
            {"data": "web", "title": "网站"},
            {"data": "filesNumber", "title": "文章数"},
            {"data": "fansNumber", "title": "粉丝数"},
            {"data": null, "title": "详情", "render": function aLink(data){
                return "<a href='toAuthorParticular/?id="+data.authorId+"/'>详情</a>"
                }
            },
            {"data": null, "title": "操作", "width": "60px", "render": function botton(){
                return "<button class=\"btn btn-success btn-xs\"><i class=\"fa fa-check\"></i></button>\n" +
                    "<button class=\"btn btn-primary btn-xs\"><i class=\"fa fa-pencil\"></i></button>\n"+
                    "<button class=\"btn btn-danger btn-xs\"><i class=\"fa fa-trash-o \"></i></button>"
                },
            }
        ]
    };
}