<script setup>
import { useGraphsStore } from "../../stores/graphs.js";
import { ref, computed } from "vue";
import { useAirfoilDataStore } from "../../stores/airfoilData.js";
import { addChartHeaders } from "../../utils/airfoilDataConvert.js";

const graphsUpdated = computed(() => {
const graphsStore = useGraphsStore();
  return graphsStore.panelGeometry.data !== null;
});

// computed graphs from store
const imgs = computed(() => {
const graphsStore = useGraphsStore();
var srcs = [];
// base64 encoded images for src tagh
srcs.push("data:image/png;base64," + graphsStore.panelGeometry.img);
srcs.push("data:image/png;base64," + graphsStore.geom_pts.img);
srcs.push("data:image/png;base64," + graphsStore.control_pts.img);
srcs.push("data:image/png;base64," + graphsStore.pressure.img);


return srcs;
});


const displayGraphs = () => {
}

defineExpose({ displayGraphs });
</script>

<template>
    <v-container class="fill-height">
      <v-responsive class="align-center text-center fill-height">
        <v-card variant="tonal">

          <div>
            <h1>Graphs</h1>
  
            <v-row>
              <v-col cols="12" md="6">
                <v-card>
                  <v-card-title>Panel Geometry</v-card-title>
                  <v-card-text>
                    <img :src="imgs[0]" alt="panel geometry" />
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col cols="12" md="6">
                <v-card>
                  <v-card-title>Geometry Points</v-card-title>
                  <v-card-text>
                    <img :src="imgs[1]" alt="geometry points" />
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
            <v-col cols="12" md="6">
              <v-card>
                <v-card-title>Cp vectors at control points</v-card-title>
                <v-card-text>
                  <img :src="imgs[2]" alt="control points" />
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="6">
              <v-card>
                <v-card-title>Pressure Coefficient</v-card-title>
                <v-card-text>
                  <img :src="imgs[3]" alt="pressure stuffs" />
                </v-card-text>
              </v-card>
            </v-col>
            </v-row>
          </div>
        </v-card>
      </v-responsive>
    </v-container>
  </template>
    
<style scoped>
img {
    width: 100%;
}
</style>