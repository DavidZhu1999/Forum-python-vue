<template>
  <div id="Login" style="width: 600px; margin: 50px auto">
    <v-card color="basil">
      <div style="display: flex;padding:50px 0">
        <v-spacer></v-spacer>
        <v-chip id="verification" x-large outlined>
          <v-icon left>mdi-check-decagram-outline</v-icon>
          Verification
        </v-chip>
        <v-spacer></v-spacer>
      </div>
      <v-divider></v-divider>
      <v-col>
      <v-text-field  @keyup.enter="uploadyanzheng()" class="pa-2" v-model="yanzheng" counter="6" hint="Please input the verification code" label="Verification"></v-text-field>
      </v-col>
        <div style="display:flex">
          <v-spacer></v-spacer>
        <v-btn @click="uploadyanzheng()" x-large color="primary">Verify</v-btn>
          <v-spacer></v-spacer>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      username: "",
      password: "",
      email: "",
      yanzheng: "",
    };
  },
  methods: {
    uploadyanzheng: function () {
      console.log(this.username);
      this.$axios
        .post("http://127.0.0.1:5000/user/emailverify", {
          username: this.username,
          password: this.password,
          email: this.email,
          verifycode: this.yanzheng,
        })
        .then((response) => {
          var code = response.data.status;
          if(code == 1){
            alert(response.data.message)
            this.$router.push('/blog')
          }
        });
    },
  },
  created: function () {
    (this.username = this.$route.params.username),
      (this.password = this.$route.params.password),
      (this.email = this.$route.params.email);
  },
};
</script>