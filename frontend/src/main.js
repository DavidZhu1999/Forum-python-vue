import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import axios from 'axios'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

Vue.prototype.$axios = axios
Vue.config.productionTip = false
Vue.use(mavonEditor)

Vue.directive('rainbow', {
  bind(el,binding,vnode){
    el.style.color = "#" + Math.random().toString(16).slice(2,8)
  }
})

Vue.filter("to-uppercase",function(value){
  return value.toUpperCase()
})

Vue.filter("snippet",function(value){
  return value.slice(0,100) + "..."
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
