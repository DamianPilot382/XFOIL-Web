<template>
  <v-container fill-height fluid>
    <v-responsive class="text-center fill-height">
      <v-card variant="tonal">

        <h1>Airfoil Editor</h1>
        
          <v-row justify="center">
            <v-col cols="12" md="6">

              <!-- Select Input Method -->
              <v-select
                label="Select Input Type"
                :items="['Input File', 'NACA 4 Series Generator', 'From Scratch']"
                variant="solo-filled"
                @update:model-value="getSelectionFromDropdown"
              ></v-select>

              <!-- Input Method -->
              <component :is="inputMethodSelected" ref="inputPanel"
              ></component>

            </v-col>
          </v-row>
        <br>
        <br>
        <v-divider></v-divider>
        <br>
        <v-btn @click="submit" color="primary" v-show="submitBtnEnabled">Generate</v-btn>
      </v-card>
      <br>
      <br>
      <v-card>
        <AirfoilGraph ref="airfoilGraph"/>
      </v-card>
    </v-responsive>
  </v-container>
</template>
  
<script setup>

import FileInputPanel from "./FileInputPanel.vue";
import NACAInputPanel from "./NACAInputPanel.vue";
import { shallowRef, ref } from "vue";
import AirfoilGraph from "../Graphs/AirfoilGraph.vue";


var inputPanel = ref(null);
var inputMethodSelected = shallowRef(null);
var submitBtnEnabled = ref(false);
var airfoilGraph = ref(null);

const getSelectionFromDropdown = (selection) => {

  submitBtnEnabled.value = true;

  if (selection == "Input File") {
    inputMethodSelected.value = FileInputPanel;
    return FileInputPanel;
  } else if (selection == "NACA 4 Series Generator") {
    inputMethodSelected.value = NACAInputPanel;
  } else{
    submitBtnEnabled.value = false;
    inputMethodSelected.value = null;
  }
};

const submit = () => {
  console.log("AirfoilPanel SUBMIT");

  // if(inputMethodSelected.value == null){
  //   console.log("No input panel selected");
  //   return;
  // }

  // airfoilGraph.value.airfoilData = [{x: 1, y: 0},
  //                                   {x: 2, y: 1},];

  // airfoilGraph.value.updateChart();

  inputPanel.value.submit();
  // airfoilGraph.value.doge();
};


</script>
