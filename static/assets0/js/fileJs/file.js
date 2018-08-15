function loadCommentsList(articleid){
    $.ajax({
        url: 'getComments/?articleid='+articleid,
        type: 'GET',
        dataType: 'json',
        success: function(data){
            loadComments(data.data);
        }
    })
}

function loadComments(dataList){
    var html = "";
    var num = dataList.length;
    if(num != 0){
        for(i=0;i<num;i++){
            var data = dataList[i];
            html += "<div class=\"commentBlock\">\n" +
                "        <table>\n" +
                "            <tr>\n" +
                "                <td class=\"commentsImgTd\">\n" +
                "                   <div class=\"commentsImgDiv\">\n" +
                "                        <img src=\"/static/assets0/img/product.jpg\" class=\"commentsImg\">\n" +
                "                   </div>\n" +
                "                </td>\n" +
                "                <td class=\"commentsCommentTd\">\n" +
                "                    <ul>\n" +
                "                         <p class=\"comment\"><b class=\"commenterName\">"+data.username+"：</b>"+data.content+"</p>\n" +
                "                    </ul>\n" +
                "                    <ul>\n" +
                "                          <span class=\"fl grayText\">"+data.commentTime+"</span>\n" +
                "                          <span class=\"fr cursorPoint\"><a href=\"javascript:void(0)\" class=\"grayText\">👍&nbsp;赞:&nbsp;&nbsp;2212&nbsp;&nbsp;</a></span>\n" +
                "                    </ul>\n" +
                "                </td>\n" +
                "            </tr>\n" +
                "         </table>\n" +
                "     </div>"
        }
    }
    $("#commentsDiv").children().remove();
    $("#commentsDiv").append(html);
}


function loadCorrelatFiles(objectid, page){
    if(objectid !== ""){
        $.ajax({
            url: 'getCorrelationFiles/?objectid='+objectid+"&page="+page,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                addCorrelatFiles(data.data, page, objectid);
            }
        })
    }
}

function addCorrelatFiles(dataList, page, objectid){
    var html = "";
    var length = dataList.length;
    if(length > 0){
        for(i=0; i<length; i++){
            data = dataList[i];
            html += "                    <div class=\"row\">\n" +
                "                        <a href=\"/fileParticular/?articleid="+data.articleid+"\">\n" +
                "                            <div class=\"col-lg-12\">\n" +
                "                                <div class=\"content-panel\">\n" +
                "                                    <div class=\"funcInIndex\">\n" +
                "                                        <button type=\"button\" class=\"btn btn-warning\" style=\"font-size: 10px;\">点赞 "+data.likeNum+"</button>\n" +
                "                                        <button type=\"button\" class=\"btn btn-warning\" style=\"font-size: 10px;\">评论 "+data.commentNum+"</button>\n" +
                "                                        <button type=\"button\" class=\"btn btn-warning\" style=\"font-size: 10px; margin-right: 15px;\">收藏 "+data.collectNum+"</button>\n" +
                "                                    </div>\n" +
                "                                    <div class=\"panel-body mt\" style=\"padding-left: 10px;\">\n" +
                "                                        <div id=\"recommendx\" class=\"recommend_news\">\n" +
                "                                            <p>\n" +
                "                                                <strong>"+data.title+"</strong> &nbsp; &nbsp; &nbsp; 发表日期： "+data.posttime+" &nbsp; &nbsp; &nbsp; 文章来源："+data.webSource+"\n" +
                "                                            </p>\n" +
                "                                        </div>\n" +
                "                                    </div>\n" +
                "                                    <div class=\"panel-body\" style=\"padding-left: 10px; height: 100px;\">\n" +
                "                                        <p class=\"to-much-p\" style='color: #000000'>"+data.content+"</p>\n" +
                "                                    </div>\n" +
                "                                </div>\n" +
                "                            </div>\n" +
                "                        </a>\n" +
                "                    </div>\n"
        }
    }
    if(length == 10){
        html += "<div class=\"row\" id='moreCorrelationFiles'>\n" +
            "                        <a href='javascript: void(0);' onclick=\"loadCorrelatFiles('"+objectid+"', "+(page+1)+")\">\n" +
            "                            <div class=\"col-lg-12\">\n" +
            "                                <div class=\"content-panel\">\n" +
            "<p style='text: center;'>点击加载更多</p>" +
            "                                </div>\n" +
            "                            </div>\n" +
            "                        </a>\n" +
            "                    </div>"
    }
    if(page == 0){
        $("#correlationFiles").append(html);
    }
    else{
        $("#moreCorrelationFiles").replaceWith(html);
    }
}

