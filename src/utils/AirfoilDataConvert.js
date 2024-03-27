// Converts airfoil data from a Chart.js Scatter plot format to a JSON object
function convertChartToJson(airfoilData){
    const xPoints = airfoilData.datasets[0].data.map(point => point.x);
    const yPoints = airfoilData.datasets[0].data.map(point => point.y);

    var ret = {
        x: xPoints,
        y: yPoints        
    };

    return ret;
}

// Converts airfoil data from a JSON object to a Chart.js Scatter plot format
function convertJsonToChart(json){
    var ret = {
        datasets: [{
            data: []
        }]
    };

    for (var i = 0; i < json.x.length; i++){
        ret.datasets[0].data.push({x: json.x[i], y: json.y[i]});
    }

    return ret;
}

export { convertChartToJson, convertJsonToChart };