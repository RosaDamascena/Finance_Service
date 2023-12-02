<template>
    <div>
      <div class="d-flex justify-content-center text-center">
        <h3 class="m-0">실시간 경제 뉴스 TOP 10 <i class="fas fa-newspaper"></i> </h3>
      </div>
      <hr>
      <div class="d-flex flex-column">
        <div
          v-for="article in articles"
          :key="article.id"
          class="card mb-3"
        >
          <div class="row no-gutters">
            <div class="col-md-4">
              <img :src="article.img_link" class="card-img" alt="news_thumbnail">
            </div>
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title text-center">{{ article.title }}</h5>
                <p class="card-text">{{ article.content }}...</p>
                <button class="btn btn-primary" @click="moveToArticle(article.link)">자세히 보기</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    articles: Object
  });
  
  const moveToArticle = function (link) {
    window.open(link);
  };
  </script>
  
  <style scoped>
  .card {
    cursor: pointer;
  }
  
  .card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }
  
  .card-img {
    height: 100%;
    object-fit: cover;
  }

  /* .news_bar {
    height: 50px;
    background-color: #b3ccff;
  } */
  </style>
  