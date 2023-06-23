<template>
  <div>
    <v-card class="px-2 pb-3">
      <v-card-text>
        <v-form>
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
              name="Password"
              label="Password"
              type="password"
              required
              v-model="password"
              :rules="passwordRules"
            ></v-text-field>
          </div>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn block color="info" @click="submit()">Sign In</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import {mapMutations} from 'vuex'
export default {
  name: "Signincomponent",
  data() {
    return {
      email: "",
      username:"",
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /^([A-Za-z0-9_\-\.\u4e00-\u9fa5])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,8})$/g.test(v) || "E-mail must be valid",
      ],
      password: "",
      passwordRules: [
          (v) => !!v || "Password is required",
          (v) => /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,16}$/g.test(v) || "Password must contain 8-16 bits of an upper case letter, a lower case letter, a number, and a special symbol"
          ],
    };
  },
  mounted:function(){
    if(this.$store.state.quanjulogin == "true"){
      this.$router.push('/blog')
    }
  },
  methods: {
    submit() {
      this.$axios.post(
            'http://127.0.0.1:5000/user/login',{
              email:this.email,
              password:this.password
            }
          ).then((response) =>{
            var code = response.data.status
            console.log(code)
            var data = response.data.data
            if(code === -1){
              alert(response.data.message)
            }
            if(code === -2){
              alert(response.data.message)
            }
            if(code === 1){
              
              var loginarray = new Array()
              loginarray[0] = this.email
              loginarray[1] = this.password
              loginarray[2] = true
              loginarray[3] = data
              console.log(data)
              this.quanjulogin(loginarray)
              console.log(this.$store.state)
              location.reload();
              this.$router.push('/loginblank')
            }
          })
    },
    ...mapMutations(['quanjulogin']),
  },
};
</script>
