<script setup>
import AirfoilPanel from './components/Airfoil/AirfoilPanel.vue';
import InputPanel from './components/Solver/InputPanel.vue';
import { reactive, provide, inject } from 'vue';
import { useAirfoilDataStore } from './stores/airfoilData.js';


const stateSymbol = Symbol('state')
const createState = () => reactive({ counter: 0 })
const useState = () => inject(stateSymbol)
const provideState = () => provide(stateSymbol, createState())
const airfoilData = useAirfoilDataStore().airfoilData;

</script>

<template>

  <v-app>
    
    <!-- === Top Navbar === -->
    <v-app-bar app color="grey" dark>
      <v-img alt="XFoil" contain src="./assets/logo.png" max-height="3rem"></v-img>
    </v-app-bar>

    <!-- === Main Content === -->
    <v-main>

      <p style="text-align: center">El Doge {{ airfoilData.value }} shiba</p>

      <!-- === Airfoil Panel Section === -->
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <AirfoilPanel />
          </v-col>
        </v-row>
      </v-container>

      <!-- === Airfoil Panel Section === -->
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <InputPanel />
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
</style>
