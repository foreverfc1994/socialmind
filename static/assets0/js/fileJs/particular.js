function eventHeatIndex(){//事件热度
    option = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    series: [
        {
            name: 'heat',
            type: 'gauge',
            detail: {formatter:'{value}%'},
            data: [{value: 70, name: ""}]
        }
    ]
    };
    var chart = echarts.init(document.getElementById('heat'));
    chart.setOption(option);
}

function eventSensitiveIndex(){//事件敏感度
    option = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    series: [
        {
            name: 'sensitive',
            type: 'gauge',
            detail: {formatter:'{value}%'},
            data: [{value: 50, name: ''}]
        }
    ]
    };
    var chart = echarts.init(document.getElementById('sensitive'));
    chart.setOption(option,true);
}

function eventPolarityEvent(){//事件极性
    option = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    series: [
        {
            name: 'polarity',
            type: 'gauge',
            detail: {formatter:'{value}%'},
            data: [{value: 20, name: '事件极性'}]
        }
    ]
    };
    var chart = echarts.init(document.getElementById('polarity'));
    chart.setOption(option,true);
}

function eventTrend(){//事件走势
    var heatTrendCountData = {
         labels : ["January","February","March","April","May","June","July"],
         datasets : [{
             label: "全网信息数",
             fill: false,
             pointBackgroundColor: "#FF0000",
             borderColor: "#F08080",
             backgroundColor: "#F08080",
             data : [165,159,132,129,146,155,140]      //点的Y轴值
         },

             {
                 label: "热点文章数",
                 fill: false,
                 pointBackgroundColor: "#008000",
                 borderColor: "#32CD32",
                 backgroundColor: "#32CD32",
                 data : [32,44,22,99,33,22,4]      //点的Y轴值
             },
         {
                 label: "敏感文章数",
                 fill: false,
                 pointBackgroundColor: "#66CCFF",
                 borderColor: "#0033CC",
                 backgroundColor: "#0033CC",
                 data : [32,34,27,19,33,92,44]      //点的Y轴值
             }]
     };

    //定义图表的参数
    var heatTrendCountOptions = {
        title: {
            display: true,
            text: "事件走势统计",
            fontSize: 20,
            fontColor: "#000000",
        },
    };
    heatTrendCountconfig = {
        "type": "line",
        "data": heatTrendCountData,
        "options": heatTrendCountOptions,
    };
    new Chart(document.getElementById("heatTrendCount"), heatTrendCountconfig);
}

function heatIndexBoom(){//热度爆发统计
     var dataTime = {
     labels : ["January","February","March","April","May","June","July","August"],
     datasets : [{
         label: "热度指数",
         fill: false,
         pointBackgroundColor: "#FF0000",
         borderColor: "#F08080",
         backgroundColor: "#F08080",
         data : [11,159,250,330,1111,800,200,100]      //点的Y轴值
     }]
    };

    //定义图表的参数
    var optionsTime = {
        title: {
            display: true,
            text: "热度爆发统计",
            fontSize: 20,
            fontColor: "#000000",
        },
    };
    configTime = {
        "type": "line",
        "data": dataTime,
        "options": optionsTime,
    };

    new Chart(document.getElementById("heatTime"), configTime);
}

function mediaLivenessIndex(){//媒体活跃度
    var mediaLivenessData = {
        labels : ["新浪微博","微信","今日头条","中华网","新华网","凤凰网","新浪网","其他"],
        datasets : [{
         label: "媒体活跃度",
         data : [11552,9955,2550,1330,1111,800,200,100] ,
         backgroundColor: "#DAA520",
         borderColor: "#DAA520",
        }],
    };

    //定义图表的参数
    var mediaLivenessOptions = {
    };
    mediaLivenessConfig = {
        "type": "bar",
        "data": mediaLivenessData,
        "options": mediaLivenessOptions,
    };
    new Chart(document.getElementById("mediaLivenessBar"), mediaLivenessConfig);

}

