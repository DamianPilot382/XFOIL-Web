<script setup>
import { Chart, PointElement, LineElement, LinearScale } from 'chart.js';
import dragData from 'chartjs-plugin-dragdata';
import { Scatter } from 'vue-chartjs';
import { useAirfoilDataStore } from "../../stores/airfoilData.js";
import { airfoilTestData } from "../../utils/airfoilTestData.js";

var airfoilData = useAirfoilDataStore().airfoilData;

airfoilData.value = airfoilTestData;

var config = {
  aspectRatio: 6,
  pointRadius: 5,
  showLine: true,
  pointBackgroundColor: 'rgba(0, 0, 0, 1)',
  scales: {
    x: {
      min: -0.01,
      max: 1.01,
    },
    y: {
      min: -0.13,
      max: 0.13,
    }
  },
  xaxis: {
      scaleanchor: "y",
      scaleratio: 1,
  },
  plugins: {
    dragData: {
      round: 10,
      dragX: true,
    },
    legend: {
      display: false,
    },
  }
};

Chart.register(LinearScale, PointElement, LineElement, dragData);

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
