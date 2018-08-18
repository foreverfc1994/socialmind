function pickType(num, keyword){
    var tds = document.getElementById("typeSelect").getElementsByTagName("td");
    tds[num].className = "active";
    for(i=0; i<14; i++){
        if(i !== num){
            td = tds[i];
            $(td).removeClass();
        }
    }
    eventList(0, keyword);
}

function eventSearch(){
    var searchKeyword = $("#fileSearchInput").val();
    eventList(0, searchKeyword);
}

function eventList(page, keyword){
    $.ajax({
        url: 'getEventList/?page='+page.toString()+"&keyword="+keyword,
        type:'GET',
        dataType: 'json',
        success: function(data){
            if(keyword==undefined){
                keyword="";
            }
            eventLoad(data.data, page, keyword);
        }
    })
}

function eventLoad(dataList, page, keyword){
    html = "";
    for(i=0; i<dataList.length; i++){
        data = dataList[i];
        html += "<a href=\"/eventParticular/?objectid="+data.objectid+"\" class=\"list-group-item\">\n" +
            "                                    <div class=\"row\">\n" +
            "                                        <div class=\"col-lg-7\">\n" +
            "                                            <h3 class=\"list-group-item-heading\">"+data.title+"</h3>\n" +
            "\n" +
            "                                        </div>\n" +
            "                                        <div class=\"col-lg-5\">\n" +
            "                                            <table>\n" +
            "                                                <tr>\n" +
            "                                                    <td style=\"width: 30%;\">时间："+data.starttime+"</td>\n" +
            "                                                    <td style=\"width: 20%;\">热度："+data.heatIndex+"</td>\n" +
            "                                                    <td style=\"width: 20%;\">点赞："+data.likeNum+"</td>\n" +
            "                                                    <td style=\"width: 20%;\">收藏："+data.collectNum+"</td>\n" +
            "                                                    <td style=\"width: 20%;\">评论："+data.commentNum+"</td>\n" +
            "                                                </tr>\n" +
            "                                            </table>\n" +
            "                                        </div>\n" +
            "                                    </div>\n" +
            "                                    <p class=\"list-group-item-text\">\n" +
            "                                        "+data.introduction+"。\n" +
            "                                    </p>\n" +
            "                                </a>"
    };
    if(dataList.length == 20){
        html+="<a onclick=\"eventList("+(page+1).toString()+",'"+keyword+"')\" class=\"list-group-item\" id='moreItems' style='cursor: pointer;'>\n" +
        "       <p class=\"list-group-item-text\">\n" +
        "             点击加载更多。\n" +
        "       </p>\n" +
        "  </a>"
    }
    if(dataList.length == 0){
        html = "<a href=\"/eventParticular/?objectid="+data.objectid+"\" class=\"list-group-item\">\n" +
            "                                    <div class=\"row\">\n" +
            "                                        <div class=\"col-lg-7\">\n" +
            "                                            <h3 class=\"list-group-item-heading\" style='text: center'>无更多内容</h3>\n" +
            "\n" +
            "                                        </div>\n" +
            "                                    </div>\n" +
            "                                    <p class=\"list-group-item-text\">\n" +
            "                                        请搜索其他内容\n" +
            "                                    </p>\n" +
            "                                </a>"
    }
    if(page == 0){
        $("#results").children().remove();
        $("#results").append(html);
    }
    else{
        $("#moreItems").replaceWith(html);
    }
}