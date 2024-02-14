<template>
  <v-app>
    <v-app-bar app color="grey" dark>
      <v-img alt="XFoil" contain src="./assets/logo.png" max-height="3rem"></v-img>
    </v-app-bar>
    <v-main>
      <h1>Hello there</h1>
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <b-button variant="success">Hello World!</b-button>
            <!-- <Dropper /> -->
          </v-col>
        </v-row>
        <!-- <v-row>
          <v-col cols="7">
            <AirfoilPanel />
          </v-col>
          <v-col cols="5">
            <NACAInputPanel />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="7">
            <GraphPanel />
          </v-col>
          <v-col cols="5">
            <InputPanel />
          </v-col>
        </v-row> -->
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  // import InputPanel from './components/InputPanel.vue';
  // import GraphPanel from './components/GraphPanel.vue';
  // import NACAInputPanel from './components/NACAInputPanel.vue';
  // import AirfoilPanel from './components/AirfoilPanel.vue';
  // import Dropdown from './components/Dropdown.vue';
  // import Dropper from './components/Dropper.vue';
</script>

<style >
  .v-card {
    padding: 1rem;
  }
</style>