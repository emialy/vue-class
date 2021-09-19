<template>
 <div id="background">
   <BlogHeader/>
   <div class="box-left">
     <ul>
      <li>
        <router-link to="usercenter">完善资料</router-link>
      </li>
      <li>
        <router-link to="collectlist">我的收藏</router-link>
      </li>
      <li>
        <router-link to="myarticles">我发过的</router-link>
      </li>
      <li>
        <router-link to="deleteuser">注销用户</router-link>
      </li>
</ul>
   </div>
   <div class="box-right">
     <router-view></router-view>
   </div>
 </div>
  <BlogFooter/>
</template>

<script>
import BlogFooter from "../components/BlogFooter";
import BlogHeader from "../components/BlogHeader";
export default {
  name: "User.vue",
  components: {BlogHeader, BlogFooter}
}
</script>

<style scoped>
.box-left{
  height: 100%;
  float: left;
}
.box-right{
  overflow: hidden;
  height: 100%;
}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 20%;
    background-color: #f1f1f1;
    position: fixed;
    height: 100%;
    overflow: auto;
    font-weight: bold;
}
li a {
    display: block;
    color: #000;
    padding: 8px 16px;
    text-decoration: none;
}
li a:hover:not(.active) {
    background-color: #555;
    color: white;
}
</style>