function emotionTrend(){//情绪走势统计
    var emotionData = {
        labels : ["January","February","March","April","May","June","July"],
        datasets : [{
            label: "喜悦",
            fill: false,
            pointBackgroundColor: "#FF0000",
            borderColor: "#F08080",
            backgroundColor: "#F08080",
            data : [165,159,132,129,146,155,140]
            },

            {
             label: "中性",
             fill: false,
             pointBackgroundColor: "#008000",
             borderColor: "#32CD32",
             backgroundColor: "#32CD32",
             data : [32,44,22,99,33,22,4]
            },
            {
             label: "悲伤",
             fill: false,
             pointBackgroundColor: "#66CCFF",
             borderColor: "#0033CC",
             backgroundColor: "#0033CC",
             data : [32,34,27,19,33,92,44]
            },{
             label: "愤怒",
             fill: false,
             pointBackgroundColor: "#FF99CC",
             borderColor: "#FF6699",
             backgroundColor: "#FF6699",
             data : [12,21,17,9,13,12,4]      //点的Y轴值
            },{
             label: "惊奇",
             fill: false,
             pointBackgroundColor: "#FF9900",
             borderColor: "#FF6600",
             backgroundColor: "#FF6600",
             data : [5,8,9,6,2,14,1]      //点的Y轴值
            },{
             label: "恐惧",
             fill: false,
             pointBackgroundColor: "#00FF66",
             borderColor: "#33CC00",
             backgroundColor: "#33CC00",
             data : [2,1,2,2,0,1,1]      //点的Y轴值
            }]
    };

    //定义图表的参数
    var emotionOptions = {
        title: {
            display: true,
            text: "情绪走势统计",
            fontSize: 20,
            fontColor: "#000000",
        },
    };
    emotionConfig = {
        "type": "line",
        "data": emotionData,
        "options": emotionOptions,
    };
    new Chart(document.getElementById("emotionLine"), emotionConfig);
}

function heatIndexMap(){//热度地图
    function randomData() {
        return Math.round(Math.random()*500);
    }
    var mydata = [
        {name: '北京',value: randomData() },{name: '天津',value: randomData() },
        {name: '上海',value: randomData() },{name: '重庆',value: randomData() },
        {name: '河北',value: randomData() },{name: '河南',value: randomData() },
        {name: '云南',value: randomData() },{name: '辽宁',value: randomData() },
        {name: '黑龙江',value: randomData() },{name: '湖南',value: randomData() },
        {name: '安徽',value: randomData() },{name: '山东',value: randomData() },
        {name: '新疆',value: randomData() },{name: '江苏',value: randomData() },
        {name: '浙江',value: randomData() },{name: '江西',value: randomData() },
        {name: '湖北',value: randomData() },{name: '广西',value: randomData() },
        {name: '甘肃',value: randomData() },{name: '山西',value: randomData() },
        {name: '内蒙古',value: randomData() },{name: '陕西',value: randomData() },
        {name: '吉林',value: randomData() },{name: '福建',value: randomData() },
        {name: '贵州',value: randomData() },{name: '广东',value: randomData() },
        {name: '青海',value: randomData() },{name: '西藏',value: randomData() },
        {name: '四川',value: randomData() },{name: '宁夏',value: randomData() },
        {name: '海南',value: randomData() },{name: '台湾',value: randomData() },
        {name: '香港',value: randomData() },{name: '澳门',value: randomData() }
    ];
    var optionHeat = {
        backgroundColor: '#DCDCDC',
        title: {
            text: '热度地图',
            subtext: '纯属虚构',
            x:'center'
        },
        tooltip : {
            trigger: 'item',
            formatter: '{b}<br/>{c}'
        //    b为省份，c为数据
        },
        visualMap: {
            show : true,
            x: 'left',
            y: 'bottom',
            text: ['正面', '负面'],
            calculable: true,
            splitList: [
                {start: 500, end:600},{start: 400, end: 500},
                {start: 300, end: 400},{start: 200, end: 300},
                {start: 100, end: 200},{start: 0, end: 100},
            ],
            color: ['#00FF00', '#90EE90', '#ADFF2F','#FFFFE0', '#FFA07A', '#FF0000']
        },
        series: [{
            name: '随机数据',
            type: 'map',
            mapType: 'china',
            roam: false,
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            data:mydata
        }]
    };
    var chartHeat = echarts.init(document.getElementById('heatMap'));
    chartHeat.setOption(optionHeat);
}

