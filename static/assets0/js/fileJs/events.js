
function format (d, objectid) {
    // `d` is the original data object for the row
    return '<table>'+
        '<tr><td style="width: 80%;">'+
            '<table cellpadding="5" cellspacing="0" border="0" class="ui celled table" id="filesTable">'+
        '</table></td><td>'+
        '<button class="moreButton" onclick="toAllFiles(\''+objectid+'\')">所有文章</button></td>'+
        '</tr></table>';
}


function eventsTable(func){
    $.ajax({
        url: 'getData/?func='+func,
        type: 'GET',
        dataType: 'json',
        success: function(data){
            indexTable(data.data);
        }
    });
    function indexTable(dataList){
        var eventTable = $("#eventTable").DataTable({
            "dom": '<"top"if>rt<"bottom"lp><"clear">',
            "ordering": false,
            "stateSave": true,
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
            "data": dataList,
            "columns": [
                {"data": null, "class": "details-control", "defaultContent": "", "title": "全部内容", "width": "8%", "searchable": false},
                {"data": null, "title": "事件名称", "orderable": false, "render": function aaa(data){return "<a href='/eventParticular/?objectid="+data.objectid+"'>"+data.name+"</a>"}},
                {"data": "heatIndex", "title": "事件热度", "orderable": false},
                {"data": "newsNum", "title": "相关信息数", "orderable": false},
                {"data": "begintime", "title": "发生时间", "orderable": false},
                {"data": "objectid", "visible": false, "searchable": false, "orderable": false},
            ]
        });
        $('#eventTable tbody').on('click', 'td.details-control', function () {
            var tr = $(this).closest('tr');
            var rowIndex = tr.index();
            var objectid = $("#eventTable").DataTable().row(rowIndex).data().objectid;
            $.ajax({
                url: 'getArticle/?objectid='+objectid,
                type: 'GET',
                dataType: 'json',
                async: false,
                success: function(data){
                    articleList = data.data;
                }
            });
            var row = eventTable.row(tr);
            if ( row.child.isShown()){
                // This row is already open - close it
                row.child.hide();
                tr.removeClass('shown');
            }
            else {
                // Open this row
                row.child(format(row.data(), objectid)).show();
                tr.addClass('shown');
                filesTable();
            }
        });
    }
}

function filesTable(){
    $("#filesTable").DataTable({
        "dom": '<"top"><"bottom"><"clear">',
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
        "data": articleList,
        "columns": [
            {"data": null, "title": "文章标题", "render": function toFile(data){return "<a href='/fileParticular/?articleid="+data.id+"' title='"+data.fileTitle+"'>"+data.fileTitle+"</a>"}},
            {"data": "fileStar", "title": "文章赞数"},
            {"data": "wroteTime", "title": "写作时间"},
            {"data": "id", "visible": false}
        ]
    });
}

function toAllFiles(objectid){
    window.location.href = '/fileSearch/?objectid='+objectid;
}