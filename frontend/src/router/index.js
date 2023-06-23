import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import blogarticle from '../components/Article.vue'
import blognewArticle from '../components/newArticle.vue'
import store from '../store/index.js'
import articleauthor from '../components/Usercenter.vue'
import changepassword from '../components/changepassword.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
  },
  {
    path:'/blank',
    component: () => import('../views/Blank.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    children:[
      {
        path:'',
        component: () => import('../components/SignIn.vue')
      },
      {
        path:'SignUp',
        component: () => import('../components/SignUp.vue')
      },
    ]
  },
  {
    path: '/signupemail',
    name: 'signupemail',
    component: () => import('../views/signupemail.vue')
  },
  {
    path: '/blog',
    name: 'blog',
    component: () => import('../views/Blog.vue'),
  },
  {
    path:'/articleauthor',
    component: articleauthor
  },
  {
    path:'/blog/article/:id',
    component: blogarticle
  },
  {
    path:'/blog/newArticle',
    component: blognewArticle,
  },
  {
    path:'/account',
    component: () => import('../views/Accountcenter.vue')
  },
  {
    path:'/blogcenter/:username',
    component: articleauthor
  },
  {
    path:'/time',
    component: changepassword
  }
]

const router = new VueRouter({
  routes
})

export default router
