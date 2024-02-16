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

  export default {
    name: 'ScatterShart',
    components: { Scatter },
    data() {
      return {

        chartData: {
          datasets: [{
            data: [ {x: -2,y: 4},
                    {x: -1,y: 1} ]
            }],
        },
        chartOptions: {
          responsive: true
        }

      }
    }
  }
  </script>