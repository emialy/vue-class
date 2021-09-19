<template>
<div id="background">
    <BlogHeader/>

    <div id="grid">
        <div id="signin">
            <h3>登录账号</h3>
            <form>
                <div class="form-elem">
                    <span>账号：</span>
                    <input v-model="signinName" type="text" placeholder="输入用户名">
                </div>

                <div class="form-elem">
                    <span>密码：</span>
                    <input v-model="signinPwd" type="password" placeholder="输入密码">
                </div>

                <div class="form-elem">
                    <button v-on:click.prevent="signin">登录</button>
                </div>
            </form>
        </div>
    </div>


    <BlogFooter/>
</div>
</template>

<script>
    import axios from 'axios';
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'


    export default {
        name: 'Login',
        components: {BlogHeader, BlogFooter},
        data: function () {
            return {
                signinName: '',
                signinPwd: '',
                signupResponse: null,
            }
        },
        methods: {
            signin() {
                const that = this;
                axios
                    .post('/api/token/', {
                        username: that.signinName,
                        password: that.signinPwd,
                    })
                    .then(function (response) {
                        const storage = localStorage;
                        const expiredTime = Date.parse(response.headers.date) + 60 * 100 * 1000;
                        // 设置 localStorage
                        storage.setItem('access.myblog', response.data.access);
                        storage.setItem('refresh.myblog', response.data.refresh);
                        storage.setItem('expiredTime.myblog', expiredTime);
                        storage.setItem('username.myblog', that.signinName);

                        // 是否为管理员
                        axios
                            .get('/api/user/' + that.signinName + '/')
                            .then(function (response) {
                                storage.setItem('isSuperuser.myblog', response.data.is_superuser);
                                // 路由跳转
                                that.$router.push({name: 'Home'});
                            });
                    })
            },
        }
    }
</script>

<style scoped>
    #grid {
        display: grid;
        margin-top: 80px;
        grid-template-columns: 1fr 1fr;
    }
    h3{
      color: purple;
    }
    #signin {
      text-align: center;
      font-weight: bold;
    }

    .form-elem {
        padding: 10px;
    }

    input {
        height: 25px;
        padding-left: 10px;
    }

    button {
        height: 35px;
        cursor: pointer;
        border: none;
        outline: none;
        background: gray;
        color: whitesmoke;
        border-radius: 5px;
        width: 60px;
    }
</style>