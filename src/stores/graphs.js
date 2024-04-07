import {defineStore} from 'pinia'
import { ref } from 'vue'

export const useGraphsStore = defineStore('graphs', {
    state: () => ({
        panelGeometry: { img: null, data: null, fillData: null },
        geom_pts: { img: null, data: null },
        control_pts: { img: null, data: null },
        pressure: { img: null, data: null },
        mode: 'img',
        renderImgs: ref(false),
    }),

})
    