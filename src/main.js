/**
 * main.js
 */

// Plugins
import { registerPlugins } from '@/plugins'
import { createPinia } from 'pinia'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

const pinia = createPinia()

// Create the app
const app = createApp(App)

// Register plugins
registerPlugins(app)
app.use(pinia)

// Mount the app
app.mount('#app')
