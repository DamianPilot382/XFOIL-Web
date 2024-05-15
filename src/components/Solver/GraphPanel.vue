<script setup>
import { useGraphsStore } from "/src/stores/graphs.js";
import { useResultsGraphsStore } from "/src/stores/resultsGraphs.js";
import { computed } from "vue";

const graphsStore = useGraphsStore();
const resultsGraphsStore = useResultsGraphsStore();

// computed graphs from store
const imgs = computed(() => {

  var srcs = [];

  // base64 encoded images for src tag
  srcs.push("data:image/png;base64," + graphsStore.panelGeometry.img);
  srcs.push("data:image/png;base64," + graphsStore.geom_pts.img);
  srcs.push("data:image/png;base64," + graphsStore.control_pts.img);
  srcs.push("data:image/png;base64," + graphsStore.pressure.img);

  return srcs;
});

function getResults() {

  const decimalPlaces = 4;

  var Cl_SPVP = resultsGraphsStore.Cl_SPVP.toFixed(decimalPlaces);
  var Cl_KJ = resultsGraphsStore.Cl_KJ.toFixed(decimalPlaces);
  var Cm_SPVP = resultsGraphsStore.Cm_SPVP.toFixed(decimalPlaces);

  return "<h2>Lift Coefficient (CL)</h2>" + 
         "<h3>SPVP method: " + Cl_SPVP + "</h3>" +
         "<h3>Kutta-Joukowski: " + Cl_KJ + "</h3>" +
         "<h2>Moment Coefficient (CM)</h2>" +
         "<h3>SPVP method: " + Cm_SPVP + "</h3>";

}


</script>

<template>
  <v-container class="fill-height" v-if="graphsStore.renderImgs">

    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <div>
          <h1>Results</h1>
        </div>
        <div v-html="getResults()"></div>
      </v-card>

    </v-responsive>

    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">

        <div>
          <h1>Graphs</h1>
          <!-- <PressureCoeffGraph /> -->
          <v-row>
            <v-col cols="12" md="12">
              <v-card>
                <v-card-title>Panel Geometry</v-card-title>
                <v-card-text>
                  <img :src="imgs[0]" alt="panel geometry" />
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="12">
              <v-card>
                <v-card-title>Geometry Points</v-card-title>
                <v-card-text>
                  <img :src="imgs[1]" alt="geometry points" />
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
          <v-row>
          <v-col cols="12" md="12">
            <v-card>
              <v-card-title>Cp vectors at control points</v-card-title>
              <v-card-text>
                <img :src="imgs[2]" alt="control points" />
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" md="12">
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