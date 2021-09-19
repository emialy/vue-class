<template>
    <div>
        <div v-if="hasCollect">
            <button name="collect" @click="cancelCollect()">取消收藏</button>
        </div>
        <div v-else>
            <button name="collect" @click="collect">收藏</button>
        </div>
    </div>
    <br>
    <p>已有 {{ collects.length }} 条收藏</p>
    <hr>

    <!-- 渲染所有收藏内容 -->
    <div
            v-for="collect in collects"
            :key="collect.id"
    >
        <div class="collects">
            <div>
                    <span class="username" style="font-size: 13px">
                        {{ collect.author.username }}
                    </span>
                于
                <span class="created">
                    {{ formatted_time(collect.created) }}
                </span>
                收藏
            </div>

        </div>
        <hr>

    </div>
</template>

<script>
    import axios from 'axios';
    import authorization from '@/utils/authorization';
    // import forbiddenArray from "../assets/js/BadWord";

    export default {
        name: 'Collects',
        inject: ['reload'],
        // 通过 props 获取当前文章
        props: {article: Object},
        data: function () {
            return {
                // 所有收藏
                collects: [],
                // forbiddenArray: []
            }
        },
        // 监听 article 对象
        // 以便实时更新收藏
        watch: {
            article() {
                this.collects = this.article !== null ? this.article.collects : []
            }
        },
        methods: {
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
                                // .then(function (response) {
                                //         that.$router.push({name: 'ArticleDetail', params: {id: response.data.id}});
                                //         alert('收藏成功')
                                //     })
                                .then(function () {
                                    // hasCollect1 = hasCollect +1;
                                    // 将新评论添加到顶部
                                    alert('收藏成功')
                                })
                            that.reload()
                        }
                        else {
                            alert('请登录后收藏')
                        }
                    })
            },
            //取消收藏
            cancelCollect(collect) {
                const that = this;
                authorization()
                    .then(function (response) {
                        if (response[0]) {
                            axios
                                .delete('/api/collect/' + collect.id + '/',
                                    {
                                        headers: {Authorization: 'Bearer ' + localStorage.getItem('access.myblog')}
                                    })
                                .then(function () {
                                    alert('收藏已取消')
                                })
                            that.reload()
                        }

                        else {
                            alert('请登录后再操作')
                        }
                    })
            },
        },
        computed: {
            hasCollect() {
                return localStorage.getItem('has_collect.myblog') === 'true'
            }
        }
    }
</script>

<style scoped>
    button {
        cursor: pointer;
        border: none;
        outline: none;
        color: whitesmoke;
        border-radius: 5px;
    }

    .submitBtn {
        height: 35px;
        background: steelblue;
        width: 60px;
    }

    .commentBtn {
        height: 25px;
        background: lightslategray;
        width: 40px;
    }

    .collects {
        padding-top: 10px;
    }

    .username {
        font-weight: bold;
        color: darkorange;
    }

    .created {
        font-weight: bold;
        color: darkblue;
    }
</style>