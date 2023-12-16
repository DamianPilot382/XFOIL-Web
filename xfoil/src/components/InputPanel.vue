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
          label="Angle of Attack"
          type="number"
        ></v-text-field>
        <v-file-input
          v-model="csvFile"
          label="Airfoil Data File"
          accept=".csv,.dat"
        ></v-file-input>
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
const csvFile = ref(null);
const v_inf = ref(0);
const aoa = ref(0);
const loading = ref(false);
const info = ref("Enter parameters and click generate to begin");
const imgsrc = ref("");
const submit = () => {
  if (csvFile.value === null) {
    info.value = "Please select an airfoil data file";
    return;
  }
  // if (v_inf.value === 0) {
  //   info.value = "Please enter a freestream velocity";
  //   return;
  // }
  // if (aoa.value === 0) {
  //   info.value = "Please enter an angle of attack";
  //   return;
  // }
  var reader = new FileReader();
  var data = [];
  reader.onload = function (e) {
    var contents = e.target.result;
    var lines = contents.split("\n");
    for (var i = 0; i < lines.length; i++) {
      var line = lines[i].split(",");
      // to remove the last \r
      line[1] = line[1].replace("\r", "");
      // to float
      line[0] = parseFloat(line[0]);
      line[1] = parseFloat(line[1]);
      data.push(line);
    }

    loading.value = true;
    axios
      .post("http://localhost:5000/compute", {
        data: data,
        v_inf: v_inf.value,
        aoa: aoa.value,
      })
      .then((res) => {
        console.log(res);
        info.value = res.data.text;
        loading.value = false;

        // update graphs store
        const graphsStore = useGraphsStore();
        graphsStore.panelGeometry.data = res.data.panel_geometry.data;
        graphsStore.panelGeometry.img = res.data.panel_geometry.pic;
        graphsStore.geom_pts.data = res.data.geom_pts.data;
        graphsStore.geom_pts.img = res.data.geom_pts.pic;
        graphsStore.control_pts.data = res.data.control_pts.data;
        graphsStore.control_pts.img = res.data.control_pts.pic;
        graphsStore.pressure.data = res.data.pressure.data;
        graphsStore.pressure.img = res.data.pressure.pic;
      })
      .catch((err) => {
        console.log(err);
        info.value = "Error: " + err;
      });
  };

  reader.readAsText(csvFile.value[0]);
};
</script>

<style scoped>
.v-divider {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>