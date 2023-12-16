<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
          <h1>Airfoil</h1>
          airfoil graph 1
        <div v-if="graphsUpdated">
          <h1>Graphs</h1>

          <v-row>
            <v-col cols="12" md="6">
              <v-card>
                <v-card-title>Panel Geometry</v-card-title>
                <v-card-text>
                  <img v-if="useImgs" :src="imgs[0]" alt="panel geometry" />
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="6">
              <v-card>
                <v-card-title>Geometry Points</v-card-title>
                <v-card-text>
                  <img v-if="useImgs" :src="imgs[1]" alt="geometry points" />
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
          <v-row>
          <v-col cols="12" md="6">
            <v-card>
              <v-card-title>Control Points</v-card-title>
              <v-card-text>
                <img v-if="useImgs" :src="imgs[2]" alt="control points" />
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" md="6">
            <v-card>
              <v-card-title>Pressure stuffs</v-card-title>
              <v-card-text>
                <img v-if="useImgs" :src="imgs[3]" alt="pressure stuffs" />
              </v-card-text>
            </v-card>
          </v-col>
          </v-row>
        </div>
      </v-card>
    </v-responsive>
  </v-container>
</template>
  
  <script setup>
// import graph store
import { useGraphsStore } from "../stores/graphs.js";
import { ref, computed } from "vue";

const graphsUpdated = computed(() => {
  const graphsStore = useGraphsStore();
  return graphsStore.panelGeometry.data !== null;
});

const useImgs = computed(() => {
  const graphsStore = useGraphsStore();
  return graphsStore.mode == "img";
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

const submit = () => {
  // get graphs store
  const graphsStore = useGraphsStore();
  // get graphs
  console.log(graphsStore);
};
</script>
  
  <style scoped>
img {
  width: 100%;
}
</style>