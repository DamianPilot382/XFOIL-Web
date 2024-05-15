<script setup>
import { ref } from "vue";
import axios from "axios";
import { useAirfoilDataStore } from "/src/stores/airfoilData.js";
import { addChartHeaders } from "/public/utils/airfoilDataConvert.js";

const airfoilData = useAirfoilDataStore().airfoilData;

// NACA 4-Series Airfoil Inputs
const maxCamber = ref(2);
const maxCamberLoc = ref(4);
const maxThickness = ref(12);

// Number of points to generate
const numPoints = ref(20);

function getAirfoilName(){
  var airfoilName = "NACA "+maxCamber.value+maxCamberLoc.value;

  if(maxThickness.value < 10)
    airfoilName += "0"+maxThickness.value;
  else
    airfoilName += maxThickness.value;
  return airfoilName;

}

async function submit() {

  if(isNaN(parseInt(maxCamber.value)) || isNaN(parseInt(maxCamberLoc.value)) 
  || isNaN(parseInt(maxThickness.value)) || isNaN(parseInt(numPoints.value))){
    alert("Error: Invalid input");
    return;
  }

  // PROD OR DEV LINKS
  var requestURL = "https://1cstgscusd.execute-api.us-west-1.amazonaws.com/Prod/NACA4Airfoil";
  // var requestURL = "http://127.0.0.1:3000/NACA4Airfoil";

  await axios
    .post(requestURL, {
      maxCamber: parseInt(maxCamber.value),
      maxCamberLoc: parseInt(maxCamberLoc.value),
      maxThickness: parseInt(maxThickness.value),
      numPoints: parseInt(numPoints.value),
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
