var eventsData = [{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
},{
  "name": "test",
  "index": "100",
  "number": "22323",
  "date": "2018-01-02",
  "id": "22332"
}];

var fileData = [{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},{
    "fileTitle": "test",
    "fileStar": "3323",
    "wroteTime": "2018-08-11",
    "id": "1111"
},]


function format (d) {
    // `d` is the original data object for the row
    return '<table>'+
        '<tr><td style="width: 80%;">'+
            '<table cellpadding="5" cellspacing="0" border="0" class="ui celled table" id="filesTable">'+
        '</table></td><td>'+
        '<button class="moreButton" onclick="toAllFiles()">所有文章</button></td>'+
        '</tr></table>';
}


function eventsTable(){
    var eventTable = $("#eventTable").DataTable({
        "dom": '<"top"if>rt<"bottom"lp><"clear">',
        "order": [2, "dsc"],
        "aLengthMenu": [[20,50,-1], [20, 50, "全部"]],
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
        "data": eventsData,
        "columns": [
            {"data": null, "class": "details-control", "orderable": false, "defaultContent": "", "title": "全部内容", "width": "10%"},
            {"data": "name", "title": "事件名称"},
            {"data": "index", "title": "事件热度"},
            {"data": "number", "title": "相关信息数"},
            {"data": "date", "title": "发生时间"},
            {"data": "id", "visible": false}
        ]
    });
    $('#eventTable tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = eventTable.row(tr);
        if ( row.child.isShown()){
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child(format(row.data())).show();
            tr.addClass('shown');
            filesTable();
        }
    });
}

function filesTable(){
    $("#filesTable").DataTable({
        // "dom": '<"top">rt<"bottom"><"clear">',
        "order": [1, "dsc"],
        "aLengthMenu": [[5], [5]],
        "language": {
            "lengthMenu": "",
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
        "data": fileData,
        "columns": [
            {"data": "fileTitle", "title": "文章标题"},
            {"data": "fileStar", "title": "文章赞数"},
            {"data": "wroteTime", "title": "写作时间"},
            {"data": "id", "visible": false}
        ]
    });
}

function toAllFiles(){
    window.location.href = '/fileSearch/';
}