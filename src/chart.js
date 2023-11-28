import Chart from 'chart.js/auto'
import * as fs from 'fs';



var airfoil = "NACA 0012";

let csv = fs.readFileSync('NACA0012.csv', "utf8");


let data = d3.csvParse(csv);

var xCoord = data.map(function (d) { return d.x });
var yCoord = data.map(function (d) { return d.y });


var chart = new Chart('chart', {
    type: 'scatter',
    data: {
        labels:xCoord,
        datasets: [{
            label: airfoil,
            data: yCoord,
            borderColor: 'black',
            borderWidth: 1,
            pointBackgroundColor: ['#000'],
            pointBorderColor: ['#000'],
            pointRadius: 3,
            pointHoverRadius: 5,
            showLine: true,
            fill:true,
        }]
    },
    options: {
        responsive:true,
        aspectRatio:1,
        legend: false,
        tooltips: false,
        scales: {

            y:{
                min: -1,
                max: 1
            }
        }
    }
});