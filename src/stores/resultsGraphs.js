import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useResultsGraphsStore = defineStore('resultsGraphs', {
    state: () => ({
        pressureCoeff: ref({}),
        Cl_SPVP: ref(0),
        Cl_KJ: ref(0),
        Cm_SPVP : ref(0)
    }),

})
