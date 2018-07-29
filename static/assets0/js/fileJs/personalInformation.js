function clickedHistory(num){
    var buttonList = document.getElementsByClassName("buttonFlag");
    buttonList[num].className = "bigButtonClicked buttonFlag";
    for(i=0;i<4;i++){
        if(i!=num){
            buttonId = buttonList[i].id;
            $(buttonId).removeClass();
            buttonList[i].className = "bigButton buttonFlag";
        }
    };
    if(num==0){
        $("#items").replaceWith("<div class=\"files\" id=\"items\">\n" +
            "                                <strong class=\"historyTitle\">我的浏览</strong>\n" +
            "                                <a href=\"javascript:void(0)\" onclick=\"clickedHistory(0)\" style='color: #000000;'>&nbsp;&nbsp;&nbsp;&nbsp;事件浏览</a>\n" +
            "                                <a href=\"javascript:void(0)\" onclick=\"toFiles(0)\" style='color: #999999;'>&nbsp;&nbsp;&nbsp;&nbsp;文章浏览</a>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                            </div>");
    }
    if(num==1){
         $("#items").replaceWith("<div class=\"files\" id=\"items\">\n" +
             "                                <strong class=\"historyTitle\">我的评论</strong>\n" +
             "                                <a href=\"javascript:void(0)\" onclick=\"clickedHistory(1)\" style='color: #00000'>&nbsp;&nbsp;&nbsp;&nbsp;我评论的事件</a>\n" +
             "                                <a href=\"javascript:void(0)\" onclick=\"toFiles(1)\" style='color: #999999'>&nbsp;&nbsp;&nbsp;&nbsp;我评论的文章</a>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                            </div>");
    }
    if(num==2){
         $("#items").replaceWith("<div class=\"files\" id=\"items\">\n" +
             "                                <strong class=\"historyTitle\">我的点赞</strong>\n" +
             "                                <a href=\"javascript:void(0)\" onclick=\"clickedHistory(2)\" style='color: #000000;'>&nbsp;&nbsp;&nbsp;&nbsp;事件点赞</a>\n" +
             "                                <a href=\"javascript:void(0)\" onclick=\"toFiles(2)\" style='color: #999999;'>&nbsp;&nbsp;&nbsp;&nbsp;文章点赞</a>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                            </div>");
    }
    if(num==3){
         $("#items").replaceWith("<div class=\"files\" id=\"items\">\n" +
             "                                <strong class=\"historyTitle\">我的收藏</strong>\n" +
             "                                <a href=\"javascript:void(0)\" onclick=\"clickedHistory(3)\" style='color: #000000;'>&nbsp;&nbsp;&nbsp;&nbsp;事件收藏</a>\n" +
             "                                <a href=\"javascript:void(0)\" onclick=\"toFiles(3)\" style='color: #999999;'>&nbsp;&nbsp;&nbsp;&nbsp;文章收藏</a>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                                <div class=\"filesTable mt\">\n" +
             "                                    <table class=\"filesBlock\">\n" +
             "                                        <tr>\n" +
             "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">事件标题</strong></td>\n" +
             "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;时间： 2017-10-20 &nbsp; &nbsp; &nbsp; 事件分类： 个人事件</p></td>\n" +
             "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
             "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                        <tr class=\"fileTextTr\">\n" +
             "                                            <td colspan=\"3\" class=\"fileP\">\n" +
             "                                                <a href=\"/fileParticular/\">\n" +
             "                                                    <p class=\"to-much-p\">\n" +
             "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
             "                                                    </p>\n" +
             "                                                </a>\n" +
             "                                            </td>\n" +
             "                                        </tr>\n" +
             "                                    </table>\n" +
             "                                </div>\n" +
             "                            </div>");
    }
}

function toFiles(num){
        if(num==0){
        $("#items").replaceWith("<div class=\"files\" id=\"items\">\n" +
            "                                <strong class=\"historyTitle\">我的浏览</strong>\n" +
            "                                <a href=\"javascript:void(0)\" onclick=\"clickedHistory(0)\" style='color: #999999;'>&nbsp;&nbsp;&nbsp;&nbsp;事件浏览</a>\n" +
            "                                <a href=\"javascript:void(0)\" onclick=\"toFiles(0)\" style='color: #000000;'>&nbsp;&nbsp;&nbsp;&nbsp;文章浏览</a>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">文章标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;发表时间： 2017-10-20</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">文章标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;发表时间： 2017-10-20</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">文章标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;发表时间： 2017-10-20</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">文章标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;发表时间： 2017-10-20</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">文章标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;发表时间： 2017-10-20</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">文章标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;发表时间： 2017-10-20</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                                <div class=\"filesTable mt\">\n" +
            "                                    <table class=\"filesBlock\">\n" +
            "                                        <tr>\n" +
            "                                            <td class=\"verticalBottom\" style=\"width: 15%;\"><strong style=\"font-size: 20px;\">文章标题</strong></td>\n" +
            "                                            <td class=\"verticalBottom\"><p>&nbsp; &nbsp;发表时间： 2017-10-20</p></td>\n" +
            "                                            <td class=\"verticalBottom\" style=\"text-align: right;\">\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">点赞 1</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px;\">评论 2</button>\n" +
            "                                                <button type=\"button\" class=\"btn btn-warning mt\" style=\"font-size: 10px; margin-right: 15px;\">收藏 3</button>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                        <tr class=\"fileTextTr\">\n" +
            "                                            <td colspan=\"3\" class=\"fileP\">\n" +
            "                                                <a href=\"/fileParticular/\">\n" +
            "                                                    <p class=\"to-much-p\">\n" +
            "                                                        测试测试测试测试测试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                        试测试测试测试测试测试测试测试测试测试试测试测试测试测试测试测试测试测试测试\n" +
            "                                                    </p>\n" +
            "                                                </a>\n" +
            "                                            </td>\n" +
            "                                        </tr>\n" +
            "                                    </table>\n" +
            "                                </div>\n" +
            "                            </div>");
    }
}