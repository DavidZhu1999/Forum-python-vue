<template>
    <div>
        <button @click="tixing()">console</button>
        {{filteredBlogs}}
    </div>
</template>

<script>
export default {
    data:function(){
        return{
            items:[],
        }
    },
    methods:{
        tixing:function(){
            console.log(this.items)
        }
    },
  computed: {
    filteredBlogs: function () {
      return this.items.filter((item) => {
        return(item.date.match("2021-04"))
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
}
</script>