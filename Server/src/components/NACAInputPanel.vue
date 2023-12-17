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
        <v-btn @click="submit" color="primary">Generate</v-btn>
        <!-- seperator bar -->
        <v-divider></v-divider>
        <!-- info panel -->
        <v-card>
          <v-card-title>Info</v-card-title>
          <v-card-text>
            <v-progress-circular v-if="loading" indeterminate color="primary">
            </v-progress-circular>
            <p v-else>{{ info }}</p>
          </v-card-text>
        </v-card>
      </v-card>
    </v-responsive>
  </v-container>
</template>
  
  <script setup>
import { ref } from "vue";
import { useGraphsStore } from "../stores/graphs.js";
import axios from "axios";
const maxCamber = ref(0);
const maxCamberLoc = ref(0);
const maxThickness = ref(0);
const loading = ref(false);
const info = ref("Enter parameters and click generate to begin");
const imgsrc = ref("");
const submit = () => {

  loading.value = true;

  axios
    .post("http://localhost:5000/nacaAirfoil", {
      maxCamber: maxCamber.value,
      maxCamberLoc: maxCamberLoc.value,
      maxThickness: maxThickness.value,
    })
    .then((res) => {
      console.log(res);
      info.value = res.data.text;
      loading.value = false;
      
    })
    .catch((err) => {
      console.log(err);
      info.value = "Error: " + err;
    });
};

</script>

<style scoped>
.v-divider {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>