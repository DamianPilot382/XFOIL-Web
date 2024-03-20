<template>
    <Scatter :data="data" :options="options" ref="myGraph"/>
  </template>
  
<script>
  import {
    Chart as ChartJS,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend
  } from 'chart.js'
  import { Scatter } from 'vue-chartjs'
  import * as chartConfig from './chartConfig'
  import { ref } from 'vue'

  
  ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend)

//   const myGraph = ref(null);
  
  export default {
    // setup(){
    //     const myGraph = ref(null);

    //     return {myGraph}
    // },
    name: 'App',
    components: {
      Scatter
    },
    data() {
      return chartConfig
    },
    mounted() {
      console.log('mounted');
    //   console.log(this.data.datasets[0].data[0]);
    //   this.data.datasets[0].data[0].x = 69;
    //   console.log(this.data.datasets[0].data[0]);

    //   console.log(myGraph);
      

    },
    methods: {
        updateChart(){
            console.log('doge');
            console.log(this.$refs.scatterChart);
            console.log(this.$data._chart);

            this.$refs.scatterChart.update();
        }
    }
  }
</script>
  