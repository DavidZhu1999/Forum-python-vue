<template>
  <v-container>
    <v-card max-width="40%" color="#ddd" style="margin: 10px auto">
      <changepassword></changepassword>
    </v-card>
      <v-card
        max-width="80%"
        style="margin: 10px auto"
        color="#ddd"
        dark
        @click="tiaozhuan(item.id)"
        v-for="(item, i) in filteredBlogs"
        :key="i"
      >
        <v-card-title style="color:black">
          {{ item.title | to-uppercase}}
        </v-card-title>

        <v-card-subtitle style="color:black">{{ item.introduction | snippet}}</v-card-subtitle>

      </v-card>
    </v-container>
</template>

<script>
import changepassword from '../components/changepassword.vue'
  export default {
    components:{
      changepassword
    },
    data: () => ({
      loading: false,
      selection: 1,
      items:[],
      username:""
    }),
computed: {
    filteredBlogs: function () {
      return this.items.filter((item) => {
        console.log(this.listtype);
        return item.author.match(this.$route.query.username);
      });
    },
  },
    methods: {
          tiaozhuan: function (i) {
      this.$router.push({ path: "/blog/article/" + i, query: { id: i } });
    },
    },
    created: function () {
      this.username=this.$store.state.quanjuusername
    },
    mounted: function () {
      this.username=this.$store.state.quanjuusername
    this.$axios.post("http://127.0.0.1:5000/blog/blog_author",{
      username:this.username
    }).then((response) => {
      console.log(response.data);
      for (var i = 0; i < response.data.datas.length; i++) {
        var datas = {
          id: response.data.datas[i][0],
          title: response.data.datas[i][1],
          author: response.data.datas[i][2],
          introduction: response.data.datas[i][3],
          mainbody: response.data.datas[i][4],
          type: response.data.datas[i][5]
        };
        this.items.push(datas);
      }
      console.log(this.items);
      console.log(this.items[0].id);
      
    });
  },
  }
</script>