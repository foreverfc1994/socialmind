function personUserIndex(){
    $.ajax({
        url: 'List/person/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            personUserTable(data.data)
        },
        error: function(){alert("未知错误，请重试！");}
    })
}
function personUserTable(data){
    options = {
        "order": [0, "asc"],
        stateSave: true,
        "bAutoWidth": false,
        "aLengthMenu": [[15,50, 100], [15, 50, 100]],
        "language": {
            "lengthMenu": "&nbsp; &nbsp; &nbsp;每页_MENU_条记录",
            "zeroRecords": "没有找到记录",
            "info": "&nbsp; &nbsp; &nbsp;第_PAGE_页(共_PAGES_页)",
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
            {"data": "userid", "title": "用户id"},
            {"data": "username", "title": "用户名"},
            {"data": "realname", "title": "真实姓名"},
            {"data": "sex", "title": "性别"},
            {"data": "age", "title": "年龄"},
            {"data": "phoneNum", "title": "手机号码"},
            {"data": "email", "title": "邮箱"},
            {"data": "job", "title": "工作"},
            {"data": "registrantTime", "title": "注册日期"},
            {"data": null, "title": "操作", "width": "40px", "render": function botton(data){
                    return "<button class=\"btn btn-danger btn-xs\" onclick=\"deleteUser('"+data.userid+"')\">删除</button>"
                },
            }
        ]
    };
    var table=$('#personUser').DataTable(options);
}

function companyUserIndex(){
    $.ajax({
        url: 'List/company/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            companyUserTable(data.data)
        },
        error: function(){alert("未知错误，请重试");}
    })
}
function companyUserTable(data){
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
            {"data": "userid", "title": "用户id"},
            {"data": "username", "title": "用户名"},
            {"data": "companyname", "title": "公司名称"},
            {"data": "companytype", "title": "公司类别"},
            {"data": "registertime", "title": "公司注册日期"},
            {"data": "email", "title": "邮箱"},
            {"data": "registrantTime", "title": "账号注册日期"},
            {"data": null, "title": "操作", "width": "40px", "render": function botton(data){
                    return "<button class=\"btn btn-danger btn-xs\" onclick=\"deleteUser('"+data.userid+"')\">删除</button>"
                },
            }
        ]
    };
    var table=$('#comUser').DataTable(options);
}

function govermentUserIndex(){
    $.ajax({
        url: 'List/goverment/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            govermentUserTable(data.data)
        },
        error: function(){alert("未知错误");}
    })
}
function govermentUserTable(data){
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
            {"data": "userid", "title": "用户id"},
            {"data": "username", "title": "用户名"},
            {"data": "govname", "title": "政府机构名称"},
            {"data": "govcode", "title": "机构代码"},
            {"data": "govType", "title": "政府机构类型"},
            {"data": "email", "title": "邮箱"},
            {"data": "registrantTime", "title": "账号注册日期"},
            {"data": null, "title": "操作", "width": "40px", "render": function botton(data){
                    return "<button class=\"btn btn-danger btn-xs\" onclick=\"deleteUser('"+data.userid+"')\">删除</button>"
                },
            }
        ]
    };
    var table=$('#govUser').DataTable(options);
}

function instituteUserIndex(){
    $.ajax({
        url: 'List/institute/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            instituteUserTable(data.data)
        },
        error: function(){alert("未知错误");}
    })
}
function instituteUserTable(data){
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
            {"data": "userid", "title": "用户id"},
            {"data": "username", "title": "用户名"},
            {"data": "institutionname", "title": "机构名称"},
            {"data": "institudecode", "title": "机构代码"},
            {"data": "institutionlevel", "title": "机构级别"},
            {"data": "institutiontype", "title": "机构类型"},
            {"data": "email", "title": "邮箱"},
            {"data": "registrantTime", "title": "账号注册日期"},
            {"data": null, "title": "操作", "width": "40px", "render": function botton(data){
                    return "<button class=\"btn btn-danger btn-xs\" onclick=\"deleteUser('"+data.userid+"')\">删除</button>"
                },
            }
        ]
    };
    var table=$('#institutionUser').DataTable(options);
}

function deleteUser(userid){
    con = confirm("确定删除该用户？");
    if(con==true){
        $.ajax({
            url: 'deleteUser/?userid='+userid,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                if(data.data=='success'){
                    alert("删除成功!");
                    location.reload();
                }
                else{
                    alert("删除失败");
                }
            },
            error: function(data){
                alert("删除失败，请稍后重试");
            }
        })
    }
}