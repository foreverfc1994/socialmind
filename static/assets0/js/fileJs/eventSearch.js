function pickType(num){
    var tds = document.getElementById("typeSelect").getElementsByTagName("td");
    tds[num].className = "active";
    for(i=0; i<14; i++){
        if(i != num){
            td = tds[i];
            $(td).removeClass();
        }
    }
}