<script setup>

import FileInputPanel from "./FileInputPanel.vue";
import NACAInputPanel from "./NACAInputPanel.vue";
import { shallowRef, ref } from "vue";
import AirfoilGraph from "./AirfoilGraph.vue";

// Input type currently being used
var inputPanel = ref(null);

// Input type currently selected from dropdown
var inputMethodSelected = shallowRef(null);

// Whether the submit button is enabled
var submitBtnEnabled = ref(false);

var showGraph = ref(true); // TODO Implement hiding when not populated

// Airfoil graph component
var airfoilGraph = ref(null);

//Loading wheel after generate button is clicked
var loading = ref(false);

// Get the selected input method from the dropdown
const getSelectionFromDropdown = (selection) => {

  // Enable submit button
  submitBtnEnabled.value = true;

  // Set input to Input File
  if (selection == "Input File") {

    inputMethodSelected.value = FileInputPanel;
    return FileInputPanel;

  // Set input to NACA 4 Series Generator
  } else if (selection == "NACA 4 Series Generator") {

    inputMethodSelected.value = NACAInputPanel;
    
  // Else, no input method selected
  } else{

    // Disable submit button and deselect input method
    submitBtnEnabled.value = false;
    inputMethodSelected.value = null;
  }
};

// Submit the Airfoil to Server
async function submit() {

  // Disable submit button and enable loading wheel
  submitBtnEnabled.value = false;
  loading.value = true;

  // Call the submit button for the selected input method
  await inputPanel.value.submit();

  // Enable submit button and Disable loading wheel
  submitBtnEnabled.value = true;
  loading.value = false;

};

</script>

<template>
  <v-container fill-height fluid>
    <v-responsive class="text-center fill-height">

      <!-- === Airfoil Input Type Dropdown === -->
      <v-card variant="tonal">

        <h1>Airfoil Editor</h1>
        
          <v-row justify="center">
            <v-col cols="12" md="6">

              <!-- Select Input Method -->
              <v-select
                label="Select Input Type"
                :items="['Input File', 'NACA 4 Series Generator']"
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

        <!-- Submit Button -->
        <v-btn @click="submit" color="primary" v-show="submitBtnEnabled">Generate</v-btn>
        <v-progress-circular v-if="loading" indeterminate color="primary"></v-progress-circular>

      </v-card>

      <br>
      
      <!-- === Airfoil Graph === -->
      <v-card variant="tonal">
        <AirfoilGraph v-show="showGraph" ref="airfoilGraph"/>
      </v-card>

    </v-responsive>
  </v-container>
  
</template>
