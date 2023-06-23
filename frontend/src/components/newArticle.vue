<template>
  <div style="width: 90%; margin: 0 auto">
    <v-text-field
      v-model="title"
      :rules="rules"
      counter="120"
      clearable
      hint=""
      label="TITLE"
    ></v-text-field>
    <v-textarea
      v-model="introduction"
      :rules="rules1"
      counter="240"
      clearable
      hint=""
      label="INTRODUCTION"
    ></v-textarea>
    <h3 style="margin-bottom: 10px">Author: {{ author }}</h3>
    <div>
      <v-btn-toggle
        v-model="toggle_exclusive"
        mandatory
        color="success"
        style="width: 95%; margin: 20px auto"
      >
        <v-btn
          small
          :title="item.text"
          @click="type = item.type"
          v-for="(item, i) in items"
          :key="i"
        >
          <v-icon small>{{ item.icon }}</v-icon>
        </v-btn>
      </v-btn-toggle>
    </div>
    <mavon-editor
      ref="md"
      style="z-index: 0"
      :value="value1"
      language="en"
      v-model="value"
      :toolbars="toolbars"
      :ishljs="true"
      @save="save"
      @imgAdd="$imgAdd"
    />
    <div style="display: flex; justify-content: center; margin: 30px">
      <v-btn color="success" large @click="consolefunction()">upload</v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "blognewArticle",
  data() {
    return {
      type: "all",
      hover: false,
      items: [
        { text: "all", icon: "mdi-semantic-web", type: "all" },
        { text: "c", icon: "mdi-language-c", type: "c" },
        { text: "c++", icon: "mdi-language-cpp", type: "cpp" },
        { text: "c#", icon: "mdi-language-csharp", type: "csharp" },
        { text: "css3", icon: "mdi-language-css3", type: "css3" },
        { text: "go", icon: "mdi-language-go", type: "go" },
        { text: "haskell", icon: "mdi-language-haskell", type: "haskell" },
        { text: "html5", icon: "mdi-language-html5", type: "html5" },
        { text: "java", icon: "mdi-language-java", type: "java" },
        {
          text: "javascript",
          icon: "mdi-language-javascript",
          type: "javascript",
        },
        { text: "lua", icon: "mdi-language-lua", type: "lua" },
        { text: "markdown", icon: "mdi-language-markdown", type: "markdown" },
        { text: "php", icon: "mdi-language-php", type: "php" },
        { text: "python", icon: "mdi-language-python", type: "python" },
        { text: "ruby", icon: "mdi-language-ruby", type: "ruby" },
        { text: "rust", icon: "mdi-language-rust", type: "rust" },
        { text: "swift", icon: "mdi-language-typescript", type: "swift" },
        { text: "vue", icon: "mdi-vuejs", type: "vue" },
        { text: "jquery", icon: "mdi-jquery", type: "jquery" },
        { text: "nodejs", icon: "mdi-nodejs", type: "nodejs" },
      ],
      rules: [(v) => v.length <= 120 || "Max 120 characters"],
      rules1: [(v) => v.length <= 240 || "Max 240 characters"],
      toggle_exclusive: undefined,
      value: "",
      value1: "",
      title: "",
      author: "zhuzhehao",
      introduction: "",
      email: "",
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
    };
  },
  created: function () {
    this.email = this.$store.state.quanjuemail;
    this.author = this.$store.state.quanjuusername;
  },
  methods: {
    consolefunction: function () {
      this.$axios
        .post("http://127.0.0.1:5000/blog/add", {
          title: this.title,
          author: this.author,
          introduction: this.introduction,
          content: this.value,
          email: this.email,
          type: this.type,
        })
        .then((response) => {
          console.log(response);
          console.log(response.data.status);
          if (response.data.status == 1) {
            this.$router.push("/blog");
          }
        });
    },
    save: function () {
      console.log("nihao");
    },
    // 绑定@imgAdd event
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
};
</script>