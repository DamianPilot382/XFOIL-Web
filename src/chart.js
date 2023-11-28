import Chart from 'chart.js/auto'

d3.csv('https://s3-us-west-2.amazonaws.com/s.cdpn.io/2814973/atp_wta.csv').then(makeChart);

function makeChart(players) {
    // players is an array of objects where each object represents a player
    console.log("HERE");

    var playerLabels = players.map(function (d) { return d.Name });
    var weeksData = players.map(function (d) { return d.Weeks });


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
}