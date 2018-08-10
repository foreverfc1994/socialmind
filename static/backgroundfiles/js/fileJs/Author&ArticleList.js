function getTableAuthorData(data){
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
                return "<a href='/ArticlesOfAuthor/?id="+data.authorId+"'>详情</a>";
                }
            },
            {"data": null, "title": "操作", "width": "40px", "render": function botton(data){
                    return "<button class=\"btn btn-danger btn-xs\" onclick='deleteAuthor(\""+data.authorId+"\")'><i class=\"fa fa-trash-o \"></i></button>"
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
        "bProcessing":true,
        stateSave: true,
        "aLengthMenu": [[15,50,-1], [15, 50, "全部"]],
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
            {"data": null, "title": "操作","width": "5%", "render": function botton(data){
                    return "<button class=\"btn btn-danger btn-xs\" onclick='deleteArticle(\""+data.id+"\")'><i class=\"fa fa-trash-o \"></i></button>"
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

function getAuthor_ArticleList(datas){
    if(datas.length>0){
        html = "";
        for(i=0; i<datas.length; i++){
            data = datas[i];
            articleID = data.articleID;
            author = data.name;
            posttime = data.posttime;
            title = data.title;
            content = data.content;
            scannumber = data.scanNum;
            commentnumber = data.commentNum;
            collectnumber = data.collectNum;
            html += "\n" +
                "                    <div class=\"row\" style=\"padding-top: 20px;padding-bottom: 20px\">\n" +
                "                            <div class=\"col-md-12\">\n" +
                "                            <div class=\"row\">\n" +
                "                                <div class=\"col-md-4\" style=\"padding-left: 0px\">\n" +
                "                                    <img style=\"display: inline-block\" class=\"xiaoimg\" src='/static/backgroundfiles/assets/img/ui-zac.jpg' alt=\"\">\n" +
                "                                    <a style=\"font-size: 12px;color: #333;margin-left: 12px;line-height: 30px;\" href='/ArticlePaticular/?id="+articleID+"'>"+author+"</a>\n" +
                "                                    <a style=\"font-size: 12px;color: #969696;margin-left: 8px;line-height: 30px;cursor: default;\" href='/ArticlePaticular/?id="+articleID+"'>\n" +
                "                                        发布于："+posttime+"\n" +
                "                                    </a>\n" +
                "                                </div>\n" +
                "                            </div>\n" +
                "                            <div class=\"row\">\n" +
                "                                <a href='/ArticlePaticular/?id="+articleID+"' class=\"tit\">"+title+"</a>\n" +
                "                                <a class=\"con\" href='/ArticlePaticular/?id="+articleID+"'>\n" +
                                                    content+
                "                                </a>\n" +
                "                            </div>\n" +
                "                            <div class=\"row bot\" style=\"margin-top: 20px\">\n" +
                "                                <p class=\"read fl\" style=\"display: inline-block\">阅读&nbsp;"+scannumber+"</p>\n" +
                "                                <p class=\"comment fl\" style=\"display: inline-block\">评论&nbsp;"+commentnumber+"</p>\n" +
                "                                <p class=\"collect fl\" style=\"display: inline-block\">收藏&nbsp;"+collectnumber+"</p>\n" +
                "                            </div>\n" +
                "                        </div>\n" +
                "                    </div>\n" +
                "                    <hr style=\"margin: 0px;height:2px;border: 0px;background-color: #ddd\">"
        };
        $("#authorFiles").append(html);
    }
}

function deleteAuthor(id){
    ensure = confirm("确定删除该作者（该作者文章也会被删除）？");
    if(ensure==true){
        $.ajax({
            url:'authorDelete/?id='+id,
            type:'GET',
            dataType:'json',
            success: function(data){
                if(data.data=="succeed"){
                    alert("删除成功");
                }
                else{
                    alert("删除失败，请重试");
                }
            },
            error: function(){
                alert("网络错误，请重试");
            },
        })
    }
}

function deleteArticle(id){
ensure = confirm("确定删除该文章？");
    if(ensure==true){
        $.ajax({
            url:'deleteArticle/?id='+id,
            type:'GET',
            dataType:'json',
            success: function(data){
                if(data.data=="succeed"){
                    alert("删除成功");
                }
                else{
                    alert("删除失败，请重试");
                }
            },
            error: function(){
                alert("网络错误，请重试");
            },
        })
    }
}