<template>
  <div>
    <h1>Articles</h1>
    <div>
      <input v-model="searchQuery" type="text" placeholder="Enter search query">
      <button @click="fetchArticles(searchQuery)">검색</button>
    </div>
    <div v-if="articles">
      <ul>
        <li v-for="(article, index) in articles" :key="index">
          <h2>{{ article.title }}</h2>
          <p>Published Date: {{ article.pubDate }}</p>
          <p>Description: {{ article.description }}</p>
          <p>Link: <a :href="article.link" target="_blank">{{ article.originallink }}</a></p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No articles available.</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

const articles = ref(null)

const fetchArticles = function (query) {
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/news/search_news/?query=${query}`
    })
    .then((res) => {
        console.log(res.data)
        articles.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
}

</script>

<!-- 스타일링 -->
<style>
/* your styles here */
</style>

