import Chart from 'chart.js/auto'


var chart = new Chart(ctx, {
    type: 'scatter',
    data: {
        datasets: [{
            data: [{
                x: 1,
                y: 1
            }, {
                x: 3,
                y: 7
            }, {
                x: 6,
                y: 5
            }, { // add same data as the first one, to draw the closing line
                x: 1,
                y: 1
            }],
            borderColor: 'black',
            borderWidth: 1,
            pointBackgroundColor: ['#000'],
            pointBorderColor: ['#000'],
            pointRadius: 5,
            pointHoverRadius: 5,
            fill: false,
            tension: 0,
            showLine: true
        }, {
            data: [{
                x: 3.5,
                y: 4.5
            }],
            pointBackgroundColor: 'orange',
            pointBorderColor: 'darkorange',
            pointRadius: 10,
            pointHoverRadius: 10
        }]
    },
    options: {
        legend: false,
        tooltips: false,
        scales: {
            xAxes: [{
                ticks: {
                    min: 0,
                    max: 10
                },
                gridLines: {
                    color: '#888',
                    drawOnChartArea: false
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 8,
                    padding: 10
                },
                gridLines: {
                    color: '#888',
                    drawOnChartArea: false
                }
            }]
        }
    }
});