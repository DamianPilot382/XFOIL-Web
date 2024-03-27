<script setup>
import { ref } from "vue";
import axios from "axios";
import { useAirfoilDataStore } from "../../stores/airfoilData.js";


const inputFile = ref(null);
const airfoilData = useAirfoilDataStore().airfoilData;

const submit = () => {
  
  if (inputFile.value === null) {
    // TODO Warn user that a file must be selected
    console.log("No file selected");
    return;
  }

  var fileName = inputFile.value[0].name.split('.');
  //var name = fileName[0]; // TODO Do something with name
  var extension = fileName[1];

  // TODO Implement other file types
  if(extension != "csv" && extension != "dat"){
    // TODO Warn user that the file must be a .csv or .dat file
    console.log("Invalid file type");
    return;
  }

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

    console.log(data);

    axios
      .post("http://localhost:5000/InputFile", {
        data: data,
      })
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  reader.readAsText(inputFile.value[0]);
};

defineExpose({ submit });

</script>

<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <h1>Input Panel</h1>
        <v-file-input
          v-model="inputFile"
          label="Airfoil Data File"
          accept=".csv,.dat"
        ></v-file-input>
        <v-divider></v-divider>
        <h4 class="text-center">Sample Input Files</h4>
        <br>
        <v-row>
          <v-col cols="3"></v-col>
          <v-col cols="3">
            <v-btn color="primary" href="/public/sample_files/n0012.csv" target="_blank">CSV</v-btn>
          </v-col>
          <v-col cols="3">
            <v-btn color="primary" href="/public/sample_files/n0012.dat" target="_blank">DAT</v-btn>
          </v-col>
          <v-col cols="3"></v-col>
        </v-row>
        
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
