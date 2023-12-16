import {defineStore} from 'pinia'

export const useGraphsStore = defineStore('graphs', {
    state: () => ({
        panelGeometry: { img: null, data: null },
        geom_pts: { img: null, data: null },
        control_pts: { img: null, data: null },
        pressure: { img: null, data: null },
        mode: 'img'
    }),

})
    