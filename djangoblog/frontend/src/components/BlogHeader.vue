<template>
    <div id="header">
        <nav class="top-nav">
            <ul>
                <li>
                    <router-link to="/">首页</router-link>
                </li>
                <li>
                    <router-link to="/">关于</router-link>
                </li>
                <div class="search">
                    <br>
                    <form>
                        <input v-model="searchText" type="text" placeholder="输入搜索内容...">
                        <button v-on:click.prevent="searchArticles"></button>
                    </form>
                </div>
                <div class="login">
                    <div v-if="hasLogin">
                        <div class="dropdown">
                            <button class="dropbtn">欢迎, {{username}}!</button>
                            <div class="dropdown-content">
                                <router-link :to="{ name: 'UserCenter', params: { username: username }}">用户中心
                                </router-link>
                                <router-link :to="{ name: 'ArticleCreate' }">发表文章</router-link>
                                <router-link to="/" v-on:click.prevent="logout()">登出</router-link>
                            </div>
                        </div>
                    </div>
                    <div v-else>
                        <router-link to="/login" class="login-link">登录</router-link>
                    </div>
                </div>
                <div class="regis">
                    <router-link to="/register" class="regis-link">注册</router-link>
                </div>
            </ul>
        </nav>
    </div>
</template>

<script>
    import authorization from '@/utils/authorization';

    export default {
        name: 'BlogHeader',
        data: function () {
            return {
                username: '',
                searchText: '',
                hasLogin: false,
                isSuperuser: JSON.parse(localStorage.getItem('isSuperuser.myblog')),
            }
        },
        mounted() {
            authorization().then((data) => [this.hasLogin, this.username] = data);
        },
        methods: {
            logout() {
                localStorage.clear();
                window.location.reload(false);
            },
            refresh() {
                this.username = localStorage.getItem('username.myblog');
            },
            searchArticles() {
                const text = this.searchText.trim();
                if (text.charAt(0) !== '') {
                    this.$router.push({name: 'Home', query: {search: text}})
                }

            }
        }
    }
</script>

<style scoped>
    .dropbtn {
        background-color: mediumslateblue;
        color: white;
        padding: 4px 8px 8px 8px;
        font-size: 8px;
        border: none;
        cursor: pointer;
        height: 12px;
        border-radius: 5px;
    }

    /* 容器 <div> - 需要定位下拉内容 */
    .dropdown {
        position: relative;
        display: inline-block;
    }

    /* 下拉内容 (默认隐藏) */
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 80px;
        font-size: 8px;
        box-shadow: 0 4px 10px 0 rgba(0, 0, 0, 0.2);
        text-align: left;
    }

    /* 下拉菜单的链接 */
    .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }

    /* 鼠标移上去后修改下拉菜单链接颜色 */
    .dropdown-content a:hover {
        background-color: #f1f1f1
    }

    /* 在鼠标移上去后显示下拉菜单 */
    .dropdown:hover .dropdown-content {
        display: block;
    }

    /* 当下拉内容显示后修改下拉按钮的背景颜色 */
    .dropdown:hover .dropbtn {
        background-color: darkslateblue;
    }

</style>

<style scoped>
    #header {
        position: fixed;
        left: 0;
        top: 0;
        height: 7%;
        width: 100%;
        background-image: url("../assets/img/2.jpg");
        opacity: 0.7;
        text-align: center;
        font-weight: bold;
    }

    .login-link {
        color: black;
    }

    .login {
        text-align: right;
        padding-left: 91%;
        padding-top: 8px;
        float: right;
        position: absolute;
    }

    .regis-link {
        color: black;
    }

    .regis {
        text-align: right;
        padding-left: 88%;
        padding-top: 8px;
        float: right;
        position: absolute;
    }

    ul {
        display: flex;
        list-style-type: none;
        margin: 0px;
        padding: 0px;
        overflow: hidden;

    }

    li {
        float: left;
        display: block;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
    }

    .search {
        text-align: right;
        padding-left: 73%;
        float: right;
        position: absolute;
    }

    .search {
        text-align: right;
        padding-left: 70%;
        float: right;
        position: absolute;
    }

    form {
        position: absolute;
        width: 100px;
        margin: 0 auto;
    }

    input, button {
        border: none;
        outline: none;
    }

    input {
        width: 100%;
        height: 20px;
        padding-left: 13px;
        padding-right: 46px;
    }

    .search input {
        border: 2px solid gray;
        border-radius: 5px;
        background: transparent;
        top: 0;
        right: 0;
    }

    .search button {
        background: gray;
        height: 25px;
        width: 45px;
        cursor: pointer;
        position: absolute;
        border-radius: 0 5px 5px 0;
        top: 0;
        left: 167px;
    }

    .search button:before {
        content: "搜索";
        font-size: 13px;
        color: white;
    }

</style>