function sensitiveIndexMap(){//敏感度地图
    function randomData() {
        return Math.round(Math.random()*500);
    }

    var mydata = [
        {name: '北京',value: randomData() },{name: '天津',value: randomData() },
        {name: '上海',value: randomData() },{name: '重庆',value: randomData() },
        {name: '河北',value: randomData() },{name: '河南',value: randomData() },
        {name: '云南',value: randomData() },{name: '辽宁',value: randomData() },
        {name: '黑龙江',value: randomData() },{name: '湖南',value: randomData() },
        {name: '安徽',value: randomData() },{name: '山东',value: randomData() },
        {name: '新疆',value: randomData() },{name: '江苏',value: randomData() },
        {name: '浙江',value: randomData() },{name: '江西',value: randomData() },
        {name: '湖北',value: randomData() },{name: '广西',value: randomData() },
        {name: '甘肃',value: randomData() },{name: '山西',value: randomData() },
        {name: '内蒙古',value: randomData() },{name: '陕西',value: randomData() },
        {name: '吉林',value: randomData() },{name: '福建',value: randomData() },
        {name: '贵州',value: randomData() },{name: '广东',value: randomData() },
        {name: '青海',value: randomData() },{name: '西藏',value: randomData() },
        {name: '四川',value: randomData() },{name: '宁夏',value: randomData() },
        {name: '海南',value: randomData() },{name: '台湾',value: randomData() },
        {name: '香港',value: randomData() },{name: '澳门',value: randomData() }
    ];
    var optionSensitive = {
        backgroundColor: '#DCDCDC',
        title: {
            text: '敏感度地图',
            subtext: '纯属虚构',
            x:'center'
        },
        tooltip : {
            trigger: 'item',
            formatter: '{b}<br/>{c}'
        //    b为省份，c为数据
        },
        visualMap: {
            show : true,
            x: 'left',
            y: 'bottom',
            text: ['正面', '负面'],
            calculable: true,
            splitList: [
                {start: 500, end:600},{start: 400, end: 500},
                {start: 300, end: 400},{start: 200, end: 300},
                {start: 100, end: 200},{start: 0, end: 100},
            ],
            color: ['#00FF00', '#90EE90', '#ADFF2F','#FFFFE0', '#FFA07A', '#FF0000']
        },
        series: [{
            name: '随机数据',
            type: 'map',
            mapType: 'china',
            roam: false,
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            data:mydata
        }]
    };
    var chartSensitive = echarts.init(document.getElementById('sensitiveMap'));
    chartSensitive.setOption(optionSensitive);
}

function emotionMap(){//情绪地图
    function randomData() {
        return Math.round(Math.random()*500);
    }
    var mydata = [
        {name: '北京',value: randomData() },{name: '天津',value: randomData() },
        {name: '上海',value: randomData() },{name: '重庆',value: randomData() },
        {name: '河北',value: randomData() },{name: '河南',value: randomData() },
        {name: '云南',value: randomData() },{name: '辽宁',value: randomData() },
        {name: '黑龙江',value: randomData() },{name: '湖南',value: randomData() },
        {name: '安徽',value: randomData() },{name: '山东',value: randomData() },
        {name: '新疆',value: randomData() },{name: '江苏',value: randomData() },
        {name: '浙江',value: randomData() },{name: '江西',value: randomData() },
        {name: '湖北',value: randomData() },{name: '广西',value: randomData() },
        {name: '甘肃',value: randomData() },{name: '山西',value: randomData() },
        {name: '内蒙古',value: randomData() },{name: '陕西',value: randomData() },
        {name: '吉林',value: randomData() },{name: '福建',value: randomData() },
        {name: '贵州',value: randomData() },{name: '广东',value: randomData() },
        {name: '青海',value: randomData() },{name: '西藏',value: randomData() },
        {name: '四川',value: randomData() },{name: '宁夏',value: randomData() },
        {name: '海南',value: randomData() },{name: '台湾',value: randomData() },
        {name: '香港',value: randomData() },{name: '澳门',value: randomData() }
    ];
    var optionEmotion = {
        backgroundColor: '#DCDCDC',
        title: {
            text: '情绪地图',
            subtext: '纯属虚构',
            x:'center'
        },
        tooltip : {
            trigger: 'item',
            formatter: '{b}<br/>{c}'
        //    b为省份，c为数据
        },
        visualMap: {
            show : true,
            x: 'left',
            y: 'bottom',
            text: ['正面', '负面'],
            calculable: true,
            splitList: [
                {start: 500, end:600},{start: 400, end: 500},
                {start: 300, end: 400},{start: 200, end: 300},
                {start: 100, end: 200},{start: 0, end: 100},
            ],
            color: ['#00FF00', '#90EE90', '#ADFF2F','#FFFFE0', '#FFA07A', '#FF0000']
        },
        series: [{
            name: '随机数据',
            type: 'map',
            mapType: 'china',
            roam: false,
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            data: mydata,
        }]
    };
    var emotionMap = echarts.init(document.getElementById('emotionMap'));
    emotionMap.setOption(optionEmotion);
}

