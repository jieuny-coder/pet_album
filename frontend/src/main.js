import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'  //만든 라우터 가져오기 

const app = createApp(App)

app.use(router)   // 라우터를 Vue앱에 등록

app.mount('#app')  // Vue 앱을 index.html의 <div id="app">에 붙이기
