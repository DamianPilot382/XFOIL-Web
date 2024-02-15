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
              <!-- <FileInputPanel ref="doge"/> -->

            </v-col>
          </v-row>
        <br>
        <v-divider></v-divider>
        <br>
        <v-btn @click="submit" color="primary" v-show="submitBtnEnabled">Generate</v-btn>
      </v-card>
    </v-responsive>
  </v-container>
</template>
  
<script setup>

import FileInputPanel from "./FileInputPanel.vue";
import NACAInputPanel from "./NACAInputPanel.vue";
import { shallowRef, ref } from "vue";


var inputPanel = ref(null);
var inputMethodSelected = shallowRef(null);
var submitBtnEnabled = ref(false);

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
  if(inputMethodSelected.value == null){
    console.log("No input panel selected");
    return;
  }

  inputPanel.value.submit();
};

</script>
