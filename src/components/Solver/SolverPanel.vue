<script setup>
import InputPanel from './InputPanel.vue';
import GraphPanel from './GraphPanel.vue';

</script>

<template>
  <v-container fill-height fluid>
    <v-responsive class="align-center text-center fill-height">
      <v-card variant="tonal">
        <h1>Solver Panel</h1>
        <InputPanel />
        <GraphPanel />
      </v-card>
    </v-responsive>
  </v-container>
</template>

<style scoped>
.v-divider {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>