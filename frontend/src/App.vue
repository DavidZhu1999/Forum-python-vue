<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app>
      <v-list>
        <v-list-item> </v-list-item>

        <v-list-item link>
          <v-list-item-content @click="tanchu()">
            <v-list-item-title class="title">
              {{ username }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ email }}</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action @click="gologin()" v-show="!islogin">
            <v-btn>Log In</v-btn>
          </v-list-item-action>

          <v-list-item-action @click="logout()" v-show="islogin">
            <v-btn>Log Out</v-btn>
          </v-list-item-action>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>

      <v-list dense nav shaped>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          @click="tiaozhuan(item)"
          color="red"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar elevate-on-scroll app color="#236778">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title style="color: red">Easy Code</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import { mapMutations } from "vuex";
import cookie from "vue-cookie";
export default {
  data: () => ({
    drawer: null,
    username: "",
    email: "",
    islogin: "",
    items: [
      { title: "Home", icon: "mdi-home", to: "/" },
      {
        title: "Blog",
        icon: "mdi-book-open-page-variant-outline",
        to: "/blog",
      },
      { title: "Account", icon: "mdi-account", to: "/account" },
      { title: "About", icon: "mdi-help-box", to: "/about" },
    ],
  }),
  methods: {
    tiaozhuan: function (item) {
      if (item.title == "Account") {
        if (this.$store.state.quanjulogin == 'true') {
          this.$router.push(item.to);
        }
        else{
          alert("please login")
          this.$router.push('/login')
        }
      } else {
        this.$router.push(item.to);
      }
    },
    tanchu: function () {
      console.log("nihao");
    },
    gologin: function () {
      this.$router.push("/login");
    },
    logout: function () {
      cookie.delete("username");
      cookie.delete("password");
      cookie.delete("email");
      cookie.delete("islogin");
      var loginarray = new Array();
      loginarray[0] = "";
      loginarray[1] = "";
      loginarray[2] = "";
      loginarray[3] = "";
      this.quanjulogin(loginarray);
      location.reload();
    },
    ...mapMutations(["quanjulogin"]),
  },
  created: function () {
    this.username = this.$store.state.quanjuusername;
    this.email = this.$store.state.quanjuemail;
    if (this.$store.state.quanjulogin == "true") {
      this.islogin = true;
    } else {
      this.islogin = false;
    }
  },
  mounted: function () {
    this.username = this.$store.state.quanjuusername;
    this.email = this.$store.state.quanjuemail;
    if (this.$store.state.quanjulogin == "true") {
      this.islogin = true;
    } else {
      this.islogin = false;
    }
  },
  updated: function () {
    this.username = this.$store.state.quanjuusername;
    this.email = this.$store.state.quanjuemail;
    if (this.$store.state.quanjulogin == "true") {
      this.islogin = true;
    } else {
      this.islogin = false;
    }
  },
};
</script>

<style>
</style>