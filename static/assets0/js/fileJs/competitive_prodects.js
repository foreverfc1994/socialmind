function eventHeatIndex1(){//事件热度
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
    var chart = echarts.init(document.getElementById('heat1'));
    chart.setOption(option);
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
    var chart1 = echarts.init(document.getElementById('heat2'));
    chart1.setOption(option);
}

function eventSensitiveIndex1(){//事件敏感度
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
    var chart = echarts.init(document.getElementById('sensitive1'));
    chart.setOption(option,true);
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
    var chart = echarts.init(document.getElementById('sensitive2'));
    chart.setOption(option,true);
}
function eventPolarityEvent1(){//事件极性
    option = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    series: [
        {
            name: 'polarity',
            type: 'gauge',
            detail: {formatter:'{value}%'},
            data: [{value: 20, name: ''}]
        }
    ]
    };
    var chart = echarts.init(document.getElementById('polarity1'));
    chart.setOption(option,true);
    option = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    series: [
        {
            name: 'polarity',
            type: 'gauge',
            detail: {formatter:'{value}%'},
            data: [{value: 20, name: ''}]
        }
    ]
    };
    var chart = echarts.init(document.getElementById('polarity2'));
    chart.setOption(option,true);
}

function eventTrendStatistic1(){//事件走势统计
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
    };
    heatTrendCountconfig = {
        "type": "line",
        "data": heatTrendCountData,
        "options": heatTrendCountOptions,
    };
    new Chart(document.getElementById("heatTrendCount1"), heatTrendCountconfig);
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
    };
    heatTrendCountconfig = {
        "type": "line",
        "data": heatTrendCountData,
        "options": heatTrendCountOptions,
    };
    new Chart(document.getElementById("heatTrendCount2"), heatTrendCountconfig);
}

function heatIndexBoom1(){//热度爆发统计
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
    };
    configTime = {
        "type": "line",
        "data": dataTime,
        "options": optionsTime,
    };

    new Chart(document.getElementById("heatTime1"), configTime);
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
    };
    configTime = {
        "type": "line",
        "data": dataTime,
        "options": optionsTime,
    };

    new Chart(document.getElementById("heatTime2"), configTime);
}

