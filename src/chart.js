import Chart from 'chart.js/auto'
import * as fs from 'fs';



let csv = fs.readFileSync("f.csv", "utf8");
let data = d3.csvParse(csv);

var playerLabels = data.map(function (d) { return d.Name });
var weeksData = data.map(function (d) { return d.Weeks });


var chart = new Chart('chart', {
    type: 'bar',
    data: {
        labels: playerLabels,
        datasets: [
            {
                data: weeksData
            }
        ]
    }
});