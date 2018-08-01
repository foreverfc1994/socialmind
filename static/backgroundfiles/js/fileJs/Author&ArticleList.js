function getTableAuthorData(data){
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
                return "<a href='/toAuthorParticular/?id="+data.authorId+"'>详情</a>";
                }
            },
            {"data": null, "title": "操作", "width": "40px", "render": function botton(){
                    return "<button class=\"btn btn-danger btn-xs\"><i class=\"fa fa-trash-o \"></i></button>"
                },
            }
        ]
    };


    var table=$('#table_id_example').DataTable(options);
}

function getArticleListData(data){
    var item = 0;
    options = {
        "order": [0, "asc"],
        "bAutoWidth": false,
        "aLengthMenu": [[20,50,-1], [20, 50, "全部"]],
        "language": {
            "lengthMenu": "&nbsp;  &nbsp;  &nbsp;  每页_MENU_条记录",
            "zeroRecords": "没有找到记录",
            "info": "&nbsp;  &nbsp;  &nbsp;  第_PAGE_页(共_PAGES_页)",
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
            {"data": "id", "visible": false},
            {"data": "serialNum", "title": "序号", "width": "5%", "render": function(){
                item++;
                return item;
                }},
            {"data": "title", "title": "文章名称", "width": "40%"},
            {"data": "web", "title": "网站", "width": "8%"},
            {"data": "author", "title": "作者", "width": "8%"},
            {"data": "type", "title": "类型", "width": "8%"},
            {"data": "readed", "title": "阅读量", "width": "8%"},
            {"data": "heat", "title": "热度", "width": "5%"},
            {"data": null, "title": "详情", "width": "5%", "render": function aLink(data){
                return "<a href='/ArticlePaticular/?id="+data.id+"'>详情</a>";
                }
            },
            {"data": null, "title": "操作","width": "5%", "render": function botton(){
                    return "<button class=\"btn btn-danger btn-xs\"><i class=\"fa fa-trash-o \"></i></button>"
                },
            }
        ]
    };

    var table=$('#table_id_example').DataTable(options);
}

function getComments(datas){
    if(datas.length>0){
        html = "";
        for(i=0;i<datas.length;i++){
            data = datas[i];
            commentID = data.commentID;
            commenterID = data.commenterID;
            commenterName = data.commenterName;
            commentTime = data.commentTime;
            contentt = data.contentt;
            html += "<div class=\"comment-item\" id=\""+commentID+"\">\n" +
                "        <div class=\"pic\">\n" +
                "             <a href=\"#\"><img src=\"/static/backgroundfiles/img/details_close.png\" width=\"48\" height=\"48\" class=\"\" alt=\"\"></a>\n" +
                "        </div>\n" +
                "        <div class=\"content report-comment\">\n" +
                "            <div class=\"author\">\n" +
                "                <span class=\"\">"+commentTime+"</span>\n" +
                "                    <a href=\"#\" class=\"  \">"+commenterName+"</a> \n" +
                "            </div>\n" +
                "            <p class=\"\">"+contentt+"</p>\n" +
                "        </div>\n" +
                "    </div>\n"
        }
        $("#comments").append(html);
    }
}