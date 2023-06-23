<template>
  <div>
    <div style="display: flex">
      <v-icon style="padding-right: 10px">mdi-lock</v-icon>
      <v-text-field
        id="password"
        :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
        name="Password"
        label="Password"
        :type="show ? 'text' : 'password'"
        required
        v-model="password"
        @click:append="show = !show"
        :rules="passwordRules"
      ></v-text-field>
      <v-btn @click="getverifycode()" style="margin: 10px">getverifycode</v-btn>
    </div>
    <v-text-field
      class="pa-2"
      v-model="verifycode"
      counter="6"
      hint="Please input the verification code"
      label="Verification"
    ></v-text-field>
    <div style="display: flex; justify-content: center">
      <v-btn @click="changepassword()" style="margin: 10px 0px" color="green"
        >changepassword</v-btn
      >
    </div>
  </div>
</template>

<script>
import cookie from "vue-cookie";
import { mapMutations } from "vuex";
export default {
  name: "changepassword",
  data: function () {
    return {
      show: false,
      password: "",
      verifycode: "",
      passwordRules: [
        (v) => !!v || "Password is required",
        (v) =>
          /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,16}$/g.test(
            v
          ) ||
          "Password must contain 8-16 bits of an upper case letter, a lower case letter, a number, and a special symbol",
      ],
    };
  },
  methods: {
    getverifycode: function () {
      this.$axios
        .post("http://127.0.0.1:5000/user/changepassword", {
          email: this.$store.state.quanjuemail,
        })
        .then((response) => {
          console.log(response);
        });
    },
    changepassword: function () {
      this.$axios
        .post("http://127.0.0.1:5000/user/changepasswordverifycode", {
          email: this.$store.state.quanjuemail,
          verifycode: this.verifycode,
          password: this.password,
        })
        .then((response) => {
          if (response.data.status == 1) {
            alert(response.data.message);
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
            this.$router.push("/blog");
          } else {
            alert(response.data.message);
          }
        });
    },
        ...mapMutations(["quanjulogin"]),
  },
};
</script>