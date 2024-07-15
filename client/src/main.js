import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import HighchartsVue from 'highcharts-vue'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)



app.use(router)
app.use(HighchartsVue)

app.mount('#app')
