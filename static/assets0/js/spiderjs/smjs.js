function setspeedchart(web) {
    $.ajax({
        type: "POST",//方法类型
        dataType: "json",//预期服务器返回的数据类型
        url: "/queryspider/",//url
        data: {"web": web, "type": 'SpiderWeekSpeed'},
        success: function (data) {
            // console.log(data)

            option = {
                title: {
                    text: '爬虫一周速率变化',
                    subtext: '豆瓣小组'
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['page速率', 'item速率']
                },
                toolbox: {
                    show: true,
                    feature: {
                        dataZoom: {
                            yAxisIndex: 'none'
                        },
                        dataView: {readOnly: false},
                        magicType: {type: ['line', 'bar']},
                        restore: {},
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    // data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                    data: data.data['time']
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        formatter: '{value} /min'
                    }
                },
                series: [
                    {
                        name: 'page速率',
                        type: 'line',
                        // data: [11, 11, 15, 13, 12, 13, 10],
                        data: data.data['page'],
                        markPoint: {
                            data: [
                                {type: 'max', name: '最大值'},
                                {type: 'min', name: '最小值'}
                            ]
                        },
                        markLine: {
                            data: [
                                {type: 'average', name: '平均值'}
                            ]
                        }
                    },
                    {
                        name: 'item速率',
                        type: 'line',
                        // data: [1, -2, 2, 5, 3, 2, 0],
                        data: data.data['item'],
                        markPoint: {
                            data: [
                                // {name: '周最低', value: -2, xAxis: 1, yAxis: -1.5}
                                {type: 'max', name: '最大值'},
                                {type: 'min', name: '最小值'}
                            ]
                        },
                        markLine: {
                            data: [
                                {type: 'average', name: '平均值'},
                                // [{
                                //     symbol: 'circle',
                                //     x: '90%',
                                //     yAxis: 'max'
                                // }, {
                                //     symbol: 'circle',
                                //     label: {
                                //         normal: {
                                //             position: 'start',
                                //             formatter: '最大值'
                                //         }
                                //     },
                                //     type: 'max',
                                //     name: '最高点'
                                // }]
                            ]
                        }
                    }
                ]
            };
            var myChart = echarts.init(document.getElementById('weekspeed'));
            myChart.setOption(option, true);
        },
        error: function (data) {
            layer.msg('获取数据错误')
        }
    })


}

function errorchart() {
    var web = $("#errorweb").selectpicker('val')
    var time = $("#errortime").selectpicker('val')
    var data = {'web': web, 'time': time}
    $.ajax({
        type: "POST",//方法类型
        dataType: "json",//预期服务器返回的数据类型
        url: "/queryerror/",//url
        data: data,
        success: function (data) {
            // console.log(0)
            // console.log(data)
            var colors = ['#5793f3', '#d14a61', '#675bba'];
            // console.log(111)
            option = {
                color: colors,

                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross'
                    }
                },
                grid: {
                    right: '10%'
                },
                toolbox: {
                    feature: {
                        dataView: {show: true, readOnly: false},
                        restore: {show: true},
                        saveAsImage: {show: true}
                    }
                },
                legend: {
                    data: ['出错数', '正常数']
                },
                xAxis: [
                    {
                        type: 'category',
                        axisTick: {
                            alignWithLabel: true
                        },
                        // data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
                        data: data['time']
                    }
                ],
                yAxis: [

                    {
                        type: 'value',
                        name: '出错数',

                        position: 'right',
                        axisLine: {
                            lineStyle: {
                                color: colors[1]
                            }
                        },
                        axisLabel: {
                            formatter: '{value}'
                        }
                    },
                    {
                        type: 'value',
                        name: '正常数',

                        position: 'left',
                        axisLine: {
                            lineStyle: {
                                color: colors[2]
                            }
                        },
                        axisLabel: {
                            formatter: '{value}'
                        }
                    }
                ],
                series: [

                    {
                        name: '出错数',
                        type: 'bar',
                        yAxisIndex: 0,
                        // data: [100, 200, 300, 100, 200, 400, 600, 50, 70, 350, 100, 300]
                        data: data['bad']
                    },
                    {
                        name: '正常数',
                        type: 'line',
                        yAxisIndex: 1,
                        // data: [30000, 45000, 35100, 40000, 60000, 75000, 50000, 40000, 60000, 40000, 80000, 40000]
                        data: data['all']
                    }
                ]
            };
            // console.log(222)
            var myChart1 = echarts.init(document.getElementById('errorchart'));
            myChart1.setOption(option, true);
            // console.log(333)
        }
    });

}

