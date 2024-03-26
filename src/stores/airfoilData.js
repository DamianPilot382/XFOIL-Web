import { defineStore } from 'pinia'

export const useAirfoilDataStore = defineStore('airfoilData', {
    state: () => ({
        airfoilData: String
    }),

})
    