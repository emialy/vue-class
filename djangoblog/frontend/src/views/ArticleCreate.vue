<template>
  <BlogHeader/>
  <div id="article-create">
    <h3>发表文章</h3>
    <form id="image_form">
      <div class="form-elem">
        <span>图片：</span>
        <input
            v-on:change="onFileChange"
            type="file"
            id="file"
        >
      </div>
    </form>
    <form>
      <div class="form-elem">
        <span>标题：</span>
        <input v-model="title" type="text" placeholder="输入标题">
      </div>

      <div class="form-elem">
        <span>分类：</span>
        <span
            v-for="category in categories"
            :key="category.id"
        >
                    <!--样式也可以通过 :style 绑定-->
                    <button
                        class="category-btn"
                        :style="categoryStyle(category)"
                        @click.prevent="chooseCategory(category)"
                    >
                        {{ category.title }}
                    </button>
                </span>
      </div>

      <div class="form-elem">
        <span>标签：</span>
        <input v-model="tags" type="text" placeholder="输入标签，用逗号分隔">
      </div>

      <div class="form-elem">
        <span>正文：</span>
        <textarea v-model="body" placeholder="输入正文" rows="20" cols="80" wrap="physical" ></textarea>
      </div>
      <div class="form-elem">
        <button v-on:click.prevent="judgeBadWord();submit()">提交</button>
      </div>
    </form>
  </div>
  <BlogFooter/>
</template>

<script>
import BlogHeader from '@/components/BlogHeader.vue'
import BlogFooter from '@/components/BlogFooter.vue'
import axios from 'axios';
import authorization from '@/utils/authorization';
import forbiddenArray from "../assets/js/BadWord";

export default {
  name: 'ArticleCreate',
  components: {BlogHeader, BlogFooter},
  data: function () {
    return {
      title: '',
      body: '',

      // 所有分类
      categories: [],
      // 选定的分类
      selectedCategory: null,
      // 标签
      tags: '',

      // 标题图
      avatarID: null,
      inputContent: '',
      contents: '',
      forbiddenArray: []
    }
  },
  mounted() {
    // 页面初始化时获取所有分类
    axios
        .get('/api/category/')
        .then(response => this.categories = response.data)
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      // this.imageUrl = URL.createObjectURL(file);


      let formData = new FormData();
      formData.append("content", file);

      // 省去鉴权和错误处理的部分
      axios
          .post('/api/avatar/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer ' + localStorage.getItem('access.myblog')
            }
          })
          .then(response => this.avatarID = response.data.id)
    },
    // 根据分类是否被选中，按钮的颜色发生变化
    categoryStyle(category) {
      if (this.selectedCategory !== null && category.id === this.selectedCategory.id) {
        return {
          backgroundColor: 'black',
        }
      }
      return {
        backgroundColor: 'lightgrey',
        color: 'black',
      }
    },
    // 选取分类
    chooseCategory(category) {
      // 如果点击已选取的分类，则将 selectedCategory 置空
      if (this.selectedCategory !== null && this.selectedCategory.id === category.id) {
        this.selectedCategory = null
      } else {
        this.selectedCategory = category;
      }
    },
    judgeBadWord() {
      this.forbiddenArray = forbiddenArray.forbiddenArray;
      var re = '';

      for (var i = 0; i < forbiddenArray.length; i++) {
        if (i == forbiddenArray.length - 1)
          re += forbiddenArray[i];
        else
          re += forbiddenArray[i] + "|";
      }
      //定义正则表示式对象
      //利用RegExp可以动态生成正则表示式
      var pattern = new RegExp(re, "gi");
      this.body = this.body.replace(pattern, "***")
      if (pattern.test(this.body)) {
        return false;
      } else {
        return true;
      }
    },
    // 点击提交按钮
    submit() {
      var that = this;
      authorization()
          .then(function (response) {
                if (response[0]) {
                  let data = {
                    title: that.title,
                    body: that.body,
                  };

                  // 添加标题图
                  data.avatar_id = that.avatarID;

                  // 添加分类
                  if (that.selectedCategory) {
                    data.category_id = that.selectedCategory.id
                  }
                  // 预处理并添加标签
                  // 逗号分隔标签并剔除无效标签
                  data.tags = that.tags
                      .split(/[,，]/)
                      .map(x => x.trim())
                      .filter(x => x.charAt(0) !== '');


                  // 发送发表文章请求
                  // 成功后前往详情页面
                  const token = localStorage.getItem('access.myblog');
                  axios
                      .post('/api/article/',
                          data,
                          {
                            headers: {Authorization: 'Bearer ' + token}
                          })
                      .then(function (response) {
                        that.$router.push({name: 'ArticleDetail', params: {id: response.data.id}});
                      })
                } else {
                  alert('令牌过期，请重新登录。')
                }
              }
          )
    }
  }
}
</script>

<style scoped>

.category-btn {
  margin-right: 10px;
}

#article-create {
  text-align: center;
  font-size: large;
}

form {
  text-align: left;
  padding-left: 100px;
  padding-right: 10px;
}

.form-elem {
  padding: 10px;
}

input {
  height: 25px;
  padding-left: 10px;
  width: 50%;
}

button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: steelblue;
  color: whitesmoke;
  border-radius: 5px;
  width: 60px;
}
</style>