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
    html = "";
    num = dataList.length;
    if(num != 0){
        for(i=0;i<num;i++){
            data = dataList[i]
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
                "                          <span class=\"fl grayText\">"+data.messageTime+"</span>\n" +
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
