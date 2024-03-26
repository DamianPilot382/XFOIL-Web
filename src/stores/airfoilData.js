import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAirfoilDataStore = defineStore('airfoilData', {
    state: () => ({
        airfoilData: ref({})
    }),

})
    