<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <h1>Input Panel</h1>
        <v-file-input
          v-model="csvFile"
          label="Airfoil Data File"
          accept=".csv,.dat"
        ></v-file-input>
        
      </v-card>
    </v-responsive>
  </v-container>
</template>
  
<script setup>
import { ref, computed } from "vue";
import axios from "axios";

const csvFile = ref(null);

const submit = () => {
  console.log("File Input SUBMIT");
  if (csvFile.value === null) {
    console.log("No file selected");
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

    axios
      .post("http://localhost:5000/InputFile", {
        data: data,
      })
      .then((res) => {
        console.log("SUCCESS");
        console.log(res);
      })
      .catch((err) => {
        console.log("ERROR");
        console.log(err);
      });
  };

  reader.readAsText(csvFile.value[0]);
};

defineExpose({ submit });

</script>

<style scoped>
.v-divider {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>