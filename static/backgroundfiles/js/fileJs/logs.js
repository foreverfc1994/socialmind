function getSystemLogData(data){
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
            {"data": "userid", "visible": false},
            {"data": "role", "title": "角色"},
            {"data": "username", "title": "用户名"},
            {"data": "logtime", "title": "操作时间"},
            {"data": "logfunName", "title": "方法名"},
            {"data": "logfunLname", "title": "方法逻辑名"},
            {"data": "askurl", "title": "请求路径"},
        ]
    };


    var table=$('#syslog').DataTable(options);
}
