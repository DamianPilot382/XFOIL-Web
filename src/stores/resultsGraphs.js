import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useResultsGraphsStore = defineStore('resultsGraphs', {
    state: () => ({
        pressureCoeff: ref({})
    }),

})
