<script setup>
import { ref, computed } from "vue";
import axios from "axios";
import { useAirfoilDataStore } from "../../stores/airfoilData.js";

const v_inf = ref(0);
const aoa = ref(0);
const loading = ref(false);
const info = ref("Enter parameters and click generate to begin");

const airfoilData = useAirfoilDataStore().airfoilData;

const compute = () => {

  console.log("Compute");

  if(v_inf.value === 0) {
    info.value = "Please enter a freestream velocity";
    return;
  }

  loading.value = true;
   
    axios
      .post("http://localhost:5000/compute", {
        airfoilData: JSON.parse(JSON.stringify(airfoilData.value.datasets[0].data)),
        v_inf: v_inf.value,
        aoa: aoa.value,
      })
      .then((res) => {
        console.log(res);
        info.value = res.data.text;
        loading.value = false;

      })
      .catch((err) => {
        loading.value = false;
        console.log(err);
        info.value = "Error: " + err;
      });

};

</script>

<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <h1>Input Panel</h1>
        <v-text-field
          v-model="v_inf"
          label="Freestream Velocity"
          type="number"
        ></v-text-field>
        <v-text-field
          v-model="aoa"
          label="Angle of Attack (deg)"
          type="number"
        ></v-text-field>
        <v-btn @click="compute" color="primary">Generate</v-btn>
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

<style scoped>
.v-divider {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>