<template>

    <div id="user-center">
      <div class="form-elem">
                <button v-on:click.prevent="showingDeleteAlert = true" class="delete-btn">注销用户</button>
                <div :class="{ shake: showingDeleteAlert }">
                    <button v-if="showingDeleteAlert" class="confirm-btn" @click.prevent="confirmDelete">确定？</button>
                </div>
            </div>
    </div>

</template>

<script>
    import axios from 'axios';
    import authorization from '@/utils/authorization';

    const storage = localStorage;

    export default {
        name: 'DeleteUser',
        inject: ['reload'],
        data: function () {
            return {
                username: '',
                token: '',
                showingDeleteAlert: false,
            }
        },
        mounted() {
            this.username = storage.getItem('username.myblog');
        },
        methods: {
            confirmDelete() {
                const that = this;
                authorization()
                    .then(function (response) {
                        if (response[0]) {
                            // 获取令牌
                            that.token = storage.getItem('access.myblog');
                            axios
                                .delete('/api/user/' + that.username + '/', {
                                    headers: {Authorization: 'Bearer ' + that.token}
                                })
                                .then(function () {
                                    storage.clear();
                                    that.$router.push({name: 'Home'});
                                })
                            that.reload()
                        }
                    })
            },
        },
    }
</script>

<style scoped>

    .confirm-btn {
        width: 80px;
        margin-top: 10px;
        background-color: darkorange;
    }

    .delete-btn {
        background-color: darkred;
        margin-top: 200px;
    }

    .shake {
        animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
        transform: translate3d(0, 0, 0);
        backface-visibility: hidden;
        perspective: 1000px;
    }

    @keyframes shake {
        10%,
        90% {
            transform: translate3d(-1px, 0, 0);
        }

        20%,
        80% {
            transform: translate3d(2px, 0, 0);
        }

        30%,
        50%,
        70% {
            transform: translate3d(-4px, 0, 0);
        }

        40%,
        60% {
            transform: translate3d(4px, 0, 0);
        }
    }

</style>

<style scoped>

    #user-center {
        text-align: center;
    }

    .form-elem {
        padding: 10px;
    }
    button {
        top: 50%;
        height: 35px;
        cursor: pointer;
        border: none;
        outline: none;
        background: gray;
        color: whitesmoke;
        border-radius: 5px;
        width: 200px;
    }
</style>