function changePage(value){//切换按钮
    if(value=="open0"){
        document.getElementById("eventExponent").style.display = 'none';
        document.getElementById("change0").value = 'close0';
        document.getElementById("change0").setAttribute("class", "btn btn-warning event3Buttons");
        return;
    }
    else if(value=="close0"){
        document.getElementById("transportAnalyze").style.display = 'none';
        document.getElementById("change1").value = 'close1';
        document.getElementById("change1").setAttribute("class", "btn btn-warning event3Buttons");
        document.getElementById("emotionAnalyze").style.display = 'none';
        document.getElementById("change2").value = 'close2';
        document.getElementById("change2").setAttribute("class", "btn btn-warning event3Buttons");
        document.getElementById("eventExponent").style.display = 'block';
        document.getElementById("change0").value = 'open0';
        document.getElementById("change0").setAttribute("class", "btn btn-theme04 event3Buttons");
        return;
    }
    if(value=="open1"){
        document.getElementById("transportAnalyze").style.display = 'none';
        document.getElementById("change1").value = 'close1';
        document.getElementById("change1").setAttribute("class", "btn btn-warning event3Buttons");
        return;
    }
    else if(value=='close1'){
        document.getElementById("emotionAnalyze").style.display = 'none';
        document.getElementById("change2").value = 'close2';
        document.getElementById("change2").setAttribute("class", "btn btn-warning event3Buttons");
        document.getElementById("eventExponent").style.display = 'none';
        document.getElementById("change0").value = 'close0';
        document.getElementById("change0").setAttribute("class", "btn btn-warning event3Buttons");
        document.getElementById("transportAnalyze").style.display = 'block';
        document.getElementById("change1").value = 'open1';
        document.getElementById("change1").setAttribute("class", "btn btn-theme04 event3Buttons");
        return;
    }
    if(value=="open2"){
        document.getElementById("emotionAnalyze").style.display = 'none';
        document.getElementById("change2").value = 'close2';
        document.getElementById("change2").setAttribute("class", "btn btn-warning event3Buttons");
        return;
    }
    else if(value=='close2'){
        document.getElementById("transportAnalyze").style.display = 'none';
        document.getElementById("change1").value = 'close1';
        document.getElementById("change1").setAttribute("class", "btn btn-warning event3Buttons");
        document.getElementById("eventExponent").style.display = 'none';
        document.getElementById("change0").value = 'close0';
        document.getElementById("change0").setAttribute("class", "btn btn-warning event3Buttons");
        document.getElementById("emotionAnalyze").style.display = 'block';
        document.getElementById("change2").value = 'open2';
        document.getElementById("change2").setAttribute("class", "btn btn-theme04 event3Buttons");
        return;
    }
}

function keyWordsCloud(){
    var option = {
        tooltip: {},
        series: [ {
            type: 'wordCloud',
            gridSize: 2,
            sizeRange: [12, 50],
            rotationRange: [-90, 90],
            shape: 'pentagon',
            width: 600,
            height: 400,
            drawOutOfBound: true,
            textStyle: {
                normal: {
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    }
                },
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: [
                {
                    name: 'Sam S Club',
                    value: 10000,
                    textStyle: {
                        normal: {
                            color: 'black'
                        },
                        emphasis: {
                            color: 'red'
                        }
                    }
                },
                {
                    name: 'Macys',
                    value: 6181
                },
                {
                    name: 'Amy Schumer',
                    value: 4386
                },
                {
                    name: 'Jurassic World',
                    value: 4055
                },
                {
                    name: 'Charter Communications',
                    value: 2467
                },
                {
                    name: 'Chick Fil A',
                    value: 2244
                },
                {
                    name: 'Planet Fitness',
                    value: 1898
                },
                {
                    name: 'Pitch Perfect',
                    value: 1484
                },
                {
                    name: 'Express',
                    value: 1112
                },
                {
                    name: 'Home',
                    value: 965
                },
                {
                    name: 'Johnny Depp',
                    value: 847
                },
                {
                    name: 'Lena Dunham',
                    value: 582
                },
                {
                    name: 'Lewis Hamilton',
                    value: 555
                },
                {
                    name: 'KXAN',
                    value: 550
                },
                {
                    name: 'Mary Ellen Mark',
                    value: 462
                },
                {
                    name: 'Farrah Abraham',
                    value: 366
                },
                {
                    name: 'Rita Ora',
                    value: 360
                },
                {
                    name: 'Serena Williams',
                    value: 282
                },
                {
                    name: 'NCAA baseball tournament',
                    value: 273
                },
                {
                    name: 'Point Break',
                    value: 265
                }
            ]
        } ]
    };
    var chart = echarts.init(document.getElementById('cloud2'));
    chart.setOption(option);
    window.onresize = chart.resize;
}

