<template></template>

<script>
export default {
    data(){
        return{
            id:""
        }
    },
  created: function () {
      console.log("nihao")
    console.log(this.$route.query.id)
    this.id=this.$route.query.id
  },
  mounted: function () {
      console.log()
    this.$router.push({path:'/blog/article/' + this.id,query:{id:this.id}});
  },
};
</script>