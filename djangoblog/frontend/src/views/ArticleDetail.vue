<template>
    <div id="back">
        <BlogHeader/>
        <div v-if="article !== null" class="grid-container">
            <div>
                <h1 id="title">{{ article.title }}</h1>
                <p id="subtitle">
                    本文由
                    <span v-if="article.author.username === getUsername">
                        <router-link :to="{ name: 'UserCenter', params: { username: article.author.username }}">
                            {{article.author.username }}
                        </router-link>
                    </span>
                    <span v-if="article.author.username !== getUsername">
                            <router-link
                                    :to="{ name: 'PersonalInfo', params: { username: article.author.username }}">
                                {{article.author.username }}
                            </router-link>
                    </span>
                    发布于 {{ formatted_time(article.created) }}
                    <span v-if="article.author.username === getUsername">
                    <router-link :to="{ name: 'ArticleEdit', params: { id: article.id }}">更新与删除</router-link>
                </span>
                </p>
                <div v-html="article.body" class="article-body" style="white-space: pre-wrap;"></div>
            </div>
        </div>


        <!--<button class="commentBtn" @click="cancelCollect()">取消收藏</button>-->


        <!--<button class="commentBtn" @click="collect">收藏</button>-->
        <!--<div v-if="hasCollect">-->
        <!--<button class="commentBtn" @click="cancelCollect()">取消收藏</button>-->
        <!--</div>-->
        <!--<div v-else>-->
        <!--<button class="commentBtn" @click="collect">收藏</button>-->
        <!--</div>-->
        <Comments :article="article"/>

        <BlogFooter/>
    </div>
</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import Comments from '@/components/Comments.vue'
    // import Collects from '@/components/Collects.vue'
    import authorization from '@/utils/authorization';

    import axios from 'axios';
    // import Collects from "./Collects";


    export default {
        name: 'ArticleDetail',
        components: {BlogHeader, BlogFooter, Comments},
        inject: ['reload'],
        // const: hasCollect = 0,
        data: function () {
            return {
                article: null,
                // hasCollect: false
                collectID: null
            }
        },
        mounted() {
            axios
                .get('/api/article/' + this.$route.params.id)
                .then(response => (
                    this.article = response.data
                ));
        },
        methods: {
            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            },
            // 点击收藏
            collect() {
                const that = this;
                authorization()
                    .then(function (response) {
                        if (response[0]) {
                            axios
                                .post('/api/collect/',
                                    {
                                        article_id: that.article.id,
                                        // hasCollect: true
                                    },
                                    {
                                        headers: {Authorization: 'Bearer ' + localStorage.getItem('access.myblog')}
                                    })
                                .then(function (response) {
                                    // hasCollect1 = hasCollect +1;
                                    // 将新评论添加到顶部
                                    const data = response.data;
                                    that.collectID = data.id;
                                    that.$router.push({name: 'Collects', params: {id: response.data.id}});
                                    alert(that.collectID);
                                })
                            // that.reload()
                        }
                        else {
                            alert('请登录后收藏')
                        }
                    })
            },

            cancelCollect() {
                const that = this;
                // var collectID = await this.collect();
                authorization()
                    .then(function (response) {
                        if (response[0]) {
                            axios
                                .delete('/api/collect/' + that.collectId + '/',
                                    {
                                        headers: {Authorization: 'Bearer ' + localStorage.getItem('access.myblog')}
                                    })
                                .then(function () {
                                    alert('收藏已取消')
                                })
                            // that.reload()
                        }
                        else {
                            alert('请登录后再操作')
                        }
                    })
            },

        },
        computed: {
            isSuperuser() {
                return localStorage.getItem('isSuperuser.myblog') === 'true'
            },
            getUsername() {
                return localStorage.getItem('username.myblog')
            },
            hasCollect() {
                return localStorage.getItem('has_collect.myblog') === 'true'
            },
            // hasCollect1() {
            //     return localStorage.getItem('hasCollect.myblog')+1
            // },
        }
    }
</script>

<style scoped>
    #back {
        margin-top: 7%;
    }

    .grid-container {
        display: grid;
        grid-template-columns: 3fr 1fr;
    }

    #title {
        text-align: center;
        font-size: x-large;
    }

    #subtitle {
        text-align: center;
        color: gray;
        font-size: small;
    }

</style>

<style>
    .article-body p img {
        max-width: 100%;
        border-radius: 50px;
        box-shadow: gray 0 0 20px;
    }

    .toc ul {
        list-style-type: none;
    }

    .toc a {
        color: gray;
    }
</style>