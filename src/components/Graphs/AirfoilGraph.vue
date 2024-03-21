<script setup>
  import {
    Chart as ChartJS,
    Tooltip,
    Legend,
    PointElement,
    LineElement,
    LinearScale,
    Filler
  } from 'chart.js';
  import dragData from 'chartjs-plugin-dragdata';
  import { Scatter } from 'vue-chartjs';
  import { ref, onMounted } from "vue";

  const myData = ref({});
  myData.value = {
  
    datasets: [{ data: [{x:0, y: 0},
                              {x:1, y: 1},
                              {x:2, y: 2},
                              {x:3, y: 3},] }],
  };
  
  var myOptions = {
    aspectRatio: 8,
    showLegend: false,
    pointRadius: 8,
    showLine: true,
    pointBackgroundColor: 'rgba(1, 0, 0, 1)',
    autosize: true,
    responsive: true,
    
    xaxis: {
        scaleanchor: "y",
        scaleratio: 1,
        fixedrange: true,
    },
    yaxis: {
        fixedrange: true,
    },
    plugins: {
      dragData: {
        round: 10,
        dragX: true,
        showTooltip: true,
        onDragStart: function (e, element) {},
        onDrag: function (e, datasetIndex, index, value) {},
        onDragEnd: function (e, datasetIndex, index, value) {},
      },
    },
    animation: {
      onComplete: function() {
      }
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

  const myChart = ref(null);

  onMounted(() => {
  })

  function submit(){
    const nextData = {
      datasets: [{ data: [{x:1, y: -5},
                          {x:2, y: -3},
                          {x:3, y: 1},
                          {x:4, y: 4},
                          {x:5, y: 10}] }],
    };

    myData.value = nextData;
  }

</script>
  
<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <h2>Airfoil Plot</h2>
        <Scatter :data="myData" :options="myOptions"/>
        {{ myData }}
        <v-btn ref="doge" @click="submit" color="primary">Change</v-btn>
      </v-card>
    </v-responsive>
  </v-container>
</template>
