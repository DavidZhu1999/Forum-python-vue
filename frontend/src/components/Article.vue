<template>
  <v-card max-width="80%" style="margin: 10px auto; z-index: 0" outlined>
    <div class="head">
      <p
        style="display: flex; justify-content: center"
        class="font-weight-black"
      >
        {{ title }}
      </p>
    </div>
    <v-divider></v-divider>
    <div class="author">
      <h3>Author: {{ author }}</h3>
    </div>
    <v-divider></v-divider>
    <v-card-subtitle style="padding: 2px"
      >Introduction: {{ introduction }}</v-card-subtitle
    >
    <v-divider></v-divider>
    <div class="editor">
      <mavon-editor
        :subfield="false"
        :toolbarsFlag="false"
        language="en"
        default-open="preview"
        v-model="mainbody"
      />
    </div>
    <v-divider></v-divider>
    <div style="margin:20px 0;width:100%;display:flex;justify-content:center">
    <v-btn dense v-show="homer==nowuser" color="red" @click="deleteblog()"
          >DELETE BLOG</v-btn>
    </div>
    <h1
      style="
        margin-top: 10px;
        border-top-style: solid;
        display: flex;
        justify-content: center;
      "
    >
      Comment
    </h1>
    <v-divider></v-divider>

    <v-divider></v-divider>
    <div v-for="(comment, i) in comments" :key="i">
      <h3>Commenter: {{ comment.author }}</h3>
      <mavon-editor
        :subfield="false"
        :toolbarsFlag="false"
        language="en"
        default-open="preview"
        v-model="comment.content"
      />
      <div style="margin:20px 0;width:100%;display:flex;justify-content:center">
        <v-btn small v-show="homer==nowuser" color="red" @click="deletecomment(comment.comment_id)"
          >DELETE COMMENT</v-btn
        >
      </div>
      <v-divider inset></v-divider>
      <div
        style="text-align: right; margin: 10px 0px"
        v-for="(review, j) in comment.review"
        :key="j"
      >
        <v-divider></v-divider>
        <h4>{{ review.content }}</h4>
        <h6>{{ review.author }}</h6>
        <v-divider></v-divider>
        <v-btn x-small v-show="homer==nowuser" color="red" @click="deletereview(review.review_id)"
          >DELETE</v-btn
        >
        <v-divider></v-divider>
      </div>
      <v-text-field
        v-model="newreview[i]"
        :rules="[(v) => v.length <= 200 || 'Max 200 characters']"
        counter="200"
        hint="This field uses counter prop"
        label="Review"
      ></v-text-field>
      <div style="text-align: right; margin-bottom: 10px">
        <v-btn @click="addreview(i)" color="green" x-small>add review</v-btn>
      </div>
      <v-divider></v-divider>
    </div>
    <div>
      <mavon-editor
      ref="md"
      @imgAdd="$imgAdd"
        :autofocus="false"
        language="en"
        v-model="value"
        :toolbars="toolbars"
        :ishljs="true"
      />
    </div>
    <div style="display: flex; justify-content: center">
      <v-btn
        @click="addcomment()"
        color="green"
        large
        style="margin: 10px 0px"
        >add comment</v-btn
      >
    </div>
  </v-card>
</template>

