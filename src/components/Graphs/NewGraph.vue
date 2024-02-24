<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <h2>Airfoil Plot</h2>
        <canvas id="chart"></canvas>
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
    },
    async updateChart(){
      console.log("doChart");
      // console.log(airfoilGraph.value);
      // console.log(airfoilGraph.value.data);
      // airfoilGraph.value.data = [{x: 1, y: 0},
      //                            {x: 2, y: 1},];
      // console.log(airfoilGraph.value.data);

      // airfoilGraph.value.update();
      // airfoilGraph.value.destroy();
      // this.createChart('chart', this)

      // console.log(airfoilGraph.value);

      
      // console.log(airfoilGraph.value.data.datasets[0].data[0]);
      // airfoilGraph.value.data.datasets[0].data[0] = {x: 2, y: 3};

      // console.log(airfoilGraph.value.data.datasets[0].data[0]);

      // airfoilGraph.value.update();


      // const elDoge = {datasets: [{
      //     data: [{x: 1, y: 0},
      //            {x: 2, y: 1},],
      //     dragData: true,
      //   }]};

      // if(airfoilGraph.value != null){
      //   airfoilGraph.value.destroy();
      // }

      // const ctx = document.getElementById('chart')

      // // await this.$nextTick();

      
      // airfoilGraph.value = new Chart(ctx, {
      //   type: this.type,
      //   data: elDoge,
      //   options: this.chartOptions,
      // })

      
      // console.log(airfoilGraph.value.data);

      // airfoilGraph.value.data = {datasets: [{
      //   data: [{x: 1.000000, y: 0.004571},
      //          {x: 0.975680, y:  0},],
      //   dragData: true,
      // }]};

      // console.log(airfoilGraph.value.data);

      airfoilGraph.value.update();
      

    }
  }
}

</script>
