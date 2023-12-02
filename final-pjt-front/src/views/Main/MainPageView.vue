<template>
    <div>
        <ArticleList :articles="articles"/>
    </div>
    <!-- <div>
        <newsSearch />
    </div> -->
</template>

<script setup>
import ArticleList from '@/components/MainPageView/newsList.vue'
import newsSearch from '@/components/MainPageView/searchNews.vue'
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth.js'

const store = useAuthStore()

const articles = ref(null)

const loadCrawlingData = function () {
    axios({
        method: 'get',
        url: `${store.URL}/api/v1/news/economy_news/`
    })
    .then((res) => {
        console.log(res.data)
        articles.value = res.data.news_data
    })
    .catch((err) => {
        console.log(err)
    })
}


onMounted(() => {
    loadCrawlingData()
})

</script>

<style scoped>

</style>