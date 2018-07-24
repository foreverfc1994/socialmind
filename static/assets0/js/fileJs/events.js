
function footerKeeper(){

    function footerPosition(){
        $("footer").removeClass("fixed-bottom");
        var contentHeight = document.body.scrollHeight,//网页正文全文高度
            winHeight = window.innerHeight;//可视窗口高度，不包括浏览器顶部工具栏
        if(!(contentHeight > winHeight)){
            //当网页正文高度小于可视窗口高度时，为footer添加类fixed-bottom
            $("footer").addClass("fixed-bottom");
        } else {
            $("footer").removeClass("fixed-bottom");
        }
    }

    footerPosition();
    $(window).resize(footerPosition);
}

function clickedEventType(value){
    var liList = document.getElementById("eventTypeMenu").getElementsByTagName("li");
    var typeNum = document.getElementById("eventTypeMenu").getElementsByTagName("li").length;
    if(liList[value-1].className !== 'liAction'){
        document.getElementById("eventTypeMenu").getElementsByTagName("li")[value-1].className = "liAction";
        for(i=0; i<typeNum; i++){
            if(i !== value-1){
                document.getElementById("eventTypeMenu").getElementsByTagName("li")[i].className = "";
            }
        }
    }
    else{
        for(i=0; i<typeNum; i++){
            document.getElementById("eventTypeMenu").getElementsByTagName("li")[i].className = "";
        }
    }


}