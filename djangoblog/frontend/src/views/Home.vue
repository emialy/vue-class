<template>
<div id="background">
    <BlogHeader/>

    <ArticleList/>

    <BlogFooter/>
</div>
</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import ArticleList from '@/components/ArticleList.vue'


    export default {
        name: 'Home',
        components: {BlogHeader, BlogFooter, ArticleList}
    }
</script>
<style>
@import "../assets/css/bkg.css";
</style>