function pickType(num, keyword){
    var tds = document.getElementById("typeSelect").getElementsByTagName("td");
    tds[num].className = "active";
    for(i=0; i<14; i++){
        if(i != num){
            td = tds[i];
            $(td).removeClass();
        }
    }
    getFiles("", 0, keyword);
}
function articleSearch(){
    var searchKeyword = $("#fileSearchInput").val();
    getFiles("", 0, searchKeyword);
}
function getFiles(objectid, page, keyword){
    $.ajax({
        url: 'getAllFile/?objectid='+objectid+'&page='+page.toString()+"&keyword="+keyword,
        type: 'GET',
        dataType: 'json',
        success: function(data){
            addHtml(data.data, page, keyword);
        }
    })
}

function addHtml(dataList, page, keyword){
    html = "";
    for(i=0; i<dataList.length; i++){
        data = dataList[i];
        html += "<a href=\"/fileParticular/?articleid="+data.articleid+"\" class=\"list-group-item\">\n" +
            "                                    <div class=\"row\">\n" +
            "                                        <div class=\"col-lg-7\">\n" +
            "                                            <h3 class=\"list-group-item-heading\">"+data.title+"</h3>\n" +
            "\n" +
            "                                        </div>\n" +
            "                                        <div class=\"col-lg-5\">\n" +
            "                                            <table>\n" +
            "                                                <tr>\n" +
            "                                                    <td style=\"width: 25%;\">时间："+data.posttime+"</td>\n" +
            "                                                    <td style=\"width: 25%;\">作者："+data.authorname+"</td>\n" +
            "                                                    <td style=\"width: 25%;\">网站："+data.webname+"</td>\n" +
            "                                                    <td style=\"width: 25%;\">类型："+data.webtype+"</td>\n" +
            "                                                </tr>\n" +
            "                                            </table>\n" +
            "                                        </div>\n" +
            "                                    </div>\n" +
            "                                    <p class=\"list-group-item-text\">\n" +
            "                                        "+data.content+"。\n" +
            "                                    </p>\n" +
            "                                </a>"
    };
    if(dataList.length == 20){
        html+="<a onclick=\"getFiles('', "+(page+1).toString()+",'"+keyword+"')\" class=\"list-group-item\" id='moreItems' style='cursor: pointer;'>\n" +
        "       <p class=\"list-group-item-text\">\n" +
        "             点击加载更多。\n" +
        "       </p>\n" +
        "  </a>"
    }
    if(page == 0){
        $("#results").children().remove();
        $("#results").append(html);
    }
    else{
        $("#moreItems").replaceWith(html);
    }
}