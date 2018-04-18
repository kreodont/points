import Vue from 'vue'
import Router from 'vue-router'
import Points from '@/components/Points'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Points',
      component: Points
    }
  ]
})