function heatIndexMap1(){//热度地图
    function randomData() {
        return Math.round(Math.random()*200);
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
    var chartHeat = echarts.init(document.getElementById('heatMap1'));
    chartHeat.setOption(optionHeat);
     function randomData() {
        return Math.round(Math.random()*200);
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
    var chartHeat = echarts.init(document.getElementById('heatMap2'));
    chartHeat.setOption(optionHeat);
}
function sensitiveIndexMap1(){//敏感度地图
    function randomData() {
        return Math.round(Math.random()*200);
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
    var chartSensitive = echarts.init(document.getElementById('sensitiveMap1'));
    chartSensitive.setOption(optionSensitive);
    function randomData() {
        return Math.round(Math.random()*200);
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
    var chartSensitive = echarts.init(document.getElementById('sensitiveMap2'));
    chartSensitive.setOption(optionSensitive);
}

function keyWordsCloud1(){//关键词云
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
    var chart = echarts.init(document.getElementById('cloud1'));
    chart.setOption(option);
    window.onresize = chart.resize;
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

function informSource1(){
    var informSourceData = {"sourceData": [{
        "name": "社交平台", "children":[{
            "name": "新浪微博", "value": 2232
            },{
            "name": "微信公众号", "value": 1221
            },{
            "name": "QQ空间", "value": 999
            },{
            "name": "其他", "value": 11
            }]
        },{
        "name": "新媒体", "children":[{
            "name": "今日头条", "value": 778
            },{
            "name": "xx新闻", "value": 112
            },{
            "name": "其他", "value": 11
            }]
        },{
        "name": "传统媒体", "children":[{
            "name": "新华网", "value": 1000
            },{
            "name": "华商报", "value": 100
            },{
            "name": "其他", "value": 50
            }]
        }]
    };
    informSourceOption = {
        visualMap: {
            type: 'continuous',
            min: 0,
            max: 2000,
            inRange: {
                color: ['#2D5F73', '#538EA6', '#F2D1B3', '#F2B8A2', '#F28C8C']
            },
            left: 10,
            bottom: 40,
        },
        series: {
            type: 'sunburst',
            data: informSourceData.sourceData,
            radius: ["15%", '90%'],
        },
    };
    var informSource = echarts.init(document.getElementById("informSourcePic1"));
    informSource.setOption(informSourceOption);
    var informSourceData = {"sourceData": [{
        "name": "社交平台", "children":[{
            "name": "新浪微博", "value": 2232
            },{
            "name": "微信公众号", "value": 1221
            },{
            "name": "QQ空间", "value": 999
            },{
            "name": "其他", "value": 11
            }]
        },{
        "name": "新媒体", "children":[{
            "name": "今日头条", "value": 778
            },{
            "name": "xx新闻", "value": 112
            },{
            "name": "其他", "value": 11
            }]
        },{
        "name": "传统媒体", "children":[{
            "name": "新华网", "value": 1000
            },{
            "name": "华商报", "value": 100
            },{
            "name": "其他", "value": 50
            }]
        }]
    };
    informSourceOption = {
        visualMap: {
            type: 'continuous',
            min: 0,
            max: 2000,
            inRange: {
                color: ['#2D5F73', '#538EA6', '#F2D1B3', '#F2B8A2', '#F28C8C']
            },
            left: 10,
            bottom: 40,
        },
        series: {
            type: 'sunburst',
            data: informSourceData.sourceData,
            radius: ["15%", '90%'],
        },
    };
    var informSource = echarts.init(document.getElementById("informSourcePic2"));
    informSource.setOption(informSourceOption);
}

function mediaLivenessIndex1(){//媒体活跃度
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
    new Chart(document.getElementById("mediaLivenessBar1"), mediaLivenessConfig);
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
    new Chart(document.getElementById("mediaLivenessBar2"), mediaLivenessConfig);
}

function eventJudgeRatio1(){
    var configg = {
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
            animation:{
                animateScale: true,
                animateRoatae: true
            }
        }
    };
    var myDoughnut = new Chart(document.getElementById("serverstatusEJ1").getContext("2d"), configg);
    var configg = {
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
            animation:{
                animateScale: true,
                animateRoatae: true
            }
        }
    };
    var myDoughnut = new Chart(document.getElementById("serverstatusEJ2").getContext("2d"), configg);
}

function emotionRatio1(){
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
        animation:{
            animateScale: true,
            animateRoatae: true
        }
        }
        };
        var myDoughnut = new Chart(document.getElementById("serverstatusEM1").getContext("2d"), config);
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
        animation:{
            animateScale: true,
            animateRoatae: true
        }
        }
        };
        var myDoughnut = new Chart(document.getElementById("serverstatusEM2").getContext("2d"), config);
}

function emotionMap1(){//情绪地图
    function randomData() {
        return Math.round(Math.random()*200);
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
    var emotionMap = echarts.init(document.getElementById('emotionMap1'));
    emotionMap.setOption(optionEmotion);
    function randomData() {
        return Math.round(Math.random()*200);
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
    var emotionMap = echarts.init(document.getElementById('emotionMap2'));
    emotionMap.setOption(optionEmotion);
}

function emotionTrend1(){//情绪走势统计
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
    };
    emotionConfig = {
        "type": "line",
        "data": emotionData,
        "options": emotionOptions,
    };
    new Chart(document.getElementById("emotionTrendLine1"), emotionConfig);
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
    };
    emotionConfig = {
        "type": "line",
        "data": emotionData,
        "options": emotionOptions,
    };
    new Chart(document.getElementById("emotionTrendLine2"), emotionConfig);
}