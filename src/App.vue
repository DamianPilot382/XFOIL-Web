<script setup>
import AirfoilPanel from './components/Airfoil/AirfoilPanel.vue';
</script>

<template>

  <v-app>
    
    <!-- === Top Navbar === -->
    <v-app-bar app color="grey" dark>
      <v-img alt="XFoil" contain src="./assets/logo.png" max-height="3rem"></v-img>
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

    </v-main>

  </v-app>
</template>

<style>
  .v-card {
    padding: 1rem;
  }
</style>
