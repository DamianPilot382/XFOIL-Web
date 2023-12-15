<template>
  <v-app>
    <v-app-bar app color="grey" dark>
      <v-img alt="XFoil" contain src="./assets/logo.png" max-height="3rem"></v-img>
    </v-app-bar>
    <v-main>
      <!-- two column layout with graph on left and input on right -->
      <v-container fluid>
        <v-row>
          <v-col cols="7">
            <GraphPanel />
          </v-col>
          <v-col cols="5">
            <InputPanel />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  import InputPanel from './components/InputPanel.vue';
  import GraphPanel from './components/GraphPanel.vue';
</script>

<style >
.v-card {
  padding: 1rem;
}
</style>