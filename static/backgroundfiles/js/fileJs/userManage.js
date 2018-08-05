function personUserIndex(){
    layui.use('table', function(){
        var table = layui.table;
        table.render({
        elem: '#personUser'
        ,url:'List/person/'
        ,cellMinWidth: 80
        ,page: true
        ,cols: [[
           {field:'userid', title: '用户id', sort: true}
          ,{field:'username', title: '用户名', sort: true}
          ,{field:'realname', title: '真实姓名', sort: true}
          ,{field:'sex', title: '性别', sort: true}
          ,{field:'age', title: '年龄', sort: true}
          ,{field:'phoneNum', title: '手机号', minWidth: 100, sort: true}
          ,{field:'email', title: '邮箱', sort: true}
          ,{field:'job', title: '职业', sort: true}
          ,{field:'registrantTime', title: '注册时间', sort: true}
          ,{fixed:'right', title: '管理', sort: true, align: 'center', toolbar: '#deleteButton0'}
        ]]
        });
    })
}
function companyUserIndex(){
    layui.use('table', function(){
        var table = layui.table;
        table.render({
        elem: '#comUser'
        ,url:'List/company/'
        ,cellMinWidth: 80
        ,page: true
        ,cols: [[
           {field:'userid', title: '用户id', minWidth: 150, sort: true}
          ,{field:'username', title: '用户名',minWidth: 150, sort: true}
          ,{field:'companyname', title: '公司名称', minWidth: 150, sort: true}
          ,{field:'companytype', title: '公司类型', minWidth: 150, sort: true}
          ,{field:'email', title: '邮箱', minWidth: 200, sort: true}
          ,{field:'registertime', title: '公司登记注册时间', minWidth: 200, sort: true}
          ,{field:'registrantTime', title: '账号注册时间', minWidth: 180, sort: true}
          ,{fixed:'right', title: '管理', align: 'center', toolbar: '#deleteButton1'}
        ]]
        });
    })
}

function instituteUserIndex(){
    layui.use('table', function(){
        var table = layui.table;
        table.render({
        elem: '#institutionUser'
        ,url:'List/institute/'
        ,cellMinWidth: 80
        ,page: true
        ,cols: [[
           {field:'userid', title: '用户id', minWidth: 150, sort: true}
          ,{field:'username', title: '用户名',minWidth: 130, sort: true}
          ,{field:'institutionname', title: '机构名称', minWidth: 130, sort: true}
          ,{field:'institudecode', title: '机构代码', minWidth: 130, sort: true}
          ,{field:'institutionlevel', title: '机构级别', minWidth: 150, sort: true}
          ,{field:'institutiontype', title: '机构类型', minWidth: 150, sort: true}
          ,{field:'email', title: '邮箱', minWidth: 180, sort: true}
          ,{field:'registrantTime', title: '账号注册时间', minWidth: 150, sort: true}
          ,{fixed:'right', title: '管理', align: 'center', toolbar: '#deleteButton2'}
        ]]
        });
    })
}

function govermentUserIndex(){
    layui.use('table', function(){
        var table = layui.table;
        table.render({
        elem: '#govUser'
        ,url:'List/goverment/'
        ,cellMinWidth: 80
        ,page: true
        ,cols: [[
           {field:'userid', title: '用户id', minWidth: 180, sort: true}
          ,{field:'username', title: '用户名', minWidth: 180, sort: true}
          ,{field:'govname', title: '政府机构名', minWidth: 180, sort: true}
          ,{field:'govcode', title: '政府机构代码', minWidth: 180, sort: true}
          ,{field:'govType', title: '政府机构类型', minWidth: 100, sort: true}
          ,{field:'email', title: '邮箱', minWidth: 180, sort: true}
          ,{field:'registrantTime', title: '账号注册时间', minWidth: 180, sort: true}
          ,{fixed:'right', title: '管理', align: 'center', toolbar: '#deleteButton3'}
        ]]
        });
    })
}

