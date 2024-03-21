/**
 * main.js
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Create the app
const app = createApp(App)

// Register plugins
registerPlugins(app)

// Mount the app
app.mount('#app')
