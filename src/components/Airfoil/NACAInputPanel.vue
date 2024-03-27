<script setup>
import { ref } from "vue";
import axios from "axios";
import { useAirfoilDataStore } from "../../stores/airfoilData.js";
import { addChartHeaders } from "../../utils/airfoilDataConvert.js";

const airfoilData = useAirfoilDataStore().airfoilData;

// NACA 4-Series Airfoil Inputs
const maxCamber = ref(0);
const maxCamberLoc = ref(0);
const maxThickness = ref(0);

// Number of points to generate
const numPoints = ref(0);

function getAirfoilName(){
  var airfoilName = "NACA "+maxCamber.value+maxCamberLoc.value;

  if(maxThickness.value < 10)
    airfoilName += "0"+maxThickness.value;
  else
    airfoilName += maxThickness.value;
  return airfoilName;

}

const submit = () => {

  axios
    .post("http://localhost:5000/NACA4Airfoil", {
      maxCamber: maxCamber.value,
      maxCamberLoc: maxCamberLoc.value,
      maxThickness: maxThickness.value,
      numPoints: numPoints.value,
    })
    .then((res) => {

      airfoilData.value = addChartHeaders(res.data);

    })
    .catch((err) => {
      console.log(err);
      info.value = "Error: " + err;
    });
};

defineExpose({ submit });
</script>

<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <h1>NACA 4-Series Generator</h1>
        <v-text-field
          v-model="maxCamber"
          label="Maximum Camber (1st digit)"
          type="number"
        ></v-text-field>
        <v-text-field
          v-model="maxCamberLoc"
          label="Maximum Camber Location (2nd digit)"
          type="number"
        ></v-text-field>
        <v-text-field
          v-model="maxThickness"
          label="Maximum Thickness (3rd and 4th digits)"
          type="number"
        ></v-text-field>
        <v-text-field
          v-model="numPoints"
          label="Number of Points"
          type="number"
        ></v-text-field>
        <h2 v-html="getAirfoilName()"></h2>
      </v-card>
    </v-responsive>
  </v-container>
</template>

<style scoped>
.v-divider {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
