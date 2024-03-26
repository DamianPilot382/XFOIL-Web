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
import { useAirfoilDataStore } from "../../stores/airfoilData.js";

var airfoilData = useAirfoilDataStore().airfoilData;

airfoilData.value = { 
  datasets: [{
    data: [ {x: 1.000000, y: -0.000000},
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
            {x: 1.000000, y:  0.000000} ]}]};

var config = {
  aspectRatio: 8,
  pointRadius: 6,
  showLine: true,
  pointBackgroundColor: 'rgba(1, 0, 0, 1)',
  autosize: true,
  responsive: true,
  scales: {
    y: {
      min: -0.13,
      max: 0.13
    }
  },
  xaxis: {
      scaleanchor: "y",
      scaleratio: 1,
  },
  yaxis: {
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
    legend: {
      display: false,
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

</script>
  
<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">

        <h2>Airfoil Plot</h2>

        <Scatter :data="airfoilData.value" :options="config"/>
        
      </v-card>
    </v-responsive>
  </v-container>
</template>
