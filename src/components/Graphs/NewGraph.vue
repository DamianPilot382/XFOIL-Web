<template>
    <Scatter
      id="my-chart-id"
      :options="chartOptions"
      :data="chartData"
    />
  </template>
  
  <script>
  import { Scatter } from 'vue-chartjs'
  import { Chart as ChartJS, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js'
  
  ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend)

  var info =   [{x: 1.000000, y: -0.000000},
               {x: 0.975680, y:  0.004571},
               {x: 0.905027, y:  0.017080},
               {x: 0.794797, y:  0.034501},
               {x: 0.655622, y:  0.053079},
               {x: 0.501044, y:  0.068901},
               {x: 0.346213, y:  0.078064},
               {x: 0.206410, y:  0.077433},
               {x: 0.094661, y:  0.066001},
               {x: 0.016983, y:  0.033378},
               {x: 0.000000, y:  0.000000},
               {x: 0.031960, y: -0.016196},
               {x: 0.096322, y: -0.026082},
               {x: 0.205805, y: -0.037989},
               {x: 0.344770, y: -0.041040},
               {x: 0.498956, y: -0.036802},
               {x: 0.653395, y: -0.028263},
               {x: 0.792988, y: -0.018278},
               {x: 0.903990, y: -0.009042},
               {x: 0.975377, y: -0.002425},
               {x: 1.000000, y:  0.000000} ];

  export default {
    name: 'ScatterShart',
    components: { Scatter },
    data() {
      return {
        chartData: {
          datasets: [{
            data: info,
          }],
        },
        chartOptions: {
          aspectRatio: 8,
          showLegend: false,
          pointRadius: 3,
          showLine: true,
          pointBackgroundColor: 'rgba(0, 0, 0, 1)',
          autosize: true,
          autosize: true,
          responsive: true,
          
          // maintainAspectRatio: false,
          xaxis: {
              scaleanchor: "y",
              scaleratio: 1,
              fixedrange: true,
          },
          yaxis: {
              fixedrange: true,
          },
          plugins: {
            legend: {
              display: false,
            }
          }
        }

      }
    }
  }
  </script>