function setlinedata() {
    var web = $("#numweb").selectpicker('val')
    var time = $("#numtime").selectpicker('val')
    $.ajax({
        type: "POST",//方法类型
        dataType: "json",//预期服务器返回的数据类型
        url: "/queryspidernum/",//url
        data: {"web": web, "interval": time},
        success: function (data) {
            // console.log(data)

            option = {
                title: {
                    text: data['web'] + '爬取数据量变化',
                    // subtext: data['name']
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['主题', '评论', '作者']
                },
                toolbox: {
                    show: true,
                    feature: {
                        dataZoom: {
                            yAxisIndex: 'none'
                        },
                        dataView: {readOnly: false},
                        magicType: {type: ['line', 'bar']},
                        restore: {},
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    // data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                    data: data['time']
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        formatter: '{value}'
                    }
                },
                series: [
                    {
                        name: '主题',
                        type: 'line',
                        // data: [11, 11, 15, 13, 12, 13, 10],
                        data: data['topic'],
                        markPoint: {
                            data: [
                                {type: 'max', name: '最大值'},
                                {type: 'min', name: '最小值'}
                            ]
                        },
                        markLine: {
                            data: [
                                {type: 'average', name: '平均值'}
                            ]
                        }
                    },
                    {
                        name: '评论',
                        type: 'line',
                        // data: [1, -2, 2, 5, 3, 2, 0],
                        data: data['comment'],
                        markPoint: {
                            data: [
                                // {name: '周最低', value: -2, xAxis: 1, yAxis: -1.5}
                                {type: 'max', name: '最大值'},
                                {type: 'min', name: '最小值'}
                            ]
                        },
                        markLine: {
                            data: [
                                {type: 'average', name: '平均值'},

                            ]
                        }
                    },
                    {
                        name: '作者',
                        type: 'line',
                        // data: [1, -2, 2, 5, 3, 2, 0],
                        data: data['author'],
                        markPoint: {
                            data: [
                                // {name: '周最低', value: -2, xAxis: 1, yAxis: -1.5}
                                {type: 'max', name: '最大值'},
                                {type: 'min', name: '最小值'}
                            ]
                        },
                        markLine: {
                            data: [
                                {type: 'average', name: '平均值'},

                            ]
                        }
                    }
                ]
            };
            option1 = {
                title: {
                    text: data['web']+'爬取数据比例',
                    x: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: ['主题', '评论', '作者']
                },
                series: [
                    {
                        name: '比例',
                        type: 'pie',
                        radius: '70%',
                        center: ['50%', '60%'],
                        data: [
                            {value: data['sum'][0], name: '主题'},
                            {value: data['sum'][1], name: '评论'},
                            {value: data['sum'][2], name: '作者'},

                        ],
                        itemStyle: {
                            emphasis: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            };
            layer.msg(2)
            var myChart2 = echarts.init(document.getElementById('linenum'));
            myChart2.setOption(option, true);
            layer.msg(1)

            layer.msg(111)
            var myChart3 = echarts.init(document.getElementById('pienum'));
            myChart3.setOption(option1, true);
        },
        error: function (data) {
            layer.msg('获取数据错误')
        }
    })
}