function operations(articleid, num){
    $.ajax({
        url: '/addOperation/?type=article&articleid='+articleid+'&num='+num,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            if(data.data == "true"){
                changeButton(num, articleid);
            }
            else{
                alert("操作失败，请重试");
            }
        },
        error: function(){
            alert("未知错误，请重试");
        }
    })
}
function resetButton(articleid, num){
    $.ajax({
            url: '/subOperation/?type=article&articleid='+articleid+"&num="+num,
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                if(data.data == "succeed"){
                    var bt = document.getElementById("eventData").getElementsByTagName("button")[num];
                    $(bt).removeClass("active");
                    $(bt).removeAttr("onclick");
                    $(bt).attr("onclick", "operations('"+articleid+"', "+num+");");
                    var number = $(bt).find("span").text();
                    var subNumber = parseInt(number)-1;
                    $(bt).find("span").text(subNumber);
                    number = null;
                    subNumber = null;
                }
                if(data.data !== "succeed"){
                    alert("操作失败，请重试");
                }
            },
            error: function(){
                alert("未知错误，请重试");
            }
    })
}

function changeButton(num, articleid){
    var bts = document.getElementById("eventData").getElementsByTagName("button");
    var bt = bts[num];
    if(num >= 2){
        var anthor = bts[5-num];
        if(anthor.className == "btn btn-warning eventButton active"){
            $(anthor).removeClass("active");
            $(anthor).removeAttr("onclick");
            $(anthor).attr("onclick", "operations('"+articleid+"', "+(5-num)+");");
            var nnumber = $(anthor).find("span").text();
            var ssubNumber = parseInt(nnumber)-1;
            $(anthor).find("span").text(ssubNumber);
            nnumber = null;
            ssubNumber = null;
        }
    }
    $(bt).addClass("active");
    $(bt).removeAttr("onclick");
    $(bt).attr("onclick", "resetButton('"+articleid+"', "+num+");");
    var number = $(bt).find("span").text();
    var subNumber = parseInt(number)+1;
    $(bt).find("span").text(subNumber);
    number = null;
    subNumber = null;
}

function loadOpear(articleid){
    $.ajax({
        url: 'getOperaData/?articleid='+articleid,
        type: 'GET',
        dataType: 'json',
        success: function(res){
            var data = res.data;
            var html = "";
            if(data.collected == "false"){
                html += "<button class=\"btn btn-warning eventButton\" onclick=\"operations('"+articleid+"', 0)\" id=\"collectButton\">📂 收藏量：<span>"+data.collectNum+"</span></button>";
            }
            else{
                html += "<button class=\"btn btn-warning eventButton active\" onclick=\"resetButton('"+articleid+"', 0)\" id=\"collectButton\">📂 收藏量：<span>"+data.collectNum+"</span></button>";
            }
            if(data.liked == "false"){
                html += "<button class=\"btn btn-warning eventButton\" onclick=\"operations('"+articleid+"', 1)\" id=\"likeButton\">👍 点赞数：<span>"+data.likeNum+"</span></button>";
            }
            else{
                html += "<button class=\"btn btn-warning eventButton active\" onclick=\"resetButton('"+articleid+"', 1)\" id=\"likeButton\">👍 点赞数：<span>"+data.likeNum+"</span></button>";
            }
            if(data.isTrue == "true"){
                html += "<button class=\"btn btn-warning eventButton active\" onclick=\"resetButton('"+articleid+"', 2)\" id=\"isTrueButton\">😊 判真数：<span>"+data.isTrueNum+"</span></button>";
                html += "<button class=\"btn btn-warning eventButton\" onclick=\"operations('"+articleid+"', 3)\" id=\"isFalseButton\">🤬 判假数：<span>"+data.isFalseNum+"</span></button>";
            }
            else if(data.isFalse == "true"){
                html += "<button class=\"btn btn-warning eventButton\" onclick=\"operations('"+articleid+"', 2)\" id=\"isTrueButton\">😊 判真数：<span>"+data.isTrueNum+"</span></button>";
                html += "<button class=\"btn btn-warning eventButton active\" onclick=\"resetButton('"+articleid+"', 3)\" id=\"isFalseButton\">🤬 判假数：<span>"+data.isFalseNum+"</span></button>";
            }
            else{
                html += "<button class=\"btn btn-warning eventButton\" onclick=\"operations('"+articleid+"', 2)\" id=\"isTrueButton\">😊 判真数：<span>"+data.isTrueNum+"</span></button>";
                html += "<button class=\"btn btn-warning eventButton\" onclick=\"operations('"+articleid+"', 3)\" id=\"isFalseButton\">🤬 判假数：<span>"+data.isFalseNum+"</span></button>";
            }
            $("#eventData").append(html);
        }
    });
}