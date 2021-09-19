import {createWebHistory, createRouter} from "vue-router";
import Home from "@/views/Home.vue";
import ArticleDetail from "@/views/ArticleDetail.vue";
import Login from "@/views/Login.vue";
import UserCenter from "../views/UserCenter.vue";
import ArticleCreate from "@/views/ArticleCreate.vue";
import ArticleEdit from "@/views/ArticleEdit.vue";
import Register from "@/views/Register.vue";
import User from "@/views/User.vue";
import DeleteUser from "../components/DeleteUser.vue";
import myArticles from "../components/myArticles.vue";
import CollectList from "../components/CollectList.vue";
import Person from "@/views/Person.vue";
import PersonalInfo from "@/views/PersonalInfo.vue";
import PersonArticle from "../components/PersonArticle.vue";
import PersonCollect from "../components/PersonCollect.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/article/:id",
        name: "ArticleDetail",
        component: ArticleDetail
    },
    {
        path: "/login",
        name: "Login",
        component: Login
    },
    {
        path: "/register",
        name: "Register",
        component: Register
    },
   {
        path: "/user/:username",
        name: "User",
        component: User,
        redirect: '/user/:username/usercenter',
        children:[
            {
                path: "/user/:username/usercenter",
                name:"UserCenter",
                component: UserCenter
            },
            {
                path: "/user/:username/myarticles",
                name:"myArticles",
                component: myArticles
            },
            {
                path: "/user/:username/collectlist",
                name:"CollectList",
                component: CollectList
            },
            {
                path: "/user/:username/deleteuser",
                name:"DeleteUser",
                component: DeleteUser
            },
        ]
    },
    {
        path: "/person/:username",
        name: "Person",
        component: Person,
        children:[
            {
                path: "/person/:username/personalinfo",
                name:"PersonalInfo",
                component: PersonalInfo
            },
            {
                path: "/person/:username/personarticle",
                name:"PersonArticle",
                component: PersonArticle
            },
            {
                path: "/person/:username/personcollect",
                name:"PersonCollect",
                component: PersonCollect
            },
        ]
    },

    {
        path: "/article/create",
        name: "ArticleCreate",
        component: ArticleCreate
    },
    {
        path: "/article/edit/:id",
        name: "ArticleEdit",
        component: ArticleEdit
    },
];

const router = createRouter({
    // https://next.router.vuejs.org/guide/essentials/history-mode.html
    history: createWebHistory(),
    routes,
});

export default router;