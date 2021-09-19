<template>

        <router-view v-if="isRouterAlive" />
</template>

<script>
export default {
  name: 'App',
	provide(){
		return{
			reload:this.reload
		}
	},
	data(){
		return{
			isRouterAlive:true
		}
	},
	methods: {
		reload() {
			this.isRouterAlive=false
			this.$nextTick(function(){
				this.isRouterAlive=true
			})
		}
	}
}
</script>

<style>
    #app {
        font-family: Georgia, Arial, sans-serif;
        margin-left: 40px;
        margin-right: 40px;
    }
</style>


<!--<template>-->
<!--<img alt="Vue logo" src="./assets/logo.png">-->
<!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--</template>-->

<!--<script>-->

<!--import HelloWorld from './components/HelloWorld.vue'-->


<!--export default {-->
<!--name: 'App',-->
<!--components: {-->
<!--HelloWorld-->
<!--}-->
<!--}-->

<!--</script>-->

<!--<style>-->
<!--#app {-->
<!--font-family: Avenir, Helvetica, Arial, sans-serif;-->
<!-- -webkit-font-smoothing: antialiased;-->
<!-- -moz-osx-font-smoothing: grayscale;-->
<!--text-align: center;-->
<!--color: #2c3e50;-->
<!--margin-top: 60px;-->
<!--}-->
<!--</style>-->