function eventJudgeRatio(){
    var config = {
        type: 'doughnut',
        data:{
            datasets:[{
                data:[
                    40,
                    50,
                    10,
                ],
                backgroundColor:[
                    "#FFA500",
                    "#666666",
                    "#CC0000",
                ],
            }],
            labels:[
                "正面比例：",
                "负面比例：",
                "中性",
            ],
        },
        options:{
            cutoutPercentage: 60,
            responsive: true,
            legend:{
                display: true,
                position: "bottom",
            },
            title: {
                display: true,
                fontSize: 20,
                fontColor: "#000000",
                text: "事件正负面评价比例",
            },
            animation:{
                animateScale: true,
                animateRoatae: true
            }
        }
    };
    var myDoughnut = new Chart(document.getElementById("serverstatusEJ").getContext("2d"), config);
}

function emotionRatio(){
     var config = {
        type: 'doughnut',
        data:{
        datasets:[{
            data:[
                50,
                25,
                15,
                5,
                2.5,
                1.5,
                1
            ],
            backgroundColor:[
                "#FFA500",
                "#666666",
                "#3399CC",
                "#CC0000",
                "#33FF66",
                "#CCFFFF",
                "#9966FF",
            ],
        }],
        labels:[
            "喜悦",
            "惊奇",
            "中性",
            "悲伤",
            "愤怒",
            "恐惧",
            "其他",
        ],
        },
        options:{
        cutoutPercentage: 60,
        responsive: true,
        legend:{
            display: true,
            position: "bottom",
        },
        title: {
            display: true,
            fontSize: 20,
            fontColor: "#000000",
            text: "事件情绪占比",
        },
        animation:{
            animateScale: true,
            animateRoatae: true
        }
        }
        };
        var myDoughnut = new Chart(document.getElementById("serverstatusEM").getContext("2d"), config);
}

function informNet(){
    var informNetData = {"nodes": [
            {"color": "#4f19c7", "label": "大V一号", "attributes": {}, "y": 0, "x": 0, "id": "大V一号", "size": 5},
            {"color": "#4f19c7", "label": "大V二号", "attributes": {}, "y": 30, "x": 30, "id": "大V二号", "size": 8},
            {"color": "#4f19c7", "label": "大V3号", "attributes": {}, "y": 30, "x": -30, "id": "大V二号", "size": 15},
            {"color": "#4f19c7", "label": "大V4号", "attributes": {}, "y": -30, "x": 30, "id": "大V二号", "size": 8},
            {"color": "#4f19c7", "label": "大V5号", "attributes": {}, "y": -30, "x": -30, "id": "大V二号", "size": 6},
            {"color": "#4f19c7", "label": "大V6号", "attributes": {}, "y": 60, "x": 60, "id": "大V二号", "size": 14},
            {"color": "#4f19c7", "label": "大V7号", "attributes": {}, "y": 60, "x": -60, "id": "大V二号", "size": 5},
            {"color": "#4f19c7", "label": "大V8号", "attributes": {}, "y": -60, "x": 60, "id": "大V二号", "size": 3},
            {"color": "#4f19c7", "label": "大V9号", "attributes": {}, "y": -60, "x": -60, "id": "大V二号", "size": 1},
            {"color": "#4f19c7", "label": "大V10号", "attributes": {}, "y": 90, "x": 90, "id": "大V二号", "size": 5},
            {"color": "#4f19c7", "label": "大V11号", "attributes": {}, "y": 90, "x": -90, "id": "大V二号", "size": 8},
            {"color": "#4f19c7", "label": "大V11号", "attributes": {}, "y": -90, "x": -90, "id": "大V二号", "size": 2}
            ]};
    informNetDiv.showLoading();
    $.getJSON(informNetData, function (json) {
        informNetDiv.hideLoading();
        informNetDiv.setOption(option = {
            title: {
                text: 'NPM Dependencies'
            },
            animationDurationUpdate: 1500,
            animationEasingUpdate: 'quinticInOut',
            series : [
                {
                    type: 'graph',
                    layout: 'none',
                    // progressiveThreshold: 700,
                    data: json.nodes.map(function (node) {
                        return {
                            x: node.x,
                            y: node.y,
                            id: node.id,
                            name: node.label,
                            symbolSize: node.size,
                            itemStyle: {
                                normal: {
                                    color: node.color
                                }
                            }
                        };
                    }),
                    edges: json.edges.map(function (edge) {
                        return {
                            source: edge.sourceID,
                            target: edge.targetID
                        };
                    }),
                    label: {
                        emphasis: {
                            position: 'right',
                            show: true
                        }
                    },
                    roam: true,
                    lineStyle: {
                        normal: {
                            width: 0.5,
                            curveness: 0.3,
                            opacity: 0.7
                        }
                    }
                }
            ]
        }, true);
    });
}