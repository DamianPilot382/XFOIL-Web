<script setup>
import { ref } from "vue";
import { useAirfoilDataStore } from "/src/stores/airfoilData.js";
import { addChartHeaders } from "/public/utils/airfoilDataConvert.js";


const inputFile = ref(null);
const airfoilData = useAirfoilDataStore().airfoilData;

async function submit(){
  
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

    const regex = /^(-?\d*\.*\d*)[\s,](-?\d*\.*\d*)\s*$/;

    var contents = e.target.result;
    var lines = contents.split("\n");
    for (var i = 0; i < lines.length; i++) {

      const regexMatch = regex.exec(lines[i].trim());

      if(regexMatch == null){
        console.log("invalid: " + lines[i]);
        continue;
      }

      data.push({x: parseFloat(regexMatch[1]), y: parseFloat(regexMatch[2])});

    }

    airfoilData.value = addChartHeaders(data);

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
            <v-btn color="primary" href="/sample_files/n0012.csv" target="_blank">CSV</v-btn>
          </v-col>
          <v-col cols="3">
            <v-btn color="primary" href="/sample_files/n0012.dat" target="_blank">DAT</v-btn>
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
