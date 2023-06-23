<template>
  <v-container>
    <div style="display:flex;justify-content:center">
      <h2>
        {{ searchusername }}
      </h2>
    </div>
    <v-card
      max-width="80%"
      style="margin: 10px auto"
      color="#ddd"
      dark
      @click="tiaozhuan(item.id)"
      v-for="(item, i) in filteredBlogs"
      :key="i"
    >
      <v-card-title style="color: black">
        {{ item.title | to-uppercase }}
      </v-card-title>

      <v-card-subtitle style="color: black">{{
        item.introduction | snippet
      }}</v-card-subtitle>
      <v-btn style="color:black" text>{{item.date}}</v-btn>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "articleauthor",
  data() {
    return {
      searchusername: "1",
      items: [],
      email:""
    };
  },
  computed: {
    filteredBlogs: function () {
      return this.items.filter((item) => {
        console.log(this.listtype);
        return item.author.match(this.searchusername);
      });
    },
  },
  methods: {
    tiaozhuan: function (i) {
      this.$router.push({ path: "/blog/article/" + i, query: { id: i } });
    },
  },
  created: function () {
    this.searchusername = this.$route.query.username;
    console.log(this.$route.query.username);
    this.$axios.post("http://127.0.0.1:5000/user/getemail", {
        username:this.$route.query.username
    }).then((response) => {
        this.email = response.data.email[0][0]
    })
  },
  mounted: function () {
    this.$axios
      .post("http://127.0.0.1:5000/blog/blog_author", {
        username: this.searchusername,
      })
      .then((response) => {
        console.log(response.data);
        for (var i = 0; i < response.data.datas.length; i++) {
          var datas = {
            id: response.data.datas[i][0],
            title: response.data.datas[i][1],
            author: response.data.datas[i][2],
            introduction: response.data.datas[i][3],
            mainbody: response.data.datas[i][4],
            type: response.data.datas[i][5],
            date: response.data.datas[i][6]
          };
          this.items.push(datas);
        }
        console.log(this.items);
        console.log(this.items[0].id);
      });
  },
};
</script>