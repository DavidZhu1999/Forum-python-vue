<template>
  <div id="blog">
    <div
      style="position: absolute;left:85%;top:12%;z-index:1"
    >
  <v-card
    class="mx-auto"
    max-width="300"
    tile
  >
    <v-list dense>
      <v-subheader>Class</v-subheader>
      <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
        <v-list-item
        dense
          v-for="(item, i) in item1s"
          :key="i"
          @click="listtype=item.type"
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
    </div>
    <v-container style="display: flex">
      <h1 style="margin: 0px auto">Blog</h1>
      <v-btn style="margin-left: auto; margin-top: 10px" @click="addnew()"
        >add blog</v-btn
      ></v-container
    >
    <v-divider></v-divider>
    <v-container><v-text-field placeholder="search for title or author" v-model="search"></v-text-field></v-container>

    <v-container>
      <v-card
        max-width="80%"
        style="margin: 10px 10px"
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

        <v-card-actions style="display:flex;justify-content:space-between">
          <v-btn style="color:black" text @click="tiaozhuanzuozhe(item.author)">
            {{ item.author }}
          </v-btn>
          <v-btn style="color:black" text>{{item.date}}</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedItem: 0,
      item1s: [
        { text: "all", icon: "mdi-semantic-web", type:"all" },
        { text: "c", icon: "mdi-language-c", type:"c" },
        { text: "c++", icon: "mdi-language-cpp", type:"cpp" },
        { text: "c#", icon: "mdi-language-csharp", type:"csharp"  },
        { text: "css3", icon: "mdi-language-css3", type:"css3" },
        { text: "go", icon: "mdi-language-go", type:"go" },
        { text: "haskell", icon: "mdi-language-haskell", type:"haskell" },
        { text: "html5", icon: "mdi-language-html5", type:"html5" },
        { text: "java", icon: "mdi-language-java", type:"java" },
        { text: "javascript", icon: "mdi-language-javascript", type:"javascript" },
        { text: "lua", icon: "mdi-language-lua", type:"lua" },
        { text: "markdown", icon: "mdi-language-markdown", type:"markdown" },
        { text: "php", icon: "mdi-language-php", type:"php" },
        { text: "python", icon: "mdi-language-python", type:"python" },
        { text: "ruby", icon: "mdi-language-ruby", type:"ruby" },
        { text: "rust", icon: "mdi-language-rust", type:"rust" },
        { text: "swift", icon: "mdi-language-typescript", type:"swift" },
        { text: "vue", icon: "mdi-vuejs", type:"vue" },
        { text: "jquery", icon: "mdi-jquery", type:"jquery" },
        { text: "nodejs", icon: "mdi-nodejs", type:"nodejs" },
      ],
      items: [
      ],
      search: "",
      listtype: "all",
    };
  },

  methods: {
    tiaozhuan: function (i) {
      this.$router.push({ path: "/blog/article/" + i, query: { id: i } });
    },
    tiaozhuanzuozhe:function(i){
      this.$router.push({ path: "/blogcenter/" + i, query: {username: i} })
    },
    addnew: function () {
      if(this.$store.state.quanjulogin == "true"){
        window.open("http://localhost:8080/#/blog/newArticle", "_blank");
      }
      else{
        alert("pleaselogin")
        this.$router.push('/login')
      }
    },
  },
  computed: {
    filteredBlogs: function () {
      return this.items.filter((item) => {
        console.log(this.listtype);
        if (this.listtype === "all") {
          return (
            item.author.match(this.search) || item.title.match(this.search)
          );
        } else if (item.type === this.listtype) {
          return (
            item.author.match(this.search) || item.title.match(this.search)
          );
        } else {
          return null;
        }
      });
    },
  },
  mounted: function () {
    this.$axios.get("http://127.0.0.1:5000/blog/query").then((response) => {
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

<style scoped>
</style>