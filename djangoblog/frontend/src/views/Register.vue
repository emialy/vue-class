<template>
<div id="background">
    <BlogHeader/>
    <div id="grid">
        <div id="signup">
            <h3>注册账号</h3>
            <form>
                <div class="form-elem">
                    <span>账号：</span>
                    <input v-model="signupName" type="text" placeholder="输入用户名">
                </div>
                <div class="form-elem">
                    <span>生日：</span>
                    <input v-model="birthday" type="date" placeholder="输入生日">
                </div>
               <div class="form-elem">
                    <span>地址：</span>
                    <input v-model="address" type="text" placeholder="输入地址">
                </div>
                <div class="form-elem">
                    <span>手机：</span>
                    <input v-model="mobile" type="text" placeholder="输入手机号">
                </div>

                <div class="form-elem">
                    <span>密码：</span>
                    <input v-model="signupPwd" type="password" placeholder="输入密码">
                </div>
               <div class="form-elem">
                    <span>确认密码：</span>
                    <input v-model="resignupPwd" type="password" placeholder="确认密码">
                </div>
              <span v-if="signupPwd===resignupPwd">
                <div class="form-elem">
                    <button v-on:click.prevent="signup">提交</button>
                </div>
              </span>
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
        name: 'Register',
        components: {BlogHeader, BlogFooter},
        data: function () {
            return {
                signupName: '',
                signupPwd: '',
                signupResponse: null,
                resignupPwd:'',
                birthday:'',
                address:'',
                mobile:'',
            }
        },
        methods: {
            signup() {
                const that = this;
                axios
                    .post('/api/user/', {
                        username: this.signupName,
                        password: this.signupPwd,
                        birthday: this.birthday,
                        address: this.address,
                        mobile: this.mobile,
                    })
                    .then(function (response) {
                        that.signupResponse = response.data;
                        alert('用户注册成功，快去登录吧！');
                    })
                    .catch(function (error) {
                        alert(error.message);

                    });
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
    #signup {
        top: 70px;
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