// Setting the configuration items for the chart
var confGauge = {
    series: [
      {
        type: 'gauge',
        center: ['50%', '75%'],
        startAngle: 200,
        endAngle: -20,
        min: 0,
        max: 100,
        splitNumber: 10,
        itemStyle: {
          color: '#000050'
        },
        progress: {
          show: true,
          width: 30
        },
        pointer: {
          show: false
        },
        axisLine: {
          lineStyle: {
            width: 30
          }
        },
        axisTick: {
          distance: -45,
          splitNumber: 5,
          lineStyle: {
            width: 2,
            color: '#000036'
          }
        },
        splitLine: {
          distance: -52,
          length: 14,
          lineStyle: {
            width: 3,
            color: '#000036'
          }
        },
        axisLabel: {
          distance: -20,
          color: '#000036',
          fontSize: 20
        },
        anchor: {
          show: false
        },
        title: {
          show: false
        },
        detail: {
          valueAnimation: true,
          width: '60%',
          lineHeight: 40,
          borderRadius: 8,
          offsetCenter: [0, '-15%'],
          fontSize: '1.4rem',
          fontWeight: 'bolder',
          formatter: '{value} %',
          color: 'inherit'
        },
        data: [
          {
            value: 20
          }
        ]
      },
      {
        type: 'gauge',
        center: ['50%', '75%'],
        startAngle: 200,
        endAngle: -20,
        min: 0,
        max: 100,
        itemStyle: {
          color: '#000036'
        },
        progress: {
          show: true,
          width: 8
        },
        pointer: {
          show: false
        },
        axisLine: {
          show: false
        },
        axisTick: {
          show: false
        },
        splitLine: {
          show: false
        },
        axisLabel: {
          show: false
        },
        detail: {
          show: false
        },
        data: [
          {
            value: 20
          }
        ]
      }
    ]
};

var confPie = {
    legend: {
      top: '15%',
      left: 'center'
    },
    series: [
      {
        top: '15%',
        name: 'Disk',
        type: 'pie',
        color: ['#000036', '#E6EBF8'],
        radius: ['50%', '75%'],
        avoidLabelOverlap: false,
        label: {
            show: false,
            position: 'center',
            formatter(param) {
                // correct the percentage
                return param.name + ' (' + param.percent + '%)';
            }
        },
        emphasis: {
          label: {
            show: true,
            fontSize: '1.4rem',
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
      }
    ]
};

// Initialize the chart CPU
var cpuChart = echarts.init(document.getElementById('main_cpu'));
var infoChartCpu = 0;
setInterval(function () {
    $.ajax({
        url: "get_info_cpu",
        success: function(data) {
            infoChartCpu = parseInt(data);
        },
        error: function() {
            infoChartCpu = 0;
        }
    });
    cpuChart.setOption({
        title: {
            text: 'CPU',
            top: '5%',
            left: 'center'
        },
        series: [
            {
                data: [{
                    value: infoChartCpu
                }]
            },
            {
                data: [{
                    value: infoChartCpu
                }]
            }
        ]
    });
}, 1000);

// Display the chart using the configuration items and data just specified.
cpuChart.setOption(confGauge);

window.addEventListener('resize', function () {
    cpuChart.resize();
})

// Initialize the chart Memory
var memoryChart = echarts.init(document.getElementById('main_memory'));
var infoChartMemory = 0;
setInterval(function () {
    $.ajax({
        url: "get_info_memory",
        success: function(data) {
            infoChartMemory = parseInt(data);
        },
        error: function() {
            infoChartMemory = 0;
        }
    });
    memoryChart.setOption({
        title: {
            text: 'Memória',
            top: '5%',
            left: 'center'
        },
        series: [
            {
                data: [{
                    value: infoChartMemory
                }]
            },
            {
                data: [{
                    value: infoChartMemory
                }]
            }
        ]
    });
}, 1000);

// Display the chart using the configuration items and data just specified.
memoryChart.setOption(confGauge);

window.addEventListener('resize', function () {
    memoryChart.resize();
})

// Initialize the chart Disk
var diskChart = echarts.init(document.getElementById('main_disk'));

setInterval(function () {
    $.ajax({
        url: "get_info_disk",
        success: function(data) {            
            infoChartDisk = parseInt(data);
            infoChartFreeDisk = 100 - infoChartDisk;
        },
        error: function() {
            infoChartDisk = 0;
        }
    });
    diskChart.setOption({
        title: {
            text: 'Disco',
            top: '5%',
            left: 'center'
        },
      series: [
        {
          data: [
            { value: infoChartDisk, name: 'Usage' },
            { value: infoChartFreeDisk, name: 'Free' },
          ]
        }
      ]
    });
}, 1000);

// Display the chart using the configuration items and data just specified.
diskChart.setOption(confPie);

window.addEventListener('resize', function () {
    diskChart.resize();
})