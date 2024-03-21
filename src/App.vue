<template>
  <v-app>
    <v-app-bar app color="grey" dark>
      <v-img alt="XFoil" contain src="./assets/logo.png" max-height="3rem"></v-img>
    </v-app-bar>

    <v-main>
      <br>
      <h1 class="text-center">Xfoil-Web</h1>
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <AirfoilPanel />
          </v-col>
        </v-row>
      </v-container>
    </v-main>

  </v-app>
</template>

<script setup>
import AirfoilPanel from './components/Airfoil/AirfoilPanel.vue'
import AirfoilGraph from './components/Graphs/AirfoilGraph.vue'

</script>

<style >
  .v-card {
    padding: 1rem;
  }
</style>