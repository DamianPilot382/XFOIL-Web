<template>
    <div>
      <canvas id="chart"></canvas>
    </div>
  </template>
  <script>
  import { Chart, registerables } from 'chart.js'
  // load the options file externally for better readability of the component.
  // In the chartOptions object, make sure to add "dragData: true" etc.
  import chartOptions from '~/assets/js/labour.js'
  import 'chartjs-plugin-dragdata'
  
  export default {
    data() {
      return {
        chartOptions
      }
    },
    mounted() {
      Chart.register(...registerables)
      this.createChart('chart', this.chartOptions)
    },
    methods: {
      createChart(chartId, chartData) {
        const ctx = document.getElementById(chartId)
        const myChart = new Chart(ctx, {
          type: chartData.type,
          data: chartData.data,
          options: chartData.options,
        })
      }
    }
  }
  </script>