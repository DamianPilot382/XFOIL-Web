<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <h2>Airfoil Plot</h2>
        <canvas id="chart" ref="airfoilGraph"></canvas>
      </v-card>
    </v-responsive>
  </v-container>
</template>


<script>
// import { Chart, registerables } from 'chart.js'
// import 'chartjs-plugin-dragdata'


import { Chart, registerables } from 'chart.js/auto'
import { ref, defineExpose } from 'vue'
import { Scatter } from 'vue-chartjs'
import 'chartjs-plugin-dragdata'


const airfoilData = ref(0);
airfoilData.value = [{x: 1.000000, y: -0.000000},
                 {x: 0.975680, y:  0.004571},];

const airfoilGraph = ref(null);

export default {
  data() {
    return {
      airfoilData,
      airfoilGraph,
      type: 'scatter',
      chartData: {
        datasets: [{
          data: [{x: 1.000000, y: -0.000000},
                 {x: 0.975680, y:  0.004571},],
          dragData: true,
        }],
      },
      chartOptions: {
        aspectRatio: 8,
        showLegend: false,
        pointRadius: 8,
        showLine: true,
        pointBackgroundColor: 'rgba(1, 0, 0, 1)',
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
          dragData:{
            onDragStart: function(e) {
              console.log(e);
            },
            onDrag: function(e, datasetIndex, index, value) {
              console.log(datasetIndex, index, value);
            },
            onDragEnd: function(e, datasetIndex, index, value) {
              console.log(datasetIndex, index, value);
            }
          },
          legend: {
            display: false,
          }
        },
      }
    }
  },
  mounted() {
    // Chart.plugins.register('dragData', 'chartjs-plugin-dragdata')
    Chart.register(...registerables)
    this.createChart('chart', this)

  },
  methods: {
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId)
      
      airfoilGraph.value = new Chart(ctx, {
        type: chartData.type,
        data: chartData.chartData,
        options: chartData.chartOptions,
      })

      // console.log(ctx);
    },
    waitForElement(selector, callback) {
      if (document.querySelector(selector)) {
        callback();
      } else {
        setTimeout(() => waitForElement(selector, callback), 500);
      }
    },
    async updateChart(){
      console.log("doChart");
      

      if(airfoilGraph.value != null){
        airfoilGraph.value.destroy();
      }
      var ctx = null;
      ctx = document.getElementById('chart');
      
      console.log("bonk")
      this.waitForElement("#chart", () => {
        // Element-specific code here
        console.log("waiting")
        ctx = document.getElementById('chart');
      });
      console.log("fewa")

      console.log(ctx);

      if(ctx != null){
        console.log("ctx not null")
      }
    },




  }
}

</script>
