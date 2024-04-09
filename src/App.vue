<script setup>
import AirfoilPanel from './components/Airfoil/AirfoilPanel.vue';
import SolverPanel from './components/Solver/SolverPanel.vue';
import { reactive, provide, inject } from 'vue';
import { useAirfoilDataStore } from './stores/airfoilData.js';


const stateSymbol = Symbol('state')
const createState = () => reactive({ counter: 0 })
const useState = () => inject(stateSymbol)
const provideState = () => provide(stateSymbol, createState())
const airfoilData = useAirfoilDataStore().airfoilData;

</script>

<template style="background-color: red">

  <v-app>
    
    <!-- === Top Navbar === -->
    <v-app-bar app color="grey" class="align-center text-center">
      <v-container fluid>
        <h1 class="header-logo">Aerospace Helper</h1>
      </v-container>
      </v-app-bar>

    <!-- === Main Content === -->
    <v-main>

      <!-- === Airfoil Panel Section === -->
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <AirfoilPanel />
          </v-col>
        </v-row>
      </v-container>

      <!-- === solver Panel Section === -->
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <SolverPanel />
          </v-col>
        </v-row>
      </v-container>

    </v-main>

  </v-app>

</template>

<style>
  .v-card {
    padding: 1rem;
  }

  .header-logo {
    /* text-align: center; */
    font-family: Futura;
    font-size: 3rem;
    background: linear-gradient(to right, #1f05a2, #03ba1e);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  @font-face {
    font-family: Futura;
    src: url(./assets/fonts/futura/FUTURA76BOLDITALIC.TTF);
  }

</style>