<script>
export default {
  name: "blogarticle",
  methods: {
    addreview: function (i) {
      if(this.$store.state.quanjulogin != "true"){
        alert("pleaselogin")
        this.$router.push('/login')
      }
      else{
        console.log(i);
        this.$axios
        .post("http://127.0.0.1:5000/blog/comment_review", {
          id: this.comments[i].comment_id,
          author: this.$store.state.quanjuusername,
          content: this.newreview[i],
        })
        .then((response) => {
          console.log(response);
          console.log(this.id);
          this.$router.push({ path: "/blank", query: { id: this.id } });
        });
          }
    },
    addcomment: function () {
      if(this.$store.state.quanjulogin != "true"){
        alert("pleaselogin")
        this.$router.push('/login')
      }
      else{
      this.$axios
        .post("http://127.0.0.1:5000/blog/comment_blog", {
          id: this.id,
          author: this.$store.state.quanjuusername,
          content: this.value,
        })
        .then((response) => {
          console.log(response);
          console.log(this.id);
          this.$router.push({ path: "/blank", query: { id: this.id } });
        });
      }
    },
    deleteblog:function(){
      this.$axios.post("http://127.0.0.1:5000/blog/blog_delete", {
        id: this.id
      })
      .then((response)=>{
        console.log(response)
        this.$router.push({ path: "/blog"});
      })
    },
    deletecomment: function (id) {
      this.$axios.post("http://127.0.0.1:5000/blog/comment_blog_delete", {
        id: id
      })
      .then((response)=>{
        console.log(response)
        this.$router.push({ path: "/blank", query: { id: this.id } });
      })
    },
    deletereview: function (id) {
      this.$axios.post("http://127.0.0.1:5000/blog/comment_review_delete", {
        id: id
      })
      .then((response)=>{
        console.log(response)
        this.$router.push({ path: "/blank", query: { id: this.id } });
      })
    },
     $imgAdd(pos, $file) {
      var formdata = new FormData();
      formdata.append("image", $file);
      this.$axios({
        url: "http://127.0.0.1:5000/blog/upload_image",
        method: "post",
        data: formdata,
        headers: { "Content-Type": "multipart/form-data" },
      }).then((url) => {
        console.log(url)
        this.$refs.md.$img2Url(pos, url.data);
      });
    },
  },
  data() {
    return {
      deleteswitch: true,
      homer: "",
      id: "",
      title: "",
      author: "",
      mainbody: "",
      introduction: "",
      head_title: "nihao",
      author: "zhuzhehao",
      newreview: [],
      main_introduction: "baobao",
            toolbars: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        strikethrough: true, // 中划线
        mark: true, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        imagelink: true, // 图片链接
        code: true, // code
        table: true, // 表格
        fullscreen: false, // 全屏编辑
        readmodel: true, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        help: true, // 帮助
        undo: true, // 上一步
        redo: true, // 下一步
        trash: true, // 清空
        save: true, // 保存（触发events中的save事件）
        navigation: true, // 导航目录
        alignleft: true, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        subfield: true, // 单双栏模式
        preview: true, // 预览
      },
      value: "",
      value1:
        "nihaobaobao\n```javascript\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\nconsole.log('nihao')\n```",
      comments: [

      ],
    };
  },
  created: function () {
    console.log(this.$route.query.id);
    this.$axios
      .post("http://127.0.0.1:5000/blog/detail", {
        id: this.$route.query.id,
      })
      .then((response) => {
        console.log(response);
        this.title = response.data.datas.blog[1];
        this.id = response.data.datas.blog[0];
        this.author = response.data.datas.blog[2];
        this.introduction = response.data.datas.blog[3];
        this.mainbody = response.data.datas.blog[4];
        this.comments = response.data.datas.comment;
        this.homer = response.data.datas.blog[5];
        this.nowuser = this.$store.state.quanjuemail
        console.log(this.homer);
        console.log(this.nowuser)
      });
  },
  mounted: function () {
    console.log(this.$route.query.id);
    this.$axios
      .post("http://127.0.0.1:5000/blog/detail", {
        id: this.$route.query.id,
      })
      .then((response) => {
        console.log(response);
        this.title = response.data.datas.blog[1];
        this.id = response.data.datas.blog[0];
        this.author = response.data.datas.blog[2];
        this.introduction = response.data.datas.blog[3];
        this.mainbody = response.data.datas.blog[4];
        this.comments = response.data.datas.comment;
        this.homer = response.data.datas.blog[5];
        console.log(this.homer);
      });
  },
};
</script>

<style scoped>
.head {
  font-size: 40px;
}
.head p {
  margin-bottom: 0px;
}
</style>