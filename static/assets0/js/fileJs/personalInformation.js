function clickedHistory(num){
    var buttonList = document.getElementsByClassName("buttonFlag");
    buttonList[num].className = "bigButtonClicked buttonFlag";
    for(i=0;i<4;i++){
        if(i!=num){
            buttonId = buttonList[i].id;
            $(buttonId).removeClass();
            buttonList[i].className = "bigButton buttonFlag";
        }
    }
}