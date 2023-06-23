<template>
  <div>
    <v-card class="px-2 pb-3">
      <v-card-text>
        <v-form>
          <div style="display: flex">
            <v-icon style="padding-right: 10px">mdi-account</v-icon>
            <v-text-field
              name="username"
              label="Username"
              type="text"
              required
              v-model="username"
              
            ></v-text-field>
          </div>
          <div style="display: flex">
            <v-icon style="padding-right: 10px">mdi-email</v-icon>
            <v-text-field
              name="email"
              label="Email Address"
              type="text"
              required
              v-model="email"
              :rules="emailRules"
            ></v-text-field>
          </div>
          <div style="display: flex">
            <v-icon style="padding-right: 10px">mdi-lock</v-icon>
            <v-text-field
              id="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              name="Password"
              label="Password"
              :type="show1 ? 'text' : 'password'"
              required
              v-model="password"
              @click:append="show1 = !show1"
              :rules="passwordRules"
            ></v-text-field>
          </div>
          <div style="display: flex">
            <v-icon style="padding-right: 10px">mdi-lock</v-icon>
            <v-text-field
              id="verifypassword"
              :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
              name="verifyPassword"
              label="Verify Password"
              :type="show2 ? 'text' : 'password'"
              required
              v-model="verifypassword"
              @click:append="show2 = !show2"
              :rules="[samepasswordcheck || 'The password are not same']"
            ></v-text-field>
          </div>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn block color="info" @click="submit()">Signup</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import {mapMutations} from 'vuex'
export default {
  name: "Signupcomponent",
  data() {
    return {
      username: "",
      email: "",
      show1: false,
      show2: false,
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) =>
          /^([A-Za-z0-9_\-\.\u4e00-\u9fa5])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,8})$/g.test(
            v
          ) || "E-mail must be valid",
      ],
      password: "",
      verifypassword: "",
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
    submit() {
      if (this.password == this.verifypassword) {
        this.$axios
          .post("http://127.0.0.1:5000/user/register", {
            username: this.username,
            password: this.password,
            email: this.email,
          })
          .then((response) => {
            console.log(response)
            var code = response.data.status;
            if (code == 1) {
              alert(response.data.message);
              console.log(this.username)
              console.log(this.password)
              console.log(this.email)
              this.$router.push({
                name: "signupemail",
                params: {
                  username: this.username,
                  password: this.password,
                  email: this.email,
                },
              });
            }
          });
      }
    },
    samepasswordcheck() {
      if (this.password == this.verifypassword) {
        return true;
      } else {
        return "The password are not same";
      }
    },
    ...mapMutations(['quanjulogin']),
  },
};
</script>
