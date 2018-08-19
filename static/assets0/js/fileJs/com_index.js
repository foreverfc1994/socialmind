
function emotionCompose(){

    emotionComposeOption = {
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            show: true,
            right: 130,
            top: 30,
            data: ['喜悦', '愤怒', '恐惧', '沮丧', '悲伤', '其他']
        },
        series: [
            {
                name: '情绪组成',
                type: 'pie',
                radius: ['35%', '65%'],
                labelLine: {
                    normal: {
                        show: true,
                        length: 20,
                        length2: 50,
                        lineStyle: {
                            color: '#333'
                        }
                    },
                    emphasis:{
                        show: true,
                    }

                },
                label: {
                    normal: {
                        show: false,
                        formatter: '{a|{d}%}\n{b|{b}}',
                        borderWidth: 0,
                        borderRadius: 4,
                        // shadowBlur:3,
                        // shadowOffsetX: 2,
                        // shadowOffsetY: 2,
                        // shadowColor: '#999',
                        padding: [0, -60],
                        rich: {
                            a: {
                                color: '#333',
                                fontSize: 16,
                                lineHeight: 20
                            },
                            // abg: {
                            //     backgroundColor: '#333',
                            //     width: '100%',
                            //     align: 'right',
                            //     height: 22,
                            //     borderRadius: [4, 4, 0, 0]
                            // },
                            hr: {
                                borderColor: '#333',
                                width: '100%',
                                borderWidth: 0.5,
                                height: 0
                            },
                            b: {
                                fontSize: 16,
                                lineHeight: 20,
                                color: '#333'
                            }
                            // per: {
                            //     color: '#333',
                            //     padding: [2, 4],
                            //     borderRadius: 2
                            // }
                        }
                    },
                    emphasis:{
                        show: true,
                    }
                },
                data: [{
                    value: 135,
                    name: '喜悦'
                }, {
                    value: 1048,
                    name: '愤怒'
                }, {
                    value: 251,
                    name: '恐惧'
                }, {
                    value: 147,
                    name: '沮丧'
                }, {
                    value: 102,
                    name: '悲伤'
                },{
                    value: 15,
                    name: '其他'
                }]
            }
        ]
    };

    var emotionCompose = echarts.init(document.getElementById("emotionCompose"));
    emotionCompose.setOption(emotionComposeOption);
}

function eventChange(){
    $.ajax({
        url: 'loadOrganizationData/emotionTrend/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            var dataList = data.data;
        }
    });
    esIOption = {
        tooltip: {
            type: 'showTip',
            trigger: 'axis'
        },
        grid: {
            top: '3%',
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['一月','二月','三月','四月','五月','六月','七月','八月']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:'相关事件数',
                smooth: true,
                type:'line',
                stack: '总量',
                color: '#000000',
                data:[120, 132, 101, 134, 90, 230, 210, 220]
            }
        ]
    };

    var eventChange_sensitive = echarts.init(document.getElementById("eventChange"));
    eventChange_sensitive.setOption(esIOption);
}
function sensitiveInform(){
    esIOption = {
        tooltip: {
            type: 'showTip',
            trigger: 'axis'
        },
        grid: {
            top: '3%',
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['一月','二月','三月','四月','五月','六月','七月','八月']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:'相关敏感信息数',
                smooth: true,
                type:'line',
                stack: '总量',
                data:[120, 132, 101, 134, 90, 230, 210, 220]
            }
        ]
    };

    var sensitiveInformInit = echarts.init(document.getElementById("sensitiveInform"));
    sensitiveInformInit.setOption(esIOption);
}

function emotionTrend(){
    var xAxisData = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'];
    var data1 = [12,21,15,61,45,9,84,45,15,15];
    var data2 = [-15,-35,-15,-35,-65,-45,-65,-5,-45,-45];
    var data3 = [];
    var num = 0;

    for (var i = 0; i < 10; i++) {
        num = data1[i] + data2[i];
        data3.push((num).toFixed(2));
    }

    var itemStyle = {
        normal: {
        },
        emphasis: {
            barBorderWidth: 1,
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowOffsetY: 0,
            shadowColor: 'rgba(0,0,0,0.5)'
        }
    };

    emotionTrendOption = {
        backgroundColor: '#eee',
        legend: {
            data: ['正面情绪指标', '负面情绪指标', '差值'],
            align: 'left',
            left: 100
        },
        tooltip: {},
        xAxis: {
            data: xAxisData,
            name: '月份',
            silent: false,
            axisLine: {onZero: true},
            splitLine: {show: false},
            splitArea: {show: true}
        },
        yAxis: {
            inverse: false,
            splitArea: {show: false}
        },
        grid: {
            left:100
        },
        series: [
            {
                name: '正面情绪指标',
                type: 'bar',
                stack: 'one',
                itemStyle: itemStyle,
                data: data1
            },
            {
                name: '负面情绪指标',
                type: 'bar',
                stack: 'one',
                itemStyle: itemStyle,
                data: data2
            },
            {
                name: '差值',
                type: 'bar',
                stack: 'two',
                itemStyle: itemStyle,
                data: data3
            }
        ]
    };

    var emotionTrendInit = echarts.init(document.getElementById("emotionTrend"));
    emotionTrendInit.setOption(emotionTrendOption);
}