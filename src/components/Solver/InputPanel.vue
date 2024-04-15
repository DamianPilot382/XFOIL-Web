<script setup>
import { ref, computed } from "vue";
import axios from "axios";
import { useAirfoilDataStore } from "@/stores/airfoilData.js";
import { useGraphsStore } from "@/stores/graphs";
import { useResultsGraphsStore } from "@/stores/resultsGraphs.js";

const v_inf = ref(1);
const aoa = ref(5);
const loading = ref(false);
const info = ref("Enter parameters and click generate to begin");

const airfoilData = useAirfoilDataStore().airfoilData;

const graphsStore = useGraphsStore();
const resultsGraphsStore = useResultsGraphsStore();

const compute = () => {

  if(v_inf.value === 0) {
    info.value = "Please enter a freestream velocity";
    return;
  }

  loading.value = true;
   
    axios
      .post("http://localhost:5000/compute", {
        airfoilData: JSON.stringify(airfoilData.value.datasets[0].data),
        v_inf: v_inf.value,
        aoa: aoa.value,
      })
      .then((res) => {


        // Store Image Data
        graphsStore.panelGeometry.data = res.data.panel_geometry.data;
        graphsStore.panelGeometry.fillData = res.data.panel_geometry.fillData;
        graphsStore.panelGeometry.img = res.data.panel_geometry.pic;
        graphsStore.geom_pts.data = res.data.geom_pts.data;
        graphsStore.geom_pts.img = res.data.geom_pts.pic;
        graphsStore.control_pts.data = res.data.control_pts.data;
        graphsStore.control_pts.img = res.data.control_pts.pic;
        graphsStore.pressure.data = res.data.pressure.data;
        graphsStore.pressure.img = res.data.pressure.pic;

        //Store Graph Data
        resultsGraphsStore.pressureCoeff = res.data.pressureCoeff;

        console.log(resultsGraphsStore.pressureCoeff);




        graphsStore.renderImgs = true;

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