import Vue from 'vue' // 不管怎样，vue原库是必须得引入的
import Router from 'vue-router'
import Chat from '@/pages/Chat.vue'

Vue.use(Router)

export default new Router({ // 路由的实例化
  routes: [ // 设计了只用一个路线,如下所示，也就是说，我们不存在组件的路线切换,但是大型应用就是多条路由映射了
    {
      path: '/',
      name: 'Chat',
      component: Chat
    }
  ]
})
