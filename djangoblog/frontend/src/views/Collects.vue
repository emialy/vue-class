<template>
    <div class="form-elem">
                <button v-on:click.prevent="printCId">提交</button>
            </div>
</template>

<script>
    import axios from 'axios';
    import authorization from '@/utils/authorization';
    import forbiddenArray from "../assets/js/BadWord";

    export default {
        name: 'Collects',
        inject: ['reload'],
        // 通过 props 获取当前文章
        props: {article: Object},
        data: function () {
            return {
                // 所有收藏
                collectID: null
                // forbiddenArray: []
            }
        },
         mounted() {
             const that = this;
            axios
                .get('/api/collect/' + this.$route.params.id+ '/')
                .then(function (response) {
                    const data = response.data;
                    that.collectID = data.id;
                })
        },
        methods: {
            printCId(){
                const that=this;
                alert(that.collectID)
            }
        },
        computed: {
            getUsername() {
                return localStorage.getItem('username.myblog')
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