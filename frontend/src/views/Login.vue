<template>
  <div id="Login" style="width: 500px; margin: 50px auto">
    <v-card color="basil">
        <v-tabs grow>
            <v-tab to="/login">SignIn</v-tab>
            <v-tab to="/login/SignUp">SignUp</v-tab>
        </v-tabs>
        <router-view></router-view>
    </v-card>
  </div>
</template>

<script>

export default {
  name: "Login",

  data () {
      return {
        tab: null,
      }
    },
};
</script>

<style scoped>
/* Helper classes */
.basil {
  background-color: #FFFBE6 !important;
}
.basil--text {
  color: #356859 !important;
}
</style>