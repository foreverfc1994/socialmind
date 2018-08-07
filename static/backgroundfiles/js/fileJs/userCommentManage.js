function ajaxUncheckedData(){
    $.ajax({
        url: '/usrCommentsSelect/commentsCheck/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            getUncheckedData(data.data);
        },
        error: function(data){
            alert("数据错误1");
        }
    });
}

function ajaxCommentsManageData(){
    $.ajax({
        url: '/usrCommentsSelect/commentsManage/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            getCommentsData(data.data);
        },
        error: function(data){
            alert("数据错误2");
        }
    });
}




function getUncheckedData(data){
    var item = 0;
    options = {
        "order": [0, "asc"],
        stateSave: true,
        "bAutoWidth": false,
        "aLengthMenu": [[15,50, 100], [15, 50, 100]],
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
            {"data": "serialNum", "title": "序号", "render": function(){
                item++;
                return item;
                }},
            {"data": "messageid", "title": "评论id"},
            {"data": null, "title": "留言内容", "width": "150px", "render": function tdContent(data){
                return "<p title='"+data.content+"' style='overflow: hidden; white-space: nowrap; text-overflow: ellipsis; height: 30px; width: 200px;'>"+data.content+"</p>"
                }},
            {"data": "time", "title": "留言时间"},
            {"data": "objectname", "title": "事件名称"},
            {"data": "objectid", "visible": false},
            {"data": null, "title": "操作", "width": "100px", "render": function botton(data){
                    return "<button class=\"btn btn-danger btn-xs\" onclick=\"passComment('"+data.messageid+"')\">通过</button>" +
                        "<button class=\"btn btn-danger btn-xs\" style='margin-left: 5px;' onclick=\"noPass('"+data.messageid+"')\">不通过</button>"
                },
            }
        ]
    };
    var table=$('#uncheckedTable').DataTable(options);
}

function getCommentsData(data){
    var item = 0;
    options = {
        "order": [0, "asc"],
        stateSave: true,
        "bAutoWidth": false,
        "aLengthMenu": [[15,50, 100], [15, 50, 100]],
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
            {"data": "serialNum", "title": "序号", "render": function(){
                item++;
                return item;
                }},
            {"data": "messageid", "title": "评论id"},
            {"data": null, "title": "留言内容", "width": "150px", "render": function tdContent(data){
                return "<p title='"+data.content+"' style='overflow: hidden; white-space: nowrap; text-overflow: ellipsis; height: 30px; width: 200px;'>"+data.content+"</p>"
                }},
            {"data": "time", "title": "留言时间"},
            {"data": "objectname", "title": "事件名称"},
            {"data": "objectid", "visible": false},
            {"data": null, "title": "操作", "width": "100px", "render": function botton(data){
                    return "<button class=\"btn btn-danger btn-xs\" onclick=\"deleteComment('"+data.messageid+"')\">删除</button>"
                },
            }
        ]
    };
    var table=$('#commentsManage').DataTable(options);
}

function passComment(messageid){
    con = confirm("确定通过该留言？");
    if(con==true){
        $.ajax({
            url: 'commentsManage/pass/?messageid='+messageid,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                if(data.data=="true"){
                    alert("操作成功！");
                    location.reload();
                }
                else{
                    alert("未知错误");
                }
            },
            error: function(){
                alert("删除失败，请稍后重试");
            }
        })
    }
}

function noPass(messageid){
    con = confirm("确定不予通过？");
    if(con==true){
        $.ajax({
            url: 'commentsManage/noPass/?messageid='+messageid,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                if(data.data=="true"){
                    alert("操作成功！");
                    location.reload();
                }
                else{
                    alert("未知错误");
                }
            },
            error: function(){
                alert("操作失败，请稍后重试");
            }
        })
    }
}

function deleteComment(messageid){
    conn = confirm("确定删除？");
    if(conn==true){
        $.ajax({
            url: 'commentsManage/deleteComment/?messageid='+messageid,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                if(data.data=="true"){
                    alert("操作成功！");
                    location.reload();
                }
                else{
                    alert("未知错误");
                }
            },
            error: function(){
                alert("操作失败，请稍后重试");
            }
        })
    }
}