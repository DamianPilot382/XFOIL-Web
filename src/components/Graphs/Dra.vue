<template>
    <Scatter :data="data" :options="options" />
    {{ data }}
  </template>
  
  <script lang="ts">
  import {
    Chart as ChartJS,
    Filler,
    Legend,
    LinearScale,
    LineElement,
    PointElement,
    Tooltip,
  } from 'chart.js';
  import dragData from 'chartjs-plugin-dragdata';
  import { Scatter } from 'vue-chartjs';
  
  const data = {
    datasets: [{ data: [
                    {x:0, y: 0},
                    {x:1, y: 1},
                    {x:2, y: 2},
                    {x:3, y: 3}]
              }]
  };
  
  const options = {
    plugins: {
      dragData: {
        round: 10,
        dragX: true,
        showTooltip: true,
        onDragStart: function (e, element) {console.log('drag start', element);},
        onDrag: function (e, datasetIndex, index, value) {console.log('onDrag');},
        onDragEnd: function (e, datasetIndex, index, value) {console.log('onDragEnd');},
      },
    },
  };
  
  ChartJS.register(
    LinearScale,
    PointElement,
    LineElement,
    Filler,
    Tooltip,
    dragData,
    Legend
  );
  
  export default {
    name: 'App',
    components: {
      Scatter,
    },
    data() {
      return {
        data,
        options,
      };
    },
  };
  </script>
  
  <style></style>
  