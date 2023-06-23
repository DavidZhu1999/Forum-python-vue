import Vue from 'vue'
import Vuex from 'vuex'
import cookie from 'vue-cookie'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    quanjuemail: cookie.get("email"),
    quanjupassword: cookie.get("password"),
    quanjulogin: cookie.get("islogin"),
    quanjuusername: cookie.get("username")
  },
  mutations: {
    quanjulogin(state,loginarray){
      state.quanjuemail = loginarray[0],
      state.quanjupassword = loginarray[1],
      state.quanjulogin = loginarray[2],
      state.quanjuusername = loginarray[3],
      cookie.set("email",state.quanjuemail,3),
      cookie.set("password",state.quanjupassword,3),
      cookie.set("islogin",state.quanjulogin,3),
      cookie.set("username",state.quanjuusername,3)
    }
  },
  actions: {
  },
  modules: {
  }
})
