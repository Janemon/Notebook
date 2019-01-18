// 这是业务逻辑入口文件
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.prototype.$http = axios /* axios严格来说因为不算是vue里面的插件吧，所以不用 Vue.use */
Vue.config.productionTip = false

// eslint-disable-next-line
/* eslint-disable */
new Vue({
  el: '#app', // 挂载点
  router, // 使用的路由映射表
  components: { App }, // 组件的内容
  template: '<App/>' // html替换的模板，使用的是组件的内容
})
