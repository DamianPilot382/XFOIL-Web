<script setup>
import { ref } from "vue";
import axios from "axios";
const maxCamber = ref(0);
const maxCamberLoc = ref(0);
const maxThickness = ref(0);
const numPoints = ref(0);
const loading = ref(false);
const info = ref("Enter parameters and click generate to begin");
const imgsrc = ref("");
const submit = () => {

  loading.value = true;

  axios
    .post("http://localhost:5000/NACA4Airfoil", {
      maxCamber: maxCamber.value,
      maxCamberLoc: maxCamberLoc.value,
      maxThickness: maxThickness.value,
      numPoints: numPoints.value,
    })
    .then((res) => {
      console.log(res);
      info.value = "Done!";
      loading.value = false;

      const csv = res.data;
      const link = document.createElement("a");
      link.target = "_blank";
      link.href = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
      link.download = "NACA"+maxCamber.value+maxCamberLoc.value+maxThickness.value+".csv";
      link.click();


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
        <h2>NACA {{ maxCamber }}{{ maxCamberLoc }}{{ maxThickness }}</h2